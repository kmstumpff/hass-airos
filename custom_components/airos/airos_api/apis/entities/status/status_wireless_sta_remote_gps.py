class StatusWirelessStaRemoteGps:
    lat: str
    lon: str
    fix: int
    sats: int
    dim: int
    dop: str
    alt: str
    time_synced: int

    def __init__(self, data):
        self.lat = data.get("lat")
        self.lon = data.get("lon")
        self.fix = data.get("fix")
        self.sats = data.get("sats")
        self.dim = data.get("dim")
        self.dop = data.get("dop")
        self.alt = data.get("alt")
        self.time_synced = data.get("time_synced")
