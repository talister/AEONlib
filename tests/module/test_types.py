import json
from datetime import datetime

from astropy.time import Time
from pydantic import BaseModel

import aeonlib.types


class Window(BaseModel):
    """
    A window of time similar to ocs.request_models.Window
    used for testing the custom time type
    """

    start: aeonlib.types.Time | datetime | None = None
    end: aeonlib.types.Time | datetime


class TestAstropyTime:
    def test_with_astropy_time(self):
        """
        Test that the window constructed with astropy Times has datetimes when dumped
        """
        window = Window(
            start=Time(60775.0, scale="utc", format="mjd"),
            end=Time(60776.0, scale="utc", format="mjd"),
        )
        assert window.model_dump()["start"] == datetime(2025, 4, 10, 0, 0, 0, 0)
        assert window.model_dump()["end"] == datetime(2025, 4, 11, 0, 0, 0, 0)

    def test_with_astropy_time_json(self):
        """
        Test that the window constructed with astropy Times dumps to JSON properly
        """
        window = Window(
            start=Time(60775.0, scale="utc", format="mjd"),
            end=Time(60776.0, scale="utc", format="mjd"),
        )
        as_json = json.loads(window.model_dump_json())
        assert as_json["start"] == "2025-04-10T00:00:00"
        assert as_json["end"] == "2025-04-11T00:00:00"

    def test_from_datetime(self):
        """
        Test that we can construct windows using datetimes instead of astropy Times
        """
        window = Window(
            start=datetime(2025, 4, 10, 0, 0, 0, 0),
            end=datetime(2025, 4, 11, 0, 0, 0, 0),
        )
        assert window.model_dump()["start"] == datetime(2025, 4, 10, 0, 0, 0, 0)
        assert window.model_dump()["end"] == datetime(2025, 4, 11, 0, 0, 0, 0)

    def test_from_datetime_json(self):
        """
        Test that the window constructed with datetimes dumps to JSON properly
        """
        window = Window(
            start=datetime(2025, 4, 10, 0, 0, 0, 0),
            end=datetime(2025, 4, 11, 0, 0, 0, 0),
        )
        as_json = json.loads(window.model_dump_json())
        assert as_json["start"] == "2025-04-10T00:00:00"
        assert as_json["end"] == "2025-04-11T00:00:00"

    def test_from_json(self):
        """
        Test that windows can be parsed from JSON and the resulting object contains
        astropy Time objects
        """
        window_json = json.dumps(
            {
                "start": "2025-04-10T00:00:00",
                "end": "2025-04-11T00:00:00",
            }
        )
        window = Window.model_validate_json(window_json)
        assert isinstance(window.start, Time)
        assert window.start == Time(datetime(2025, 4, 10, 0, 0, 0, 0))
        assert isinstance(window.end, Time)
        assert window.end == Time(datetime(2025, 4, 11, 0, 0, 0, 0))
