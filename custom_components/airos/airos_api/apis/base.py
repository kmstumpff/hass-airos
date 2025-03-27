from . import Session


class BaseApi:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    async def get(self, url: str, url_format_list: dict = None):
        if url_format_list:
            url = url.format(**url_format_list)

        return await self.session.get(url)

    async def post(self, url: str, url_format_list: dict = None, data: dict = None):
        if url_format_list:
            url = url.format(**url_format_list)

        return await self.session.post(url, data=data)
