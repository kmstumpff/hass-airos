class StatusHost:
    hostname: str
    device_id: str
    uptime: int
    power_time: int
    time: str
    timestamp: int
    fwversion: str
    devmodel: str
    netrole: str
    loadavg: float
    totalram: int
    freeram: int
    temperature: int
    cpuload: float
    height: int

    def __init__(self, data):
        self.hostname = data.get("hostname")
        self.device_id = data.get("device_id")
        self.uptime = data.get("uptime")
        self.power_time = data.get("power_time")
        self.time = data.get("time")
        self.timestamp = data.get("timestamp")
        self.fwversion = data.get("fwversion")
        self.devmodel = data.get("devmodel")
        self.netrole = data.get("netrole")
        self.loadavg = data.get("loadavg")
        self.totalram = data.get("totalram")
        self.freeram = data.get("freeram")
        self.temperature = data.get("temperature")
        self.cpuload = data.get("cpuload")
        self.height = data.get("height")
