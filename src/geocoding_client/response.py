from __future__ import annotations

from enum import Enum
from typing import TypedDict, List

class Location(TypedDict):
    lat: str
    lon: str

class LocationType(Enum):
    ROOFTOP = "ROOFTOP"
    RANGE_INTERPOLATED = "RANGE_INTERPOLATED"
    GEOMETRIC_CENTER = "GEOMETRIC_CENTER"
    APPROXIMATE = "APPROXIMATE"

class Viewport(TypedDict):
    southwest: Location
    northeast: Location

class Geometry(TypedDict):
    location: Location
    location_type: LocationType
    viewport: Viewport

class Result(TypedDict):
    geometry: Geometry
    types: List[str]

class Status(Enum):
    OK = "OK"
    ZERO_RESULTS = "ZERO_RESULTS"
    OVER_DAILY_LIMIT = "OVER_DAILY_LIMIT"
    OVER_QUERY_LIMIT = "OVER_QUERY_LIMIT"
    REQUEST_DENIED = "REQUEST_DENIED"
    INVALID_REQUEST = "INVALID_REQUEST"
    UNKNOWN_ERROR = "UNKNOWN_ERROR"

class Response(TypedDict):
    error_message: NotRequired[str]
    results: List[Result]
    status: Status