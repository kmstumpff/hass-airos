from . import Session


class BaseApi:
    session: Session

    def __init__(self, session: Session):
        self.session = session

        if not self.session.verify:
            import urllib3
            urllib3.disable_warnings()

    def get(self, url: str, url_format_list: dict = None):
        host = self.session.get_host()
        session = self.session.get_session()

        if url_format_list:
            url = url.format(**url_format_list)

        response = session.get(host + url)

        if response.status_code != 200:
            raise Exception(f"get: error - {response.status_code}")

        return response.json()

    def post(self, url: str, url_format_list: dict = None, data: dict = None):
        host = self.session.get_host()
        session = self.session.get_session()

        if url_format_list:
            url = url.format(**url_format_list)

        response = session.post(host + url, data=data)

        if response.status_code != 200:
            raise Exception(f"post: error - {response.status_code}")

        return response.json()

