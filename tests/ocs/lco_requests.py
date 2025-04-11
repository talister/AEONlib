from datetime import datetime, timedelta

from aeonlib.ocs import (
    Constraints,
    Location,
    Request,
    RequestGroup,
    SiderealTarget,
    Window,
)
from aeonlib.ocs.lco.instruments import (
    Lco1M0ScicamSinistro,
    Lco2M0FloydsScicam,
    Lco2M0ScicamMuscat,
)

lco_1m0_scicam_sinistro = RequestGroup(
    name="test",
    observation_type="NORMAL",
    operator="SINGLE",
    proposal="TEST_PROPOSAL",
    submitter_id="bob",
    ipp_value=1.0,
    requests=[
        Request(
            location=Location(telescope_class="1m0"),
            configurations=[
                Lco1M0ScicamSinistro(
                    type="EXPOSE",
                    target=SiderealTarget(
                        name="M51", type="ICRS", ra=202.469, dec=47.195
                    ),
                    constraints=Constraints(),
                    instrument_configs=[
                        Lco1M0ScicamSinistro.config_class(
                            exposure_count=1,
                            exposure_time=10,
                            mode="central_2k_2x2",
                            optical_elements=Lco1M0ScicamSinistro.optical_elements_class(
                                filter="B"
                            ),
                        )
                    ],
                    acquisition_config=Lco1M0ScicamSinistro.acquisition_config_class(
                        mode="OFF"
                    ),
                    guiding_config=Lco1M0ScicamSinistro.guiding_config_class(
                        mode="ON", optional=True
                    ),
                )
            ],
            windows=[
                Window(
                    start=datetime.now(),
                    end=datetime.now() + timedelta(days=30),
                )
            ],
        )
    ],
)

lco_2m0_floyds_scicam = RequestGroup(
    name="test",
    observation_type="NORMAL",
    operator="SINGLE",
    proposal="TEST_PROPOSAL",
    submitter_id="bob",
    ipp_value=1.0,
    requests=[
        Request(
            location=Location(telescope_class="2m0"),
            configurations=[
                Lco2M0FloydsScicam(
                    type="SPECTRUM",
                    target=SiderealTarget(
                        name="M51", type="ICRS", ra=202.469, dec=47.195
                    ),
                    constraints=Constraints(),
                    instrument_configs=[
                        Lco2M0FloydsScicam.config_class(
                            rotator_mode="VFLOAT",
                            exposure_count=1,
                            exposure_time=10,
                            mode="default",
                            optical_elements=Lco2M0FloydsScicam.optical_elements_class(
                                slit="slit_6.0as"
                            ),
                        )
                    ],
                    acquisition_config=Lco2M0FloydsScicam.acquisition_config_class(
                        mode="WCS"
                    ),
                    guiding_config=Lco2M0FloydsScicam.guiding_config_class(
                        mode="ON", optional=True
                    ),
                )
            ],
            windows=[
                Window(
                    start=datetime.now(),
                    end=datetime.now() + timedelta(days=30),
                )
            ],
        )
    ],
)

lco_2m0_scicam_muscat = RequestGroup(
    name="test",
    observation_type="NORMAL",
    operator="SINGLE",
    proposal="TEST_PROPOSAL",
    submitter_id="bob",
    ipp_value=1.0,
    requests=[
        Request(
            location=Location(telescope_class="2m0"),
            configurations=[
                Lco2M0ScicamMuscat(
                    type="EXPOSE",
                    target=SiderealTarget(
                        name="M51", type="ICRS", ra=202.469, dec=47.195
                    ),
                    constraints=Constraints(),
                    instrument_configs=[
                        Lco2M0ScicamMuscat.config_class(
                            exposure_count=1,
                            exposure_time=10,
                            mode="MUSCAT_FAST",
                            optical_elements=Lco2M0ScicamMuscat.optical_elements_class(
                                narrowband_g_position="in",
                                narrowband_r_position="out",
                                narrowband_i_position="in",
                                narrowband_z_position="out",
                            ),
                            extra_params={  # Hate this. TODO: Hoist these to class
                                "exposure_time_g": 10,
                                "exposure_time_r": 10,
                                "exposure_time_i": 10,
                                "exposure_time_z": 10,
                            },
                        )
                    ],
                    acquisition_config=Lco2M0ScicamMuscat.acquisition_config_class(
                        mode="OFF"
                    ),
                    guiding_config=Lco2M0ScicamMuscat.guiding_config_class(
                        mode="ON", optional=True
                    ),
                )
            ],
            windows=[
                Window(
                    start=datetime.now(),
                    end=datetime.now() + timedelta(days=30),
                )
            ],
        )
    ],
)

LCO_REQUESTS = {
    "lco_1m0_scicam_sinistro": lco_1m0_scicam_sinistro,
    "lco_2m0_floyds_scicam": lco_2m0_floyds_scicam,
    "lco_2m0_scicam_muscat": lco_2m0_scicam_muscat,
}
