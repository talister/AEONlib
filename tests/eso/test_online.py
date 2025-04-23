import pytest

from aeonlib.eso.facility import EsoFacility

pytestmark = pytest.mark.online


@pytest.mark.side_effect
def test_create_folder():
    facility = EsoFacility()
    # ID from ESO p2 docs: https://www.eso.org/copdemo/apidoc/index.html
    run_container_id = 1538878
    container = facility.create_folder(run_container_id, "AEONlib Unit Test")
    assert container.name == "AEONlib Unit Test"
    assert container.parent_container_id == run_container_id
    assert container.run_id
