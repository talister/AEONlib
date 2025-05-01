"""
Models shared between facilities.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from aeonlib.types import Time


class Window(BaseModel):
    """A general time window"""

    model_config = ConfigDict(validate_assignment=True)
    start: Time | datetime | None = None
    end: Time | datetime
