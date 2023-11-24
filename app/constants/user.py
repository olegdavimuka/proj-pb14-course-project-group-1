from enum import Enum


class UserStatus(Enum, str):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    PAUSED = "PAUSED"
