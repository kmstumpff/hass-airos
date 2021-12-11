from . import StatusWirelessStaPrsStaStats


class StatusWirelessStaPrsSta:
    rssi_data: int
    snr: int
    capacity: int
    tx_mcs: int
    rx_mcs: int
    stats: StatusWirelessStaPrsStaStats
    tx_sector: int
    rx_sector: int
    distance: float
    uptime: int
    dl_signal_expect: int
    ul_signal_expect: int
    dl_capacity_expect: int
    ul_capacity_expect: int
    dl_rate_expect: int
    ul_rate_expect: int
    dl_linkscore: int
    ul_linkscore: int
    dl_avg_linkscore: int
    ul_avg_linkscore: int

    def __init__(self, data):
        self.rssi_data = data.get("rssi_data")
        self.snr = data.get("snr")
        self.capacity = data.get("capacity")
        self.tx_mcs = data.get("tx_mcs")
        self.rx_mcs = data.get("rx_mcs")
        self.stats = StatusWirelessStaPrsStaStats(data.get("stats", {}))
        self.tx_sector = data.get("tx_sector")
        self.rx_sector = data.get("rx_sector")
        self.distance = data.get("distance")
        self.uptime = data.get("uptime")
        self.dl_signal_expect = data.get("dl_signal_expect")
        self.ul_signal_expect = data.get("ul_signal_expect")
        self.dl_capacity_expect = data.get("dl_capacity_expect")
        self.ul_capacity_expect = data.get("ul_capacity_expect")
        self.dl_rate_expect = data.get("dl_rate_expect")
        self.ul_rate_expect = data.get("ul_rate_expect")
        self.dl_linkscore = data.get("dl_linkscore")
        self.ul_linkscore = data.get("ul_linkscore")
        self.dl_avg_linkscore = data.get("dl_avg_linkscore")
        self.ul_avg_linkscore = data.get("ul_avg_linkscore")
