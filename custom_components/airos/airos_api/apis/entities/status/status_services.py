class StatusServices:
    dhcpc: bool
    dhcpd: bool
    dhcp6d_stateful: bool
    pppoe: bool
    airview: int

    def __init__(self, data):
        self.dhcpc = data.get("dhcpc")
        self.dhcpd = data.get("dhcpd")
        self.dhcp6d_stateful = data.get("dhcp6d_stateful")
        self.pppoe = data.get("pppoe")
        self.airview = data.get("airview")
