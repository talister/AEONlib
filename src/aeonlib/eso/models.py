from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class EsoModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel, validate_by_name=True, serialize_by_alias=True
    )


class Container(EsoModel):
    container_id: int
    item_count: int
    item_type: str
    name: str
    parent_container_id: int
    run_id: int
