class StatusWirelessPrsInfo:
    chanbw: int
    frequency: int
    sta_count: int

    def __init__(self, data):
        self.chanbw = data.get("chanbw")
        self.frequency = data.get("frequency")
        self.sta_count = data.get("sta_count")
