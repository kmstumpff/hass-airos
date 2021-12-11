from enum import Enum

class Intervals(str, Enum):
    HOUR = "hour"
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    YEAR = "year"