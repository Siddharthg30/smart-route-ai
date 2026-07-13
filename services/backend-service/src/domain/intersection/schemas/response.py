from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from core.enums.intersection import (
    IntersectionStatus,
    OperatingMode,
)


class IntersectionResponse(BaseModel):
    id: UUID

    name: str
    city: str

    latitude: float
    longitude: float

    status: IntersectionStatus
    operating_mode: OperatingMode

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )


class IntersectionListResponse(BaseModel):
    items: list[IntersectionResponse]
    total: int