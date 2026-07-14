from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum
from src.core.database.models.base_entity import BaseEntity
from src.core.enums.intersection import (
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
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
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
    )

    operating_mode: Mapped[OperatingMode] = mapped_column(
        Enum(OperatingMode),
        default=OperatingMode.EDGE_AI,
        nullable=False,
    )