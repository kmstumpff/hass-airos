
from .enums import Endpoints

from . import Session

class AuthorizationApi:
    host: str
    token: str
    logged_in: bool

    def __init__(self, session: Session):
        self.session = session 
        self.logged_in = False

    def is_logged_in(self):
        return self.logged_in

    def login(self, username: str, password: str):
        data = {
            "hide_rd": True,
            "username": username,
            "password": password
        }
        host = self.session.get_host()
        session = self.session.get_session()

        response = session.post(host + Endpoints.AUTH.value, data=data)

        if response.status_code != 200:
            self.logged_in = False
            raise Exception(f"login: error - {response.status_code}")

        json = response.json()
        self.session.set_token(json.get("utoken"))
        self.logged_in = True

        return json
