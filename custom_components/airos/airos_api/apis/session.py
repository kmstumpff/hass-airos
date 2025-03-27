import atexit
import aiohttp
import asyncio


class Session:
    verify: bool
    host: str
    token: str
    session: aiohttp.ClientSession

    def __init__(self, host: str, verify: bool, token: str = None):
        self.host = host
        self.token = token
        self.verify = verify
        self.cookie_jar = aiohttp.CookieJar(unsafe=True)
        self.session = aiohttp.ClientSession(cookie_jar=self.cookie_jar)
        atexit.register(self.cleanup)

    def cleanup(self):
        asyncio.run(self.session.close())

    async def ping(self):
        try:
            async with self.get(self.host) as response:
                return response.status == 200
        except aiohttp.ClientConnectionError:
            return False

    async def get(self, url: str):
        response = await self.session.get(self.host + url, ssl=self.verify) 
        response.raise_for_status()

        return await response.json()

    async def post(self, url: str, data: dict):
        response = await  self.session.post(
            self.host + url, data=data, ssl=self.verify
        )
        response.raise_for_status()

        return await response.json()

    def get_host(self):
        return self.host

    def set_token(self, token=None):
        self.token = token
