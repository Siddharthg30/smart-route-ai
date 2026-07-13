from enum import StrEnum


class IntersectionStatus(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    MAINTENANCE = "MAINTENANCE"


class OperatingMode(StrEnum):
    EDGE_AI = "EDGE_AI"
    SERVER_AI = "SERVER_AI"
    TIME_BASED = "TIME_BASED"
    MANUAL = "MANUAL"