from typing import List

from . import (
    StatusWirelessPolling,
    StatusWirelessPrsInfo,
    StatusWirelessService,
    StatusWirelessThroughput,
    StatusWirelessSta,
)


class StatusWireless:
    essid: str
    mode: str
    apmac: str
    security: str
    throughput: StatusWirelessThroughput
    ieeemode: str
    compat_11n: int
    hide_essid: int
    antenna_gain: int
    frequency: int
    center1_freq: int
    dfs: int
    distance: float
    noisef: int
    txpower: int
    aprepeater: bool
    rstatus: int
    chanbw: int
    rx_chainmask: int
    tx_chainmask: int
    cac_state: int
    cac_timeout: int
    rx_idx: int
    rx_nss: int
    tx_idx: int
    tx_nss: int
    service: StatusWirelessService
    count: int
    prs_info: StatusWirelessPrsInfo
    polling: StatusWirelessPolling
    sta: List[StatusWirelessSta]

    def __init__(self, data):
        self.essid = data.get("essid")
        self.mode = data.get("mode")
        self.apmac = data.get("apmac")
        self.security = data.get("security")
        self.throughput = StatusWirelessThroughput(data.get("throughput", {}))
        self.ieeemode = data.get("ieeemode")
        self.compat_11n = data.get("compat_11n")
        self.hide_essid = data.get("hide_essid")
        self.antenna_gain = data.get("antenna_gain")
        self.frequency = data.get("frequency")
        self.center1_freq = data.get("center1_freq")
        self.dfs = data.get("dfs")
        self.distance = data.get("distance")
        self.noisef = data.get("noisef")
        self.txpower = data.get("txpower")
        self.aprepeater = data.get("aprepeater")
        self.rstatus = data.get("rstatus")
        self.chanbw = data.get("chanbw")
        self.rx_chainmask = data.get("rx_chainmask")
        self.tx_chainmask = data.get("tx_chainmask")
        self.cac_state = data.get("cac_state")
        self.cac_timeout = data.get("cac_timeout")
        self.rx_idx = data.get("rx_idx")
        self.rx_nss = data.get("rx_nss")
        self.tx_idx = data.get("tx_idx")
        self.tx_nss = data.get("tx_nss")
        self.service = StatusWirelessService(data.get("service", {}))
        self.count = data.get("count")
        self.prs_info = StatusWirelessPrsInfo(data.get("prs_info", {}))
        self.polling = StatusWirelessPolling(data.get("polling", {}))
        self.sta = [StatusWirelessSta(row) for row in data.get("sta", [])]
