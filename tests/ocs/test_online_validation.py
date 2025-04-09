"""
These tests do real validation against an LCO OCS API. To run them, you
must run the "online" mark explicitly: pytest -m online.

By default test will run against an OCS running at http://localhost:8000
set the AEONLIB_TEST_OCS environmental variable to test against a different
address.

The LCO requests assume you are a member of a proposal named TEST_PROPOSAL that has time
on all instruments.
"""

import logging
import os

import pytest

from aeonlib.ocs.lco.facility import LcoFacility
from aeonlib.ocs.request_models import RequestGroup

from .lco_requests import LCO_REQUESTS

logger = logging.getLogger(__name__)
pytestmark = pytest.mark.online


@pytest.fixture
def facility() -> LcoFacility:
    api_root = os.getenv("AEONLIB_TEST_OCS", "http://localhost:8000/api")
    return LcoFacility(api_root=api_root)


@pytest.mark.parametrize(
    "request_group", LCO_REQUESTS.values(), ids=LCO_REQUESTS.keys()
)
def test_valid_requests(facility: LcoFacility, request_group: RequestGroup):
    valid, errors = facility.validate_request_group(request_group)
    if not valid:
        logger.error("Online validation failed. Server response: %s", errors)
    assert valid
