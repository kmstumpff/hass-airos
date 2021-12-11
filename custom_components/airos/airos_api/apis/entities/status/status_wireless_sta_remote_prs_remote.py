class StatusWirelessStaRemotePrsRemote:
    rssi_data: int
    snr: int
    capacity: int
    antenna_gain: int
    tx_maxpower: int
    tx_mcs: int
    tx_bytes: int
    rx_bytes: int
    tx_sector: int
    rx_sector: int
    distance: float
    wave_ai: int

    def __init__(self, data):
        self.rssi_data = data.get("rssi_data")
        self.snr = data.get("snr")
        self.capacity = data.get("capacity")
        self.antenna_gain = data.get("antenna_gain")
        self.tx_maxpower = data.get("tx_maxpower")
        self.tx_mcs = data.get("tx_mcs")
        self.tx_bytes = data.get("tx_bytes")
        self.rx_bytes = data.get("rx_bytes")
        self.tx_sector = data.get("tx_sector")
        self.rx_sector = data.get("rx_sector")
        self.distance = data.get("distance")
        self.wave_ai = data.get("wave_ai")
