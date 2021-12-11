class StatusChainNames:
    number: int
    name: str

    def __init__(self, data):
        self.number = data.get("number")
        self.name = data.get("name")
