# import requests
# import ssl

import aiohttp


class Session:
    verify: bool
    host: str
    token: str
    # session: requests.Session
    # session: aiohttp.ClientSession

    def __init__(self, host: str, verify: bool, token: str = None):
        self.host = host
        self.token = token
        self.verify = verify
        # self.session = requests.Session()
        self.session = aiohttp.ClientSession()
        # self.session.verify = verify

        # if token:
        #     self.session.headers.update({"x-auth-token": token})

    async def ping(self):
        try:
            async with self.get(self.host) as response:
                return response.status == 200
        except aiohttp.ClientConnectionError:
            return False

    async def get(self, url: str):
        # headers = {"x-auth-token": self.token} if self.token else None
        # async with aiohttp.ClientSession() as session:
        async with self.session.get(self.host + url, ssl=self.verify) as response:
            if response.status != 200:
                raise Exception(f"get: error - {response.status}")

            return await response.json()

    async def post(self, url: str, data: dict):
        # headers = {"x-auth-token": self.token} if self.token else None
        # async with aiohttp.ClientSession() as session:
        async with self.session.post(
            self.host + url, data=data, ssl=self.verify
        ) as response:
            if response.status != 200:
                raise Exception(f"post: error - {response.status}")

            return await response.json()

    def get_host(self):
        return self.host

    # def get_session(self):
    #     return self.session

    def set_token(self, token=None):
        self.token = token
        # if token:
        #     self.session.headers.update({"x-auth-token": token})
