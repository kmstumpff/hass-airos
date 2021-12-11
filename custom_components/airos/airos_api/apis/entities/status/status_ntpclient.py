class StatusNtpclient:
    last_sync: str

    def __init__(self, data):
        self.last_sync = data.get("last_sync")
