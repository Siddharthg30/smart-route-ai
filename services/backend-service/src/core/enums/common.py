from enum import StrEnum


class Status(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class HealthStatus(StrEnum):
    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    UNHEALTHY = "UNHEALTHY"