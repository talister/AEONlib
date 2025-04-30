from datetime import datetime

import pytest
from astropy.time import Time

from aeonlib.eso.models import AbsoluteTimeConstraint
from aeonlib.models import Window


def test_constraints_from_window():
    window = Window(
        start=Time(60775.0, scale="utc", format="mjd"),
        end=Time(60776.0, scale="utc", format="mjd"),
    )

    abs_constraint = AbsoluteTimeConstraint.from_window(window)

    assert abs_constraint.start == datetime(2025, 4, 10, 0, 0)
    assert abs_constraint.end == datetime(2025, 4, 11, 0, 0)


def test_constraints_from_window_must_enter_start():
    with pytest.raises(ValueError):
        AbsoluteTimeConstraint.from_window(
            Window(start=None, end=Time(60776.0, scale="utc", format="mjd"))
        )
