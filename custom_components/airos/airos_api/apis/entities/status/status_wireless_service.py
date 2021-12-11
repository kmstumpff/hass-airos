class StatusWirelessService:
    time: int
    link: int
    _5: int
    _60: int

    def __init__(self, data):
        self.time = data.get("time")
        self.link = data.get("link")
        self._5 = data.get("5")
        self._60 = data.get("60")
