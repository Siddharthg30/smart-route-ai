from enum import StrEnum


class DecisionSource(StrEnum):
    EDGE_AI = "EDGE_AI"
    SERVER_AI = "SERVER_AI"
    TIME_BASED = "TIME_BASED"


class AIModelStatus(StrEnum):
    LOADED = "LOADED"
    UNLOADED = "UNLOADED"
    FAILED = "FAILED"