class StatusWirelessStaRemoteEthlist:
    ifname: str
    enabled: bool
    plugged: bool
    duplex: bool
    speed: int
    cable_len: int

    def __init__(self, data):
        self.ifname = data.get("ifname")
        self.enabled = data.get("enabled")
        self.plugged = data.get("plugged")
        self.duplex = data.get("duplex")
        self.speed = data.get("speed")
        self.cable_len = data.get("cable_len")
