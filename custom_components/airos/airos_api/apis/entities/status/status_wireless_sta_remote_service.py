class StatusWirelessStaRemoteService:
    time: int
    link: int
    _5: int
    _6g: int

    def __init__(self, data):
        self.time = data.get("time")
        self.link = data.get("link")
        self._5 = data.get("5")
        self._6g = data.get("6g")
