from typing import Any
from .apis import AuthorizationApi, StatusApi, Session


class AirOSApi:
    session: Any
    authorization: AuthorizationApi
    status: StatusApi
    host: str

    def __init__(self, host="http://localhost", token=None, verify=True):
        self.host = host

        self.session = Session(host=host, verify=verify, token=token)

        self.authorization = AuthorizationApi(self.session)

        self.status = StatusApi(self.session)

    def ping(self):
        return self.session.ping()

    def login(self, username: str, password: str):
        try:
            if not self.authorization.is_logged_in():
                self.authorization.login(username, password)
            return True
        except Exception as ex:
            return False

    def get_local_status(self):
        status = self.status.get_status()
        return {
            "hostname": status.host.hostname,
            "device_model": status.host.devmodel,
            "uptime": status.host.uptime,
            "cpu": status.host.cpuload,
            "firmware_version": status.host.fwversion,
            "gps_lat": status.gps.lat,
            "gps_lon": status.gps.lon,
            "mac": status.wireless.apmac,
            "distance": status.wireless.distance,
            "signal": status.wireless.sta[0].prs_sta.rssi_data,
            "rx_data_rate": status.wireless.sta[0].prs_sta.rx_mcs,
            "snr": status.wireless.sta[0].prs_sta.snr,
            "capacity": status.wireless.sta[0].prs_sta.capacity,
            "rx_throughput": status.wireless.throughput.rx,
            "tx_throughput": status.wireless.throughput.tx,
            "frequency": status.wireless.prs_info.frequency,
            "bandwidth": status.wireless.prs_info.chanbw,
        }

    def get_host(self):
        return self.host

    def get_hostname(self):
        status = self.status.get_status()
        return status.host.hostname

    def get_device_id(self):
        status = self.status.get_status()
        return status.host.device_id

    def test(self):
        # dt_format = "%Y-%m-%dT%H:%M:%SZ"

        status = self.status.get_status()
        # print(f"{status.host.devmodel=}")
        # print(f"{status.host.hostname=}")
        # print(f"{status.host.fwversion=}")
        print(f"{status.host.hostname=}")
        print(f"{status.host.devmodel=}")
        print(f"{status.host.uptime=}")
        print(f"{status.host.cpuload=}")
        print(f"{status.host.fwversion=}")

        print(f"{status.gps.lat=}")
        print(f"{status.gps.lon=}")
        print(f"{status.wireless.apmac=}")
        print(f"{status.wireless.distance=}")

        # 60 GHz
        print(f"{status.wireless.sta[0].signal=}")
        print(f"{status.wireless.sta[0].prs_sta.rx_mcs=}")
        print(f"{status.wireless.sta[0].prs_sta.snr=}")
        print(f"{status.wireless.sta[0].prs_sta.capacity=}")
        print(f"{status.wireless.throughput.rx=}")
        print(f"{status.wireless.throughput.tx=}")
        print(f"{status.wireless.prs_info.frequency=}")
        print(f"{status.wireless.prs_info.chanbw=}")

        host = self.status.get_host()
        # print(f"{host.hostname=}")

        local_status = self.status.get_local_status()
        # print(f"{local_status.signal=}")
        # print(f"{local_status.signal=}")

        # remote_status = self.status.get_remote_status()
        # print(f"{remote_status.hostname=}")
        # print(f"{remote_status.signal=}")
