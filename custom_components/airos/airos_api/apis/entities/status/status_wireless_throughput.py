class StatusWirelessThroughput:
    tx: int
    rx: int

    def __init__(self, data):
        self.tx = data.get("tx")
        self.rx = data.get("rx")
