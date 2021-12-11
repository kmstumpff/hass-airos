import requests


class Session:
    verify: bool
    host: str
    token: str
    session: requests.Session

    def __init__(self, host: str, verify: bool, token: str = None):
        self.host = host
        self.token = token
        self.verify = verify
        self.session = requests.Session()
        self.session.verify = verify

        if token:
            self.session.headers.update({"x-auth-token": token})

    def ping(self):
        try:
            self.session.get(self.host)
            return True
        except requests.exceptions.ConnectionError as ce:
            return False

    def get_host(self):
        return self.host

    def get_session(self):
        return self.session

    def set_token(self, token=None):
        self.token = token
        if token:
            self.session.headers.update({"x-auth-token": token})
