class StatusFirewall:
    iptables: bool
    ebtables: bool
    ip6tables: bool
    eb6tables: bool

    def __init__(self, data):
        self.iptables = data.get("iptables")
        self.ebtables = data.get("ebtables")
        self.ip6tables = data.get("ip6tables")
        self.eb6tables = data.get("eb6tables")
