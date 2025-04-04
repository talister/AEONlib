from typing import Any, Annotated, Literal, Union

from annotated_types import Le
from pydantic import BaseModel, ConfigDict
from pydantic.types import (
    NonNegativeInt,
    PositiveInt,
)

from aeonlib.ocs.target_models import Constraints, Target
from aeonlib.ocs.config_models import Roi


class LcoSoarGhtsBluecamImagerGuidingConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["OFF", "ON"]
    optional: bool
    """Whether the guiding is optional or not"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}


class LcoSoarGhtsBluecamImagerAcquisitionConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["MANUAL"]
    exposure_time: Annotated[int, NonNegativeInt, Le(60)] = 60
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class LcoSoarGhtsBluecamImagerConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds"""
    mode: Literal["GHTS_B_Image_2x2"]
    rotator_mode: Literal["SKY"]
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
    guiding_config: LcoSoarGhtsBluecamImagerGuidingConfig | None = None
    acquisition_config: LcoSoarGhtsBluecamImagerAcquisitionConfig | None = None


class Lco1M0NresScicamGuidingConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["ON"]
    optional: bool
    """Whether the guiding is optional or not"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}


class Lco1M0NresScicamAcquisitionConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["WCS", "BRIGHTEST"]
    exposure_time: Annotated[int, NonNegativeInt, Le(60)] = 60
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class Lco1M0NresScicamConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds"""
    mode: Literal["default"]
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
    guiding_config: Lco1M0NresScicamGuidingConfig | None = None
    acquisition_config: Lco1M0NresScicamAcquisitionConfig | None = None


class Lco2M0FloydsScicamGuidingConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["OFF", "ON"]
    optional: bool
    """Whether the guiding is optional or not"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}


class Lco2M0FloydsScicamAcquisitionConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["BRIGHTEST", "WCS"]
    exposure_time: Annotated[int, NonNegativeInt, Le(60)] = 60
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class Lco2M0FloydsScicamConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds"""
    mode: Literal["default"]
    rotator_mode: Literal["VFLOAT", "SKY"]
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
    guiding_config: Lco2M0FloydsScicamGuidingConfig | None = None
    acquisition_config: Lco2M0FloydsScicamAcquisitionConfig | None = None


class Lco2M0ScicamMuscatGuidingConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["ON", "OFF"]
    optional: bool
    """Whether the guiding is optional or not"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}


class Lco2M0ScicamMuscatAcquisitionConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["OFF"]
    exposure_time: Annotated[int, NonNegativeInt, Le(60)] = 60
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class Lco2M0ScicamMuscatConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds"""
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
    guiding_config: Lco2M0ScicamMuscatGuidingConfig | None = None
    acquisition_config: Lco2M0ScicamMuscatAcquisitionConfig | None = None


class LcoSoarGhtsRedcamGuidingConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["ON"]
    optional: bool
    """Whether the guiding is optional or not"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}


class LcoSoarGhtsRedcamAcquisitionConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["MANUAL"]
    exposure_time: Annotated[int, NonNegativeInt, Le(60)] = 60
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class LcoSoarGhtsRedcamConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds"""
    mode: Literal["GHTS_R_1200_CaNIR_6300A_1x2_slit0p8", "GHTS_R_400m1_2x2", "GHTS_R_400m2_2x2", "GHTS_R_1200_CaNIR_1x2_slit0p8", "GHTS_R_2100_5000A_1x2_slit1p0", "GHTS_R_2100_6507A_1x2_slit0p45"]
    rotator_mode: Literal["SKY"]
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
    guiding_config: LcoSoarGhtsRedcamGuidingConfig | None = None
    acquisition_config: LcoSoarGhtsRedcamAcquisitionConfig | None = None


class LcoSoarGhtsRedcamImagerGuidingConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["OFF", "ON"]
    optional: bool
    """Whether the guiding is optional or not"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}


class LcoSoarGhtsRedcamImagerAcquisitionConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["MANUAL"]
    exposure_time: Annotated[int, NonNegativeInt, Le(60)] = 60
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class LcoSoarGhtsRedcamImagerConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds"""
    mode: Literal["GHTS_R_Image_2x2"]
    rotator_mode: Literal["SKY"]
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
    guiding_config: LcoSoarGhtsRedcamImagerGuidingConfig | None = None
    acquisition_config: LcoSoarGhtsRedcamImagerAcquisitionConfig | None = None


class LcoSoarTriplespecGuidingConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["ON"]
    optional: bool
    """Whether the guiding is optional or not"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}


class LcoSoarTriplespecAcquisitionConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["MANUAL"]
    exposure_time: Annotated[int, NonNegativeInt, Le(60)] = 60
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class LcoSoarTriplespecConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds"""
    mode: Literal["fowler1_coadds2", "fowler4_coadds1", "fowler8_coadds1", "fowler16_coadds1", "fowler1_coadds1"]
    rotator_mode: Literal["SKY"]
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
    guiding_config: LcoSoarTriplespecGuidingConfig | None = None
    acquisition_config: LcoSoarTriplespecAcquisitionConfig | None = None


class LcoSoarGhtsBluecamGuidingConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["ON"]
    optional: bool
    """Whether the guiding is optional or not"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}


class LcoSoarGhtsBluecamAcquisitionConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["MANUAL"]
    exposure_time: Annotated[int, NonNegativeInt, Le(60)] = 60
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class LcoSoarGhtsBluecamConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds"""
    mode: Literal["GHTS_B_400m1_2x2"]
    rotator_mode: Literal["SKY"]
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
    guiding_config: LcoSoarGhtsBluecamGuidingConfig | None = None
    acquisition_config: LcoSoarGhtsBluecamAcquisitionConfig | None = None


class Lco1M0ScicamSinistroGuidingConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["OFF", "ON"]
    optional: bool
    """Whether the guiding is optional or not"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}


class Lco1M0ScicamSinistroAcquisitionConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["OFF"]
    exposure_time: Annotated[int, NonNegativeInt, Le(60)] = 60
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class Lco1M0ScicamSinistroConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds"""
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
    guiding_config: Lco1M0ScicamSinistroGuidingConfig | None = None
    acquisition_config: Lco1M0ScicamSinistroAcquisitionConfig | None = None


class Lco0M4ScicamQhy600GuidingConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["OFF", "ON"]
    optional: bool
    """Whether the guiding is optional or not"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}


class Lco0M4ScicamQhy600AcquisitionConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["OFF"]
    exposure_time: Annotated[int, NonNegativeInt, Le(60)] = 60
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class Lco0M4ScicamQhy600Config(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds"""
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
    guiding_config: Lco0M4ScicamQhy600GuidingConfig | None = None
    acquisition_config: Lco0M4ScicamQhy600AcquisitionConfig | None = None


class LcoBlancoNewfirmGuidingConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["ON"]
    optional: bool
    """Whether the guiding is optional or not"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}


class LcoBlancoNewfirmAcquisitionConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    mode: Literal["MANUAL"]
    exposure_time: Annotated[int, NonNegativeInt, Le(60)] = 60
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class LcoBlancoNewfirmConfig(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds"""
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
    guiding_config: LcoBlancoNewfirmGuidingConfig | None = None
    acquisition_config: LcoBlancoNewfirmAcquisitionConfig | None = None


# Export a type that encompasses all instruments
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