class StatusWirelessStaPrsStaStats:
    tx_packets: int
    rx_packets: int
    tx_bytes: int
    rx_bytes: int
    tx_errors: int
    rx_errors: int

    def __init__(self, data):
        self.tx_packets = data.get("tx_packets")
        self.rx_packets = data.get("rx_packets")
        self.tx_bytes = data.get("tx_bytes")
        self.rx_bytes = data.get("rx_bytes")
        self.tx_errors = data.get("tx_errors")
        self.rx_errors = data.get("rx_errors")
