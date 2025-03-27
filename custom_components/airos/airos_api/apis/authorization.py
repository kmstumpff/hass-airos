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

    async def login(self, username: str, password: str):
        data = {"hide_rd": True, "username": username, "password": password}

        try:
            json = await self.session.post(Endpoints.AUTH.value, data=data)

            self.session.set_token(json.get("utoken"))
            self.logged_in = True

            return json
        except Exception as ex:
            print(f"Failed to login: {ex}")
            self.logged_in = False
            raise Exception from ex
