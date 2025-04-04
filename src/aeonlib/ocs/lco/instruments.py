from typing import Any, Literal, Union

from pydantic import BaseModel, ConfigDict
from pydantic.types import (
    NonNegativeInt,
    PositiveInt,
)

from aeonlib.ocs.target_models import Constraints, Target
from aeonlib.ocs.config_models import AcquisitionConfig, GuidingConfig, Roi


class LcoSoarGhtsBluecamImagerConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds (TODO: can this really be 0?)"""
    mode: Literal["GHTS_B_Image_2x2"]
    rois: list[Roi] | None = None
    extra_params: dict[Any, Any] = {}
    """This is completely generated at runtime via configdb stuff"""
    filters: Literal["u-SDSS", "g-SDSS", "r-SDSS", "i-SDSS"]


class LcoSoarGhtsBluecamImager(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    type: Literal["EXPOSE"]
    instrument_type: str = "SOAR_GHTS_BLUECAM_IMAGER"
    repeat_duration: NonNegativeInt = 0
    instrument_configs: list[LcoSoarGhtsBluecamImagerConfig] = []
    target: Target
    constraints: Constraints
    # TODO: These should be instrument specific
    guiding_config: GuidingConfig | None = None
    acquisition_config: AcquisitionConfig | None = None
class Lco1M0NresScicamConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds (TODO: can this really be 0?)"""
    mode: Literal["default"]
    rotator_mode: Literal["VFLOAT"]
    rois: list[Roi] | None = None
    extra_params: dict[Any, Any] = {}
    """This is completely generated at runtime via configdb stuff"""


class Lco1M0NresScicam(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    type: Literal["NRES_SPECTRUM", "REPEAT_NRES_SPECTRUM", "NRES_EXPOSE", "NRES_TEST", "SCRIPT", "ENGINEERING", "ARC", "LAMP_FLAT", "NRES_BIAS", "NRES_DARK", "AUTO_FOCUS"]
    instrument_type: str = "1M0-NRES-SCICAM"
    repeat_duration: NonNegativeInt = 0
    instrument_configs: list[Lco1M0NresScicamConfig] = []
    target: Target
    constraints: Constraints
    # TODO: These should be instrument specific
    guiding_config: GuidingConfig | None = None
    acquisition_config: AcquisitionConfig | None = None
class Lco2M0FloydsScicamConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds (TODO: can this really be 0?)"""
    mode: Literal["default"]
    rotator_mode: Literal["VFLOAT"]
    rois: list[Roi] | None = None
    extra_params: dict[Any, Any] = {}
    """This is completely generated at runtime via configdb stuff"""
    slits: Literal["slit_6.0as", "slit_1.6as", "slit_2.0as", "slit_1.2as"]


class Lco2M0FloydsScicam(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    type: Literal["SPECTRUM", "REPEAT_SPECTRUM", "ARC", "ENGINEERING", "SCRIPT", "LAMP_FLAT"]
    instrument_type: str = "2M0-FLOYDS-SCICAM"
    repeat_duration: NonNegativeInt = 0
    instrument_configs: list[Lco2M0FloydsScicamConfig] = []
    target: Target
    constraints: Constraints
    # TODO: These should be instrument specific
    guiding_config: GuidingConfig | None = None
    acquisition_config: AcquisitionConfig | None = None
class Lco2M0ScicamMuscatConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds (TODO: can this really be 0?)"""
    mode: Literal["MUSCAT_SLOW", "MUSCAT_FAST"]
    rois: list[Roi] | None = None
    extra_params: dict[Any, Any] = {}
    """This is completely generated at runtime via configdb stuff"""
    narrowband_g_positions: Literal["out", "in"]
    narrowband_r_positions: Literal["out", "in"]
    narrowband_i_positions: Literal["out", "in"]
    narrowband_z_positions: Literal["out", "in"]


class Lco2M0ScicamMuscat(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    type: Literal["EXPOSE", "REPEAT_EXPOSE", "BIAS", "DARK", "STANDARD", "SCRIPT", "AUTO_FOCUS", "ENGINEERING", "SKY_FLAT"]
    instrument_type: str = "2M0-SCICAM-MUSCAT"
    repeat_duration: NonNegativeInt = 0
    instrument_configs: list[Lco2M0ScicamMuscatConfig] = []
    target: Target
    constraints: Constraints
    # TODO: These should be instrument specific
    guiding_config: GuidingConfig | None = None
    acquisition_config: AcquisitionConfig | None = None
class LcoSoarGhtsRedcamConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds (TODO: can this really be 0?)"""
    mode: Literal["GHTS_R_1200_CaNIR_6300A_1x2_slit0p8", "GHTS_R_400m1_2x2", "GHTS_R_400m2_2x2", "GHTS_R_1200_CaNIR_1x2_slit0p8", "GHTS_R_2100_5000A_1x2_slit1p0", "GHTS_R_2100_6507A_1x2_slit0p45"]
    rotator_mode: Literal["VFLOAT"]
    rois: list[Roi] | None = None
    extra_params: dict[Any, Any] = {}
    """This is completely generated at runtime via configdb stuff"""


class LcoSoarGhtsRedcam(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    type: Literal["SPECTRUM", "ENGINEERING", "SCRIPT", "ARC", "LAMP_FLAT"]
    instrument_type: str = "SOAR_GHTS_REDCAM"
    repeat_duration: NonNegativeInt = 0
    instrument_configs: list[LcoSoarGhtsRedcamConfig] = []
    target: Target
    constraints: Constraints
    # TODO: These should be instrument specific
    guiding_config: GuidingConfig | None = None
    acquisition_config: AcquisitionConfig | None = None
class LcoSoarGhtsRedcamImagerConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds (TODO: can this really be 0?)"""
    mode: Literal["GHTS_R_Image_2x2"]
    rois: list[Roi] | None = None
    extra_params: dict[Any, Any] = {}
    """This is completely generated at runtime via configdb stuff"""
    filters: Literal["g-SDSS", "r-SDSS", "i-SDSS", "z-SDSS"]


class LcoSoarGhtsRedcamImager(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    type: Literal["EXPOSE"]
    instrument_type: str = "SOAR_GHTS_REDCAM_IMAGER"
    repeat_duration: NonNegativeInt = 0
    instrument_configs: list[LcoSoarGhtsRedcamImagerConfig] = []
    target: Target
    constraints: Constraints
    # TODO: These should be instrument specific
    guiding_config: GuidingConfig | None = None
    acquisition_config: AcquisitionConfig | None = None
class LcoSoarTriplespecConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds (TODO: can this really be 0?)"""
    mode: Literal["fowler1_coadds2", "fowler4_coadds1", "fowler8_coadds1", "fowler16_coadds1", "fowler1_coadds1"]
    rotator_mode: Literal["VFLOAT"]
    rois: list[Roi] | None = None
    extra_params: dict[Any, Any] = {}
    """This is completely generated at runtime via configdb stuff"""


class LcoSoarTriplespec(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    type: Literal["SPECTRUM", "STANDARD", "ARC", "LAMP_FLAT", "BIAS"]
    instrument_type: str = "SOAR_TRIPLESPEC"
    repeat_duration: NonNegativeInt = 0
    instrument_configs: list[LcoSoarTriplespecConfig] = []
    target: Target
    constraints: Constraints
    # TODO: These should be instrument specific
    guiding_config: GuidingConfig | None = None
    acquisition_config: AcquisitionConfig | None = None
class LcoSoarGhtsBluecamConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds (TODO: can this really be 0?)"""
    mode: Literal["GHTS_B_400m1_2x2"]
    rotator_mode: Literal["VFLOAT"]
    rois: list[Roi] | None = None
    extra_params: dict[Any, Any] = {}
    """This is completely generated at runtime via configdb stuff"""


class LcoSoarGhtsBluecam(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    type: Literal["SPECTRUM", "ENGINEERING", "SCRIPT", "LAMP_FLAT", "ARC"]
    instrument_type: str = "SOAR_GHTS_BLUECAM"
    repeat_duration: NonNegativeInt = 0
    instrument_configs: list[LcoSoarGhtsBluecamConfig] = []
    target: Target
    constraints: Constraints
    # TODO: These should be instrument specific
    guiding_config: GuidingConfig | None = None
    acquisition_config: AcquisitionConfig | None = None
class Lco1M0ScicamSinistroConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds (TODO: can this really be 0?)"""
    mode: Literal["full_frame", "central_2k_2x2"]
    rois: list[Roi] | None = None
    extra_params: dict[Any, Any] = {}
    """This is completely generated at runtime via configdb stuff"""
    filters: Literal["I", "R", "U", "w", "Y", "up", "rp", "ip", "gp", "zs", "V", "B", "400um-Pinhole", "150um-Pinhole", "CN"]


class Lco1M0ScicamSinistro(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    type: Literal["EXPOSE", "REPEAT_EXPOSE", "BIAS", "DARK", "STANDARD", "SCRIPT", "AUTO_FOCUS", "ENGINEERING", "SKY_FLAT"]
    instrument_type: str = "1M0-SCICAM-SINISTRO"
    repeat_duration: NonNegativeInt = 0
    instrument_configs: list[Lco1M0ScicamSinistroConfig] = []
    target: Target
    constraints: Constraints
    # TODO: These should be instrument specific
    guiding_config: GuidingConfig | None = None
    acquisition_config: AcquisitionConfig | None = None
class Lco0M4ScicamQhy600Config(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds (TODO: can this really be 0?)"""
    mode: Literal["central30x30", "full_frame"]
    rois: list[Roi] | None = None
    extra_params: dict[Any, Any] = {}
    """This is completely generated at runtime via configdb stuff"""
    filters: Literal["OIII", "SII", "Astrodon-Exo", "w", "opaque", "up", "rp", "ip", "gp", "zs", "V", "B", "H-Alpha"]


class Lco0M4ScicamQhy600(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    type: Literal["EXPOSE", "REPEAT_EXPOSE", "AUTO_FOCUS", "BIAS", "DARK", "STANDARD", "SKY_FLAT"]
    instrument_type: str = "0M4-SCICAM-QHY600"
    repeat_duration: NonNegativeInt = 0
    instrument_configs: list[Lco0M4ScicamQhy600Config] = []
    target: Target
    constraints: Constraints
    # TODO: These should be instrument specific
    guiding_config: GuidingConfig | None = None
    acquisition_config: AcquisitionConfig | None = None
class LcoBlancoNewfirmConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds (TODO: can this really be 0?)"""
    mode: Literal["fowler1_coadds1", "fowler8_coadds1", "fowler16_coadds1"]
    rois: list[Roi] | None = None
    extra_params: dict[Any, Any] = {}
    """This is completely generated at runtime via configdb stuff"""
    filters: Literal["JX", "HX", "KXs", "1187", "2096", "1644", "2124", "2168", "J1", "1066", "DARK"]


class LcoBlancoNewfirm(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    type: Literal["EXPOSE", "SKY_FLAT", "STANDARD", "DARK"]
    instrument_type: str = "BLANCO_NEWFIRM"
    repeat_duration: NonNegativeInt = 0
    instrument_configs: list[LcoBlancoNewfirmConfig] = []
    target: Target
    constraints: Constraints
    # TODO: These should be instrument specific
    guiding_config: GuidingConfig | None = None
    acquisition_config: AcquisitionConfig | None = None


# Export a list of all instrument classes
LCO_INSTRUMENTS = Union[
    LcoSoarGhtsBluecamImager,
    Lco1M0NresScicam,
    Lco2M0FloydsScicam,
    Lco2M0ScicamMuscat,
    LcoSoarGhtsRedcam,
    LcoSoarGhtsRedcamImager,
    LcoSoarTriplespec,
    LcoSoarGhtsBluecam,
    Lco1M0ScicamSinistro,
    Lco0M4ScicamQhy600,
    LcoBlancoNewfirm,
]