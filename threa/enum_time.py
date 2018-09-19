from enum import Enum


class TimeUnits(Enum):
    H = 0
    M = 1
    S = 2

    def converse_time(t, maxtime):
        if t == TimeUnits.H:
            return maxtime * 60 * 60
        elif t == TimeUnits.M:
            return maxtime * 60
