from . import StatusInterfacesStatus


class StatusInterfaces:
    ifname: str
    hwaddr: str
    enabled: bool
    mtu: int
    status: StatusInterfacesStatus

    def __init__(self, data):
        self.ifname = data.get("ifname")
        self.hwaddr = data.get("hwaddr")
        self.enabled = data.get("enabled")
        self.mtu = data.get("mtu")
        self.status = StatusInterfacesStatus(data.get("status", {}))
