from . import StatusInterfacesStatusPersistentStats


class StatusInterfacesStatus:
    plugged: bool
    tx_bytes: int
    rx_bytes: int
    tx_packets: int
    rx_packets: int
    tx_errors: int
    rx_errors: int
    tx_dropped: int
    rx_dropped: int
    ipaddr: str
    speed: int
    duplex: bool
    cable_len: int
    persistent_stats: StatusInterfacesStatusPersistentStats

    def __init__(self, data):
        self.plugged = data.get("plugged")
        self.tx_bytes = data.get("tx_bytes")
        self.rx_bytes = data.get("rx_bytes")
        self.tx_packets = data.get("tx_packets")
        self.rx_packets = data.get("rx_packets")
        self.tx_errors = data.get("tx_errors")
        self.rx_errors = data.get("rx_errors")
        self.tx_dropped = data.get("tx_dropped")
        self.rx_dropped = data.get("rx_dropped")
        self.ipaddr = data.get("ipaddr")
        self.speed = data.get("speed")
        self.duplex = data.get("duplex")
        self.cable_len = data.get("cable_len")
        self.persistent_stats = StatusInterfacesStatusPersistentStats(
            data.get("persistent_stats", {})
        )
