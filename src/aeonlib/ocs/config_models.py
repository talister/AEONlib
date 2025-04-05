from typing import ClassVar, Protocol

from pydantic import BaseModel, ConfigDict, computed_field
from pydantic.types import NonNegativeInt


class Roi(BaseModel):
    """Region of Interest"""

    model_config = ConfigDict(validate_assignment=True)
    x1: NonNegativeInt | None = None
    x2: NonNegativeInt | None = None
    y1: NonNegativeInt | None = None
    y2: NonNegativeInt | None = None


class HasOpticalElementsProtocol(Protocol):
    optical_element_fields: ClassVar[list[str]]


class OpticalElementsMixin:
    """
    Adds the `optical_elements` attribute to classes that require it.

    Currently we flatten optical elements into the parent object so we
    can write this:
        instrument.config.filter = "r"
    Instead of this:
        instrument.config.optical_elements.filter = "r"
    The latter being somewhat annoying because it would require generating
    another unique class per instrument.
    """

    @computed_field
    @property
    def optical_elements(self: HasOpticalElementsProtocol) -> dict[str, str]:
        return {key: getattr(self, key) for key in self.optical_element_fields}
