from pydantic import BaseModel, ConfigDict, Field

from core.enums.intersection import (
    IntersectionStatus,
    OperatingMode,
)


class IntersectionCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
    )

    city: str = Field(
        min_length=2,
        max_length=100,
    )

    latitude: float = Field(
        ge=-90,
        le=90,
    )

    longitude: float = Field(
        ge=-180,
        le=180,
    )

    status: IntersectionStatus = IntersectionStatus.ACTIVE
    operating_mode: OperatingMode = OperatingMode.EDGE_AI

    model_config = ConfigDict(
        extra="forbid",
    )


class IntersectionUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    city: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    latitude: float | None = Field(
        default=None,
        ge=-90,
        le=90,
    )

    longitude: float | None = Field(
        default=None,
        ge=-180,
        le=180,
    )

    status: IntersectionStatus | None = None
    operating_mode: OperatingMode | None = None

    model_config = ConfigDict(
        extra="forbid",
    )