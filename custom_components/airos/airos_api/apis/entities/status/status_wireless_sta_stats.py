class StatusWirelessStaStats:
    rx_bytes: int
    rx_packets: int
    rx_pps: int
    tx_bytes: int
    tx_packets: int
    tx_pps: int

    def __init__(self, data):
        self.rx_bytes = data.get("rx_bytes")
        self.rx_packets = data.get("rx_packets")
        self.rx_pps = data.get("rx_pps")
        self.tx_bytes = data.get("tx_bytes")
        self.tx_packets = data.get("tx_packets")
        self.tx_pps = data.get("tx_pps")
