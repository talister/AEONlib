from datetime import datetime, timedelta

import pytest

from aeonlib.eso.facility import EsoFacility
from aeonlib.eso.models import (
    AbsoluteTimeConstraint,
    AbsoluteTimeConstraints,
    Ephemeris,
    SiderealTimeConstraint,
    SiderealTimeConstraints,
)

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
    abs_constraints = AbsoluteTimeConstraints(
        constraints=[
            AbsoluteTimeConstraint(
                start=datetime.now(), end=datetime.now() + timedelta(days=30)
            )
        ]
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


@pytest.mark.side_effect
def test_save_sidereal_time_constraints():
    facility = EsoFacility()
    folder = facility.create_folder(
        ESO_TUTORIAL_CONTAINER_ID, "AEONlib.test_save_sidereal_time_con"
    )
    ob = facility.create_ob(folder, "AEONLIB.test_save_sidereal_time_con.ob")
    sidereal_constraints = SiderealTimeConstraints(
        constraints=[
            SiderealTimeConstraint(
                start=datetime.now().strftime("%H:%M"),
                end=(datetime.now() + timedelta(hours=1)).strftime("%H:%M"),
            )
        ]
    )
    new_sidereal_constraints = facility.save_sidereal_time_constraints(
        ob, sidereal_constraints
    )
    assert (
        new_sidereal_constraints.constraints[0].start
        == sidereal_constraints.constraints[0].start
    )
    assert (
        new_sidereal_constraints.constraints[0].end
        == sidereal_constraints.constraints[0].end
    )
    facility.delete_ob(ob)
    # Need to refresh the container
    folder = facility.get_container(folder.container_id)
    facility.delete_container(folder)


@pytest.mark.skip(reason="Errors with 'Ephemeris file must have at least two records.'")
@pytest.mark.side_effect
def test_save_ephemeris():
    ephemeris_text = """    PAF.HDR.START,            # Start of PAF Header
    PAF.TYPE                  "Instrument Setup", # Type of PAF
    PAF.ID                    "", # ID for PAF
    PAF.NAME                  "{PAFNAME}",# Name of PAF
    PAF.DESC                  "Ephemeris / Eproc-4.3, 2025-04-30 20:54:26, IMCCE/OBSPM/CNRS"
    PAF.DESC                  "Target body name: Ceres (1)"
    PAF.DESC                  "Center body name: Earth {source: INPOP}"
    PAF.DESC                  "Center-site name: Cerro Paranal"
    PAF.DESC                  "Start time      : A.D. 2025-Apr-30 00:00:00.0000 UT"
    PAF.DESC                  "Stop  time      : A.D. 2025-May-03 00:00:00.0000 UT"
    PAF.DESC                  "Step-size       : 1.0  hours"
    PAF.DESC                  "Target pole/equ : IAU {East-longitude -}"
    PAF.DESC                  "Target radii    : 424.20 x 424.20 x 424.20 km {Equator, meridian, pole}"
    PAF.DESC                  "Atmos refraction: NO (AIRLESS)"
    PAF.CRTE.NAME             "Eproc.ephemcc", # Name of creator
    PAF.HDR.END,              # End of PAF Header
    # Ephem cuts: AM = 2.60, Sun elevation = 0.00 deg.
    #------------------------------------------------------------------------------
    #                              Date & Time (UT)             JD              RA (J2000)     Dec (J2000)    dRA ("/s)   dDEC ("/s)   V-mag  Slit PA
    #------------------------------------------------------------------------------
    INS.EPHEM.RECORD          "2025-04-30T10:00:00.000, 60795.41666666666, 23 52 34.5819, -10 14 26.580, 0.01342419, 0.00461927, 9.2919, 0.000, *"
    INS.EPHEM.RECORD          "2025-04-30T11:00:00.000, 60795.45833333334, 23 52 37.8514, -10 14 09.945, 0.01338837, 0.00462241, 9.2919, 0.000, *"
    #------------------------------------------------------------------------------
    INS.EPHEM.RECORD          "2025-05-01T10:00:00.000, 60796.41666666666, 23 53 53.4767, -10 07 46.780, 0.01337469, 0.00458595, 9.2913, 0.000, *"
    INS.EPHEM.RECORD          "2025-05-01T11:00:00.000, 60796.45833333334, 23 53 56.7330, -10 07 30.265, 0.01333904, 0.00458910, 9.2913, 0.000, *"
    #------------------------------------------------------------------------------
    INS.EPHEM.RECORD          "2025-05-02T10:00:00.000, 60797.41666666666, 23 55 12.0632, -10 01 09.917, 0.01332444, 0.00455202, 9.2906, 0.000, *"
    INS.EPHEM.RECORD          "2025-05-02T11:00:00.000, 60797.45833333334, 23 55 15.3062, -10 00 53.524, 0.01328897, 0.00455516, 9.2905, 0.000, *"
    #------------------------------------------------------------------------------"""
    facility = EsoFacility()
    folder = facility.create_folder(
        ESO_TUTORIAL_CONTAINER_ID, "AEONlib.test_save_ephemeris"
    )
    ob = facility.create_ob(folder, "AEONLIB.test_save_ephemeris.ob")
    ephemeris = Ephemeris(text=ephemeris_text)
    new_ephemeris = facility.save_ephemeris(ob, ephemeris)
    assert new_ephemeris.text == ephemeris.text
    facility.delete_ephemeris(ob, new_ephemeris)
    facility.delete_ob(ob)
    # Need to refresh the container
    folder = facility.get_container(folder.container_id)
    facility.delete_container(folder)
