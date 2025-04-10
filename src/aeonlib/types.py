from datetime import datetime
from typing import Annotated, Any, Type

import astropy.time
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema


class _AstropyTimeType:
    """
    Custom Pydantic type that handles astropy.time.Time serialization and parsing.
    This should enable using astropy Time objects as pydantic fields that are interoperable
    with datetime objects.
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Type[Any],
        _handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        """https://docs.pydantic.dev/latest/concepts/types/#handling-third-party-types"""

        def validate_from_datetime(datetime_value: datetime) -> astropy.time.Time:
            return astropy.time.Time(datetime_value)

        from_datetime_schema = core_schema.chain_schema(
            [
                core_schema.datetime_schema(),
                core_schema.no_info_plain_validator_function(validate_from_datetime),
            ]
        )

        def serialize_time(time_obj: astropy.time.Time) -> datetime:
            """
            Determines how to serialize an astropy.time.Time object when model_dump()
            is called. Potentially we could leave this as is and have astropy times
            in dictionaries, but Pydantic handles datetimes natively so this seems to
            be the path of least resistance.
            """
            return time_obj.datetime  # type: ignore

        return core_schema.json_or_python_schema(
            json_schema=from_datetime_schema,
            python_schema=core_schema.union_schema(
                [
                    # Try Time directly first
                    core_schema.is_instance_schema(astropy.time.Time),
                    # Then try datetime
                    from_datetime_schema,
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                serialize_time
            ),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, _core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        # Use the same schema that would be used for `datetime`
        return handler(core_schema.datetime_schema())


Time = Annotated[astropy.time.Time, _AstropyTimeType]
