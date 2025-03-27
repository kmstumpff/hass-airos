from .enums import Endpoints
from .base import BaseApi
from .entities.status import (
    Status,
    StatusHost,
    StatusWirelessSta,
    StatusWirelessStaRemote,
)


class StatusApi(BaseApi):
    def __init__(self, session):
        super().__init__(session=session)

    async def get_status(self) -> Status:
        data = await self.get(Endpoints.STATUS.value)

        entity = Status(data)
        return entity

    async def get_host(self) -> StatusHost:
        entity = await self.get_status()
        return entity.host

    async def get_local_status(self) -> StatusWirelessSta:
        entity = await self.get_status()
        return entity.wireless.sta[0]

    async def get_remote_status(self) -> StatusWirelessStaRemote:
        entity = await self.get_status()
        return entity.wireless.sta[0].remote
