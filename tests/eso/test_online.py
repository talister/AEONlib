from datetime import datetime, timedelta

import pytest

from aeonlib.eso.facility import EsoFacility
from aeonlib.eso.models import AbsoluteTimeConstraint

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


@pytest.mark.side_effect
def test_create_template():
    facility = EsoFacility()
    folder = facility.create_folder(
        ESO_TUTORIAL_CONTAINER_ID, "AEONlib.test_create_template"
    )
    ob = facility.create_ob(folder, "AEONLIB.test_create_template.ob")
    template = facility.create_template(ob, "UVES_blue_acq_slit")
    assert template.template_id
    assert len(template.parameters)
    facility.delete_template(ob, template)
    # Need to refresh observation block
    ob = facility.get_ob(ob.ob_id)
    facility.delete_ob(ob)
    # Need to refresh the container
    folder = facility.get_container(folder.container_id)
    facility.delete_container(folder)


@pytest.mark.side_effect
def test_update_template_params():
    facility = EsoFacility()
    folder = facility.create_folder(
        ESO_TUTORIAL_CONTAINER_ID, "AEONlib.test_update_template_params"
    )
    ob = facility.create_ob(folder, "AEONLIB.test_update_template_params.ob")
    template = facility.create_template(ob, "UVES_blue_acq_slit")
    # Check initial rotator mode is not SKY
    assert not any(
        p.get("name") == "INS.DROT.MODE" and p.get("value") == "SKY"
        for p in template.parameters
    )
    new_params = {
        "TEL.GS1.ALPHA": "11:22:33.000",
        "INS.DROT.MODE": "SKY",
        "INS.ADC.MODE": "AUTO",
    }
    template = facility.update_template_params(ob, template, new_params)
    # Check updated rotator mode is SKY
    assert any(
        p.get("name") == "INS.DROT.MODE" and p.get("value") == "SKY"
        for p in template.parameters
    )
    facility.delete_template(ob, template)
    # Need to refresh observation block
    ob = facility.get_ob(ob.ob_id)
    facility.delete_ob(ob)
    # Need to refresh the container
    folder = facility.get_container(folder.container_id)
    facility.delete_container(folder)


@pytest.mark.side_effect
def test_save_absolute_time_constraints():
    facility = EsoFacility()
    folder = facility.create_folder(
        ESO_TUTORIAL_CONTAINER_ID, "AEONlib.test_save_abs_time_con"
    )
    ob = facility.create_ob(folder, "AEONLIB.test_save_abs_time_con.ob")
    abs_constraints = facility.get_absolute_time_constraints(ob)
    assert len(abs_constraints.constraints) == 0
    abs_constraints.constraints.append(
        AbsoluteTimeConstraint(
            start=datetime.now(), end=datetime.now() + timedelta(days=30)
        )
    )
    new_abs_constraints = facility.save_absolute_time_constraints(ob, abs_constraints)
    # Saving loses some precision on time, so just compare the date for this test
    assert (
        new_abs_constraints.constraints[0].start.date()
        == abs_constraints.constraints[0].start.date()
    )
    assert (
        new_abs_constraints.constraints[0].end.date()
        == abs_constraints.constraints[0].end.date()
    )
    facility.delete_ob(ob)
    # Need to refresh the container
    folder = facility.get_container(folder.container_id)
    facility.delete_container(folder)
