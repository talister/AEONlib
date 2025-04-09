from typing import Annotated, Any, Literal

from annotated_types import Ge, Le
from pydantic import BaseModel, ConfigDict
from pydantic.types import (
    NonNegativeFloat,
    PositiveFloat,
    StringConstraints,
)


class SiderealTarget(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    name: Annotated[str, StringConstraints(max_length=50)] = "string"
    """The name of this Target"""
    type: Literal["ICRS", "HOUR_ANGLE"]
    """The type of this Target"""
    hour_angle: float | None = None
    """Hour angle of this Target"""
    ra: Annotated[float, NonNegativeFloat, Le(360.0)]
    """Right ascension in decimal degrees"""
    dec: Annotated[float, Ge(-90), Le(90)]
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
    dailymot: float | None = None
    """Daily motion (angle in degrees)"""


class NonSiderealTarget(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    name: Annotated[str, StringConstraints(max_length=50)] = "string"
    """Parallax of the Target ±0.45 mas, max 2000. Defaults to 0."""
    type: Literal["ORBITAL_ELEMENTS", "HOUR_ANGLE", "SATELLITE"]
    """The type of this Target TODO: Where does HOUR_ANGLE make sense?"""
    scheme: Literal[
        "ASA_MAJOR_PLANET",
        "ASA_MINOR_PLANET",
        "ASA_COMET",
        "JPL_MAJOR_PLANET",
        "JPL_MINOR_PLANET",
        "MPC_MINOR_PLANET",
        "MPC_COMET",
    ]
    """The Target scheme to use"""
    epochofel: Annotated[int, Ge(10_000), Le(100_000)]
    """The epoch of the orbital elements (MJD)"""
    orbinc: Annotated[int, NonNegativeFloat, Le(180.0)]
    """Orbital inclination (angle in degrees)"""
    longascnode: Annotated[int, NonNegativeFloat, Le(360.0)]
    """Longitude of ascending node (angle in degrees)"""
    longofperih: Annotated[int, NonNegativeFloat, Le(360.0)] | None = None
    """Longitude of perihelion (angle in degrees)"""
    argofperih: Annotated[int, NonNegativeFloat, Le(360.0)]
    """Argument of perihelion (angle in degrees)"""
    meandist: float
    """Mean distance (AU)"""
    perihdist: float | None = None
    """Perihelion distance (AU)"""
    eccentricity: NonNegativeFloat
    """Eccentricity of the orbit"""
    meanlong: float | None = None
    """Mean longitude (angle in degrees)"""
    meananom: Annotated[float, NonNegativeFloat, Le(360.0)]
    """Mean anomaly (angle in degrees)"""
    dailymot: float | None = None
    """Daily motion (angle in degrees)"""
    epochofperih: Annotated[float, Ge(361), Le(240_000), Le(100_000)] | None = None
    """Epoch of perihelion (MJD)"""
    extra_params: dict[Any, Any] = {}


class Constraints(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    max_airmass: Annotated[float, PositiveFloat, Le(25.0)] = 1.6
    max_lunar_distance: Annotated[float, NonNegativeFloat, Le(180.0)] = 30.00
    max_lunar_phase: Annotated[float, PositiveFloat, Le(1.0)] = 1.0
    max_seeing: NonNegativeFloat | None = None
    """Maximum acceptable seeing"""
    min_transparency: float | None = None
    """Minimum acceptable transparency"""
    extra_params: dict[Any, Any] = {}
