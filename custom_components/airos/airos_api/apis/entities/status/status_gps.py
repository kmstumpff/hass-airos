class StatusGps:
    lat: float
    lon: float
    fix: int
    sats: int
    dim: int
    dop: float
    alt: float
    time_sync_enabled: int

    def __init__(self, data):
        self.lat = data.get("lat")
        self.lon = data.get("lon")
        self.fix = data.get("fix")
        self.sats = data.get("sats")
        self.dim = data.get("dim")
        self.dop = data.get("dop")
        self.alt = data.get("alt")
        self.time_sync_enabled = data.get("time_sync_enabled")
