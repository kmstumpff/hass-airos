from typing import List

from . import (
    StatusFirewall,
    StatusGps,
    StatusHost,
    StatusNtpclient,
    StatusServices,
    StatusUnms,
    StatusWireless,
)
from .status_chain_names import StatusChainNames
from .status_interfaces import StatusInterfaces


class Status:
    chain_names: List[StatusChainNames]
    host: StatusHost
    genuine: str
    services: StatusServices
    firewall: StatusFirewall
    portfw: bool
    wireless: StatusWireless
    interfaces: List[StatusInterfaces]
    ntpclient: StatusNtpclient
    unms: StatusUnms
    gps: StatusGps

    def __init__(self, data):
        self.chain_names = [
            StatusChainNames(row) for row in data.get("chain_names", [])
        ]
        self.host = StatusHost(data.get("host", {}))
        self.genuine = data.get("genuine")
        self.services = StatusServices(data.get("services", {}))
        self.firewall = StatusFirewall(data.get("firewall", {}))
        self.portfw = data.get("portfw")
        self.wireless = StatusWireless(data.get("wireless", {}))
        self.interfaces = [StatusInterfaces(row) for row in data.get("interfaces", [])]
        self.ntpclient = StatusNtpclient(data.get("ntpclient", {}))
        self.unms = StatusUnms(data.get("unms", {}))
        self.gps = StatusGps(data.get("gps", {}))
