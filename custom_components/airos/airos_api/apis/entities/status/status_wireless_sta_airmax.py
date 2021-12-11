class StatusWirelessStaAirmax:
    downlink_capacity: int
    uplink_capacity: int

    def __init__(self, data):
        self.downlink_capacity = data.get("downlink_capacity")
        self.uplink_capacity = data.get("uplink_capacity")
