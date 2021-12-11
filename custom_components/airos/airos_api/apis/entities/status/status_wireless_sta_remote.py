from typing import List

from . import (
    StatusWirelessStaRemoteGps,
    StatusWirelessStaRemotePrsRemote,
    StatusWirelessStaRemoteService,
    StatusWirelessStaRemoteUnms,
)
from .status_wireless_sta_remote_ethlist import StatusWirelessStaRemoteEthlist


class StatusWirelessStaRemote:
    device_id: str
    hostname: str
    platform: str
    version: str
    time: str
    cpuload: float
    temperature: int
    totalram: int
    freeram: int
    netrole: str
    mode: str
    sys_id: str
    tx_throughput: int
    rx_throughput: int
    uptime: int
    power_time: int
    compat_11n: int
    signal: int
    rssi: int
    noisefloor: int
    tx_power: int
    distance: float
    rx_chainmask: int
    tx_bytes: int
    rx_bytes: int
    antenna_gain: int
    cable_loss: int
    height: int
    ethlist: List[StatusWirelessStaRemoteEthlist]
    gps: StatusWirelessStaRemoteGps
    https_port: int
    oob: bool
    unms: StatusWirelessStaRemoteUnms
    airview: int
    service: StatusWirelessStaRemoteService
    prs_remote: StatusWirelessStaRemotePrsRemote
    ubond_active: str

    def __init__(self, data):
        self.device_id = data.get("device_id")
        self.hostname = data.get("hostname")
        self.platform = data.get("platform")
        self.version = data.get("version")
        self.time = data.get("time")
        self.cpuload = data.get("cpuload")
        self.temperature = data.get("temperature")
        self.totalram = data.get("totalram")
        self.freeram = data.get("freeram")
        self.netrole = data.get("netrole")
        self.mode = data.get("mode")
        self.sys_id = data.get("sys_id")
        self.tx_throughput = data.get("tx_throughput")
        self.rx_throughput = data.get("rx_throughput")
        self.uptime = data.get("uptime")
        self.power_time = data.get("power_time")
        self.compat_11n = data.get("compat_11n")
        self.signal = data.get("signal")
        self.rssi = data.get("rssi")
        self.noisefloor = data.get("noisefloor")
        self.tx_power = data.get("tx_power")
        self.distance = data.get("distance")
        self.rx_chainmask = data.get("rx_chainmask")
        self.tx_bytes = data.get("tx_bytes")
        self.rx_bytes = data.get("rx_bytes")
        self.antenna_gain = data.get("antenna_gain")
        self.cable_loss = data.get("cable_loss")
        self.height = data.get("height")
        self.ethlist = [
            StatusWirelessStaRemoteEthlist(row) for row in data.get("ethlist", [])
        ]
        self.gps = StatusWirelessStaRemoteGps(data.get("gps", {}))
        self.https_port = data.get("https_port")
        self.oob = data.get("oob")
        self.unms = StatusWirelessStaRemoteUnms(data.get("unms", {}))
        self.airview = data.get("airview")
        self.service = StatusWirelessStaRemoteService(data.get("service", {}))
        self.prs_remote = StatusWirelessStaRemotePrsRemote(data.get("prs_remote", {}))
        self.ubond_active = data.get("ubond_active")
