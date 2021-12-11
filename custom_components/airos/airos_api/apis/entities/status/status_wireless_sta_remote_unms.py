class StatusWirelessStaRemoteUnms:
    status: int
    timestamp: str

    def __init__(self, data):
        self.status = data.get("status")
        self.timestamp = data.get("timestamp")
