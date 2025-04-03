from datetime import datetime
from typing import Annotated, Any, Literal

from annotated_types import Ge, Le
from pydantic import BaseModel, ConfigDict
from pydantic.types import (
    NonNegativeFloat,
    NonNegativeInt,
    PositiveFloat,
    PositiveInt,
    StringConstraints,
)


class OCSModel(BaseModel):
    model_config = ConfigDict(validate_assignment=True)


class Roi(OCSModel):
    """Region of Interest"""

    x1: NonNegativeInt | None = None
    x2: NonNegativeInt | None = None
    y1: NonNegativeInt | None = None
    y2: NonNegativeInt | None = None


class InstrumentConfig(OCSModel):
    """Instrument configuration"""

    exposure_count: PositiveInt
    """The number of exposures to take. This field must be set to a value greater than 0"""
    exposure_time: NonNegativeInt
    """ Exposure time in seconds (TODO: can this really be 0?)"""
    mode: Annotated[str, StringConstraints(max_length=50)]
    """ TODO this is dynamic per instrument"""
    rotator_mode: Annotated[str, StringConstraints(max_length=50)] | None = None
    """
    (Spectrograph only) How the slit is positioned on the sky.
    If set to VFLOAT, atmospheric dispersion is along the slit.
    """
    extra_params: dict[Any, Any] = {}
    """This is completely generated at runtime via configdb stuff"""
    optical_elements: dict[Any, Any] | None = None
    """Specification of optical elements used for this InstrumentConfig"""
    rois: list[Roi] | None = None


class Constraints(OCSModel):
    max_airmass: Annotated[float, PositiveFloat, Le(25.0)] = 1.6
    max_lunar_distance: Annotated[float, NonNegativeFloat, Le(180.0)] = 30.00
    max_lunar_phase: Annotated[float, PositiveFloat, Le(1.0)] = 1.0
    max_seeing: NonNegativeFloat | None = 0.0
    """Maximum acceptable seeing"""
    min_transparency: float | None = 0.0
    """Minimum acceptable transparency"""
    extra_params: dict[Any, Any] = {}


class AcquisitionConfig(OCSModel):
    mode: Annotated[str, StringConstraints(max_length=50)]
    """AcquisitionConfig mode to use for the observations"""
    exposure_time: Annotated[int, NonNegativeInt, Le(60)]
    """Acquisition exposure time"""
    extra_params: dict[Any, Any] = {}


class GuidingConfig(OCSModel):
    optional: bool
    """Whether the guiding is optional or not"""
    mode: Annotated[str, StringConstraints(max_length=50)]
    """Guiding mode to use for the observations"""
    optical_elements: dict[Any, Any] | None = None
    """Optical Element specification for this GuidingConfig"""
    exposure_time: Annotated[int, NonNegativeInt, Le(120)] = 120
    """Guiding exposure time"""
    extra_params: dict[Any, Any] = {}


class Target(OCSModel):
    name: Annotated[str, StringConstraints(max_length=50)] = "string"
    """The name of this Target"""
    type: Literal["ICRS", "ORBITAL_ELEMENTS", "HOUR_ANGLE", "SATELLITE"]
    """The type of this Target"""
    hour_angle: float | None = None
    """Hour angle of this Target"""
    ra: Annotated[int, NonNegativeFloat, Le(360.0)] | None = None
    """Right ascension in decimal degrees"""
    dec: Annotated[float, Ge(-90), Le(90)] | None = None
    """Declination in decimal degrees"""
    altitude: Annotated[float, NonNegativeFloat, Le(90)] | None = None
    """Altitude of this Target"""
    azimuth: Annotated[float, NonNegativeFloat, Le(360)] | None = None
    """Azimuth of this Target"""
    proper_motion_ra: Annotated[float, Le(20000.0)] = 0
    """Right ascension proper motion of the Target +/-33 mas/year. Defaults to 0."""
    proper_motion_dec: Annotated[float, Le(20000.0)] = 0
    """Declination proper motion of the Target +/-33 mas/year. Defaults to 0."""
    epoch: Annotated[int, Le(2100)] = 2000
    """Epoch in Modified Julian Days (MJD). Defaults to 2000."""
    parallax: Annotated[int, Le(2000)] = 0
    """Parallax of the Target ±0.45 mas, max 2000. Defaults to 0."""
    diff_altitude_rate: int | None = None
    """Differential altitude rate (arcsec/s)"""
    diff_azimuth_rate: int | None = None
    """Differential azimuth rate (arcsec/s)"""
    diff_epoch: int | None = None
    """Reference time for non-sidereal motion (MJD)"""
    diff_altitude_acceleration: int | None = None
    """Differential altitude acceleration (arcsec/s^2)"""
    diff_azimuth_acceleration: int | None = None
    """Differential azimuth acceleration (arcsec/s^2)"""
    scheme: (
        Literal[
            "ASA_MAJOR_PLANET",
            "ASA_MINOR_PLANET",
            "ASA_COMET",
            "JPL_MAJOR_PLANET",
            "JPL_MINOR_PLANET",
            "MPC_MINOR_PLANET",
            "MPC_COMET",
        ]
        | None
    ) = None
    """The Target scheme to use"""
    epochofel: Annotated[int, Ge(10_000), Le(100_000)] | None = None
    """The epoch of the orbital elements (MJD)"""
    orbinc: Annotated[int, NonNegativeFloat, Le(180.0)] | None = None
    """Orbital inclination (angle in degrees)"""
    longascnode: Annotated[int, NonNegativeFloat, Le(360.0)] | None = None
    """Longitude of ascending node (angle in degrees)"""
    longofperih: Annotated[int, NonNegativeFloat, Le(360.0)] | None = None
    """Longitude of perihelion (angle in degrees)"""
    argofperih: Annotated[int, NonNegativeFloat, Le(360.0)] | None = None
    """Argument of perihelion (angle in degrees)"""
    meandist: float | None = None
    """Mean distance (AU)"""
    perihdist: float | None = None
    """Perihelion distance (AU)"""
    eccentricity: NonNegativeFloat | None = None
    """Eccentricity of the orbit"""
    meanlong: float | None = None
    """Mean longitude (angle in degrees)"""
    meananom: Annotated[float, NonNegativeFloat, Le(360.0)] | None = None
    """Mean anomaly (angle in degrees)"""
    dailymot: float | None = None
    """Daily motion (angle in degrees)"""
    epochofperih: Annotated[float, Ge(361), Le(240_000), Le(100_000)] | None = None
    """Epoch of perihelion (MJD)"""
    extra_params: dict[Any, Any] = {}


class Configuration(OCSModel):
    """Request level configuration"""

    fill_window: bool = True
    type: Literal[
        "EXPOSE",
        "REPEAT_EXPOSE",
        "SKY_FLAT",
        "STANDARD",
        "ARC",
        "LAMP_FLAT",
        "SPECTRUM",
        "REPEAT_SPECTRUM",
        "AUTO_FOCUS",
        "TRIPLE",
        "NRES_TEST",
        "NRES_SPECTRUM",
        "REPEAT_NRES_SPECTRUM",
        "NRES_EXPOSE",
        "NRES_DARK",
        "NRES_BIAS",
        "ENGINEERING",
        "SCRIPT",
        "BIAS",
        "DARK",
    ]
    instrument_type: Annotated[str, StringConstraints(max_length=255)]
    """The instrument type used for the observations under this Configuration"""
    repeat_duration: NonNegativeInt = 0
    """
    The requested duration for this configuration to be repeated within. Only applicable to
    REPEAT_* type configurations. Setting parameter fill_window to True will cause
    this value to automatically be filled in to the max possible given its visibility within
    the observing window.
    """
    extra_params: dict[Any, Any] = {}
    """Non-standard configuration that will be passed to the instrument"""
    instrument_configs: list[InstrumentConfig]
    """ Standard configuration that will be passed to the instrument"""
    constraints: Constraints | None = None
    acquisition_config: AcquisitionConfig | None = None
    guiding_config: GuidingConfig | None = None
    target: Target | None = None


class Location(OCSModel):
    """
    Location constraints for this request.
    TODO: Seems the OpenAPI spec does not specify values.
    """

    site: str | None = None
    enclosure: str | None = None
    telescope: str | None = None
    telescope_class: str


class Window(OCSModel):
    """Request level window configuration"""

    start: datetime | None = None
    end: datetime
    """The time when this observing Window ends"""


class Cadence(OCSModel):
    """Request level cadence configuration"""

    start: datetime
    end: datetime
    period: Annotated[float, Ge(0.02)]
    jitter: Annotated[float, Ge(0.02)]


class Request(OCSModel):
    """A request for a single, discrete observation. One group can contain multiple
    requests"""

    acceptability_threshold: Annotated[int, NonNegativeInt, Le(100)] = 90
    """
    The percentage of the observation that must be completed to mark the request as
    complete and avert rescheduling. The percentage should be set to the lowest value
    for which the amount of data is acceptable to meet the science goal of the request.
    """
    configuration_repeats: PositiveInt = 1
    """
    The number of times this Request's set of Configurations should be repeated.
    This is useful for nodding back and forth between a set of Targets that are too
    far apart to use Dithering.
    """
    optimization_type: Literal["TIME", "AIRMASS"] | None = None
    """
    Optimization to use when scheduling. TIME favors placing requests earlier in their
    window. AIRMASS favors placing requests at lower airmass (higher altitude).
    """
    observation_note: Annotated[str, StringConstraints(max_length=255)] = ""
    """Text describing this Request"""
    extra_params: dict[Any, Any] = {}
    configurations: list[Configuration]
    cadence: Cadence | None = None
    windows: list[Window]
    location: Location


class RequestGroup(OCSModel):
    """
    An Observation request for any observatory that supports an OCS API.
    """

    proposal: str
    """The proposal ID awarded time"""
    ipp_value: NonNegativeFloat
    """A multiplier to the base priority of the Proposal for this RequestGroup
    and all child Requests. A value > 1.0 will raise the priority and debit the Proposal
    ipp_time_available upon submission. If a Request does not complete, the time debited
    for that Request is returned. A value < 1.0 will lower the priority and credit the
    ipp_time_available of the Proposal up to the ipp_limit on the successful completion
    of a Request. The value is generally set to 1.05.
    """
    operator: Literal["SINGLE", "MANY"]
    """Operator that describes how child Requests are scheduled.
    Use SINGLE if you have only one Request and MANY if you have more than one.
    """
    observation_type: Literal["NORMAL", "RAPID_RESPONSE", "TIME_CRITICAL", "DIRECT"]
    """The type of observations under this RequestGroup. Requests submitted with
    RAPID_RESPONSE bypass normal scheduling and are executed immediately.
    Requests submitted with TIME_CRITICAL are scheduled normally but with a high priority.
    These modes are only available if the Proposal was granted special time.
    """
    submitter_id: str = ""
    name: Annotated[str, StringConstraints(max_length=50)]
    """
    Descriptive name for this RequestGroup. This string will be placed in the
    FITS header as the GROUPID keyword value for all FITS frames originating from this
    RequestGroup.
    """
    requests: list[Request] = []
