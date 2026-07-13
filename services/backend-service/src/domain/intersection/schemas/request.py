from pydantic import BaseModel, ConfigDict

from core.enums.intersection import (
    IntersectionStatus,
    OperatingMode,
)


class IntersectionCreate(BaseModel):
    name: str
    city: str
    latitude: float
    longitude: float

    status: IntersectionStatus = IntersectionStatus.ACTIVE
    operating_mode: OperatingMode = OperatingMode.EDGE_AI

    model_config = ConfigDict(
        extra="forbid",
    )


class IntersectionUpdate(BaseModel):
    name: str | None = None
    city: str | None = None
    latitude: float | None = None
    longitude: float | None = None

    status: IntersectionStatus | None = None
    operating_mode: OperatingMode | None = None

    model_config = ConfigDict(
        extra="forbid",
    )