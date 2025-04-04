from typing import Annotated, Any

from annotated_types import Le
from pydantic import BaseModel, ConfigDict
from pydantic.types import (
    NonNegativeInt,
    StringConstraints,
)


class Roi(BaseModel):
    """Region of Interest"""

    model_config = ConfigDict(validate_assignment=True)
    x1: NonNegativeInt | None = None
    x2: NonNegativeInt | None = None
    y1: NonNegativeInt | None = None
    y2: NonNegativeInt | None = None


class AcquisitionConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Annotated[str, StringConstraints(max_length=50)]
    """AcquisitionConfig mode to use for the observations"""
    exposure_time: Annotated[int, NonNegativeInt, Le(60)]
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class GuidingConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    optional: bool
    """Whether the guiding is optional or not"""
    mode: Annotated[str, StringConstraints(max_length=50)]
    """Guiding mode to use for the observations"""
    optical_elements: dict[Any, Any] | None = None
    """Optical Element specification for this GuidingConfig"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}
