class StatusWirelessPolling:
    dcap: int
    ucap: int

    def __init__(self, data):
        self.dcap = data.get("dcap")
        self.ucap = data.get("ucap")
