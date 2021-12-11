from . import (
    StatusWirelessStaAirmax,
    StatusWirelessStaPrsSta,
    StatusWirelessStaRemote,
    StatusWirelessStaStats,
)


class StatusWirelessSta:
    mac: str
    linked_5: bool
    linked_60: bool
    lastip: str
    signal: int
    rssi: int
    noisefloor: int
    tx_idx: int
    rx_idx: int
    tx_nss: int
    rx_nss: int
    tx_latency: int
    distance: float
    tx_packets: int
    tx_lretries: int
    tx_sretries: int
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
    stats: StatusWirelessStaStats
    airmax: StatusWirelessStaAirmax
    prs_sta: StatusWirelessStaPrsSta
    debug_dist_zero_count: int
    debug_dist_local: int
    debug_dist_local_avg: int
    debug_dist_local_min: int
    debug_dist_local_max: int
    debug_dist_remote: int
    debug_dist_remote_avg: int
    debug_dist_remote_min: int
    debug_dist_remote_max: int
    debug_dist_prs_remote: int
    debug_dist_prs_remote_avg: int
    debug_dist_prs_remote_min: int
    debug_dist_prs_remote_max: int
    ubond_active: str
    remote: StatusWirelessStaRemote

    def __init__(self, data):
        self.mac = data.get("mac")
        self.linked_5 = data.get("linked_5")
        self.linked_60 = data.get("linked_60")
        self.lastip = data.get("lastip")
        self.signal = data.get("signal")
        self.rssi = data.get("rssi")
        self.noisefloor = data.get("noisefloor")
        self.tx_idx = data.get("tx_idx")
        self.rx_idx = data.get("rx_idx")
        self.tx_nss = data.get("tx_nss")
        self.rx_nss = data.get("rx_nss")
        self.tx_latency = data.get("tx_latency")
        self.distance = data.get("distance")
        self.tx_packets = data.get("tx_packets")
        self.tx_lretries = data.get("tx_lretries")
        self.tx_sretries = data.get("tx_sretries")
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
        self.stats = StatusWirelessStaStats(data.get("stats", {}))
        self.airmax = StatusWirelessStaAirmax(data.get("airmax", {}))
        self.prs_sta = StatusWirelessStaPrsSta(data.get("prs_sta", {}))
        self.debug_dist_zero_count = data.get("debug_dist_zero_count")
        self.debug_dist_local = data.get("debug_dist_local")
        self.debug_dist_local_avg = data.get("debug_dist_local_avg")
        self.debug_dist_local_min = data.get("debug_dist_local_min")
        self.debug_dist_local_max = data.get("debug_dist_local_max")
        self.debug_dist_remote = data.get("debug_dist_remote")
        self.debug_dist_remote_avg = data.get("debug_dist_remote_avg")
        self.debug_dist_remote_min = data.get("debug_dist_remote_min")
        self.debug_dist_remote_max = data.get("debug_dist_remote_max")
        self.debug_dist_prs_remote = data.get("debug_dist_prs_remote")
        self.debug_dist_prs_remote_avg = data.get("debug_dist_prs_remote_avg")
        self.debug_dist_prs_remote_min = data.get("debug_dist_prs_remote_min")
        self.debug_dist_prs_remote_max = data.get("debug_dist_prs_remote_max")
        self.ubond_active = data.get("ubond_active")
        self.remote = StatusWirelessStaRemote(data.get("remote", {}))
