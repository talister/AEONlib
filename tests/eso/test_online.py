import pytest

from aeonlib.eso.facility import EsoFacility

pytestmark = pytest.mark.online

# ID from ESO p2 docs: https://www.eso.org/copdemo/apidoc/index.html
ESO_TUTORIAL_CONTAINER_ID = 1538878


@pytest.mark.side_effect
def test_create_folder():
    facility = EsoFacility()
    folder = facility.create_folder(
        ESO_TUTORIAL_CONTAINER_ID, "AEONlib.test_create_folder"
    )
    assert folder.name == "AEONlib.test_create_folder"
    assert folder.parent_container_id == ESO_TUTORIAL_CONTAINER_ID
    assert folder.container_id
    facility.delete_container(folder)


@pytest.mark.side_effect
def test_create_ob():
    facility = EsoFacility()
    folder = facility.create_folder(ESO_TUTORIAL_CONTAINER_ID, "AEONlib.test_create_ob")
    ob = facility.create_ob(folder, "AEONLIB.test_create_ob.ob")
    assert ob.ob_id
    assert ob.name == "AEONLIB.test_create_ob.ob"
    assert ob.item_type == "OB"
    facility.delete_ob(ob)
    # Need to refresh the container
    folder = facility.get_container(folder.container_id)
    facility.delete_container(folder)


@pytest.mark.side_effect
def test_save_ob():
    facility = EsoFacility()
    folder = facility.create_folder(ESO_TUTORIAL_CONTAINER_ID, "AEONlib.test_save_ob")
    ob = facility.create_ob(folder, "AEONLIB.test_save_ob.ob")
    ob.name = "AEONlib.test_save_ob.ob-MODIFIED"
    ob.target.name = "m51"
    new_ob = facility.save_ob(ob)
    assert new_ob.ob_id == ob.ob_id
    assert new_ob.name == ob.name
    assert new_ob.target.name == ob.target.name
    facility.delete_ob(new_ob)
    # Need to refresh the container
    folder = facility.get_container(folder.container_id)
    facility.delete_container(folder)
