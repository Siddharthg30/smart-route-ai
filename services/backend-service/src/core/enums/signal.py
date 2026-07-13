from enum import StrEnum


class SignalState(StrEnum):
    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"


class SignalDirection(StrEnum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"