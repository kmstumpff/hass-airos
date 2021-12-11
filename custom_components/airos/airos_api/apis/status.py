from .enums import Endpoints
from .base import BaseApi
from .entities.status import Status, StatusHost, StatusWirelessSta, StatusWirelessStaRemote


class StatusApi(BaseApi):

    def __init__(self, session):
        super().__init__(session=session)

    def get_status(self) -> Status:
        data = self.get(Endpoints.STATUS.value)

        entity = Status(data)
        return entity

    def get_host(self) -> StatusHost:
        entity = self.get_status()
        return entity.host

    def get_local_status(self) -> StatusWirelessSta:
        entity = self.get_status()
        return entity.wireless.sta[0]

    def get_remote_status(self) -> StatusWirelessStaRemote:
        entity = self.get_status()
        return entity.wireless.sta[0].remote

