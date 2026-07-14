from sqlalchemy import Float, String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from core.database.models.base_entity import BaseEntity
from core.enums.intersection import (
    IntersectionStatus,
    OperatingMode,
)


class Intersection(BaseEntity):
    """
    Represents a physical traffic intersection.
    """

    __tablename__ = "intersections"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True,
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    longitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    status: Mapped[IntersectionStatus] = mapped_column(
        Enum(IntersectionStatus),
        default=IntersectionStatus.ACTIVE,
        nullable=False,
        index=True,
    )

    operating_mode: Mapped[OperatingMode] = mapped_column(
        Enum(OperatingMode),
        default=OperatingMode.EDGE_AI,
        nullable=False,
    )