class StatusInterfacesStatusPersistentStats:
    tx_packets: int
    rx_packets: int
    tx_errors: int
    rx_errors: int
    tx_dropped: int
    rx_dropped: int

    def __init__(self, data):
        self.tx_packets = data.get("tx_packets")
        self.rx_packets = data.get("rx_packets")
        self.tx_errors = data.get("tx_errors")
        self.rx_errors = data.get("rx_errors")
        self.tx_dropped = data.get("tx_dropped")
        self.rx_dropped = data.get("rx_dropped")
