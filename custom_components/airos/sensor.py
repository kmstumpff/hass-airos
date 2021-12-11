"""Support for AirOS sensors."""
from __future__ import annotations
from .airos_api.airos_api import AirOSApi

from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    FREQUENCY_MEGAHERTZ,
    PERCENTAGE,
    LENGTH_METERS,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    DATA_RATE_MEGABITS_PER_SECOND,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
import logging
_LOGGER = logging.getLogger(__name__)


SENSORS: dict[str, SensorEntityDescription] = {
    "hostname": SensorEntityDescription(
        key="hostname",
        name="Hostname",
    ),
    "device_model": SensorEntityDescription(
        key="device_model",
        name="Device Model",
    ),
    "uptime": SensorEntityDescription(
        key="uptime",
        name="Uptime",
    ),
    "cpu": SensorEntityDescription(
        key="cpu",
        name="CPU Load",
        native_unit_of_measurement=PERCENTAGE,
    ),
    "firmware_version": SensorEntityDescription(
        key="firmware_version",
        name="Firmware Version",
    ),
    "gps_lat": SensorEntityDescription(
        key="gps_lat",
        name="Latitude",
    ),
    "gps_lon": SensorEntityDescription(
        key="gps_lon",
        name="Longitude",
    ),
    "mac": SensorEntityDescription(
        key="mac",
        name="MAC",
    ),
    "distance": SensorEntityDescription(
        key="distance",
        name="Distance",
        native_unit_of_measurement=LENGTH_METERS,
    ),
    "signal": SensorEntityDescription(
        key="signal",
        name="Signal",
        # device_class=SensorDeviceClass.SIGNAL_STRENGTH,
        native_unit_of_measurement=SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    ),
    "rx_data_rate": SensorEntityDescription(
        key="rx_data_rate",
        name="RX Data Rate",
    ),
    "snr": SensorEntityDescription(
        key="snr",
        name="SNR",
    ),
    "capacity": SensorEntityDescription(
        key="capacity",
        name="Capacity",
        native_unit_of_measurement=DATA_RATE_MEGABITS_PER_SECOND,
    ),
    "rx_throughput": SensorEntityDescription(
        key="rx_throughput",
        name="RX Throughput",
        native_unit_of_measurement=DATA_RATE_MEGABITS_PER_SECOND,
    ),
    "tx_throughput": SensorEntityDescription(
        key="tx_throughput",
        name="TX Throughput",
        native_unit_of_measurement=DATA_RATE_MEGABITS_PER_SECOND,
    ),
    "frequency": SensorEntityDescription(
        key="tx_throughput",
        name="TX Throughput",
        # device_class=SensorDeviceClass.FREQUENCY,
        native_unit_of_measurement=FREQUENCY_MEGAHERTZ,
    ),
    "bandwidth": SensorEntityDescription(
        key="bandwidth",
        name="Bandwidth",
        # device_class=SensorDeviceClass.FREQUENCY,
        native_unit_of_measurement=FREQUENCY_MEGAHERTZ,
    ),
}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the AirOS sensor."""
    api: AirOSApi = hass.data[DOMAIN][entry.entry_id]

    hostname = await hass.async_add_executor_job(api.get_hostname)
    async_add_entities([AirOSSensor(api, SENSORS[sensor], hostname, entry) for sensor in SENSORS], True)


class AirOSSensor(SensorEntity):
    """Entity object for AirOS sensor."""

    def __init__(self, airos: AirOSApi, sensor: SensorEntityDescription, hostname, entry=None) -> None:
        """Entity object for Flick Electric sensor."""
        self._airos: AirOSApi = airos
        self._hostname = hostname
        self._sensor = sensor
        self._entry_id = entry.entry_id
        self._state = None
        self._data = None

    def update(self):
        """Update the sensor."""
        try:
            self.hass.data[DOMAIN][self._entry_id].update_data()
        except Exception as ex:
            _LOGGER.error(f"Error updating airos sensor: {ex}")
        self._data = self.hass.data[DOMAIN][self._entry_id].data

        if self._data and self._sensor.key in self._data:
            self._state = self._data[self._sensor.key]

    @property
    def unique_id(self):
        """Return a unique ID to use for this sensor."""
        return "{}_{}".format(self._entry_id, self._sensor.key)

    @property
    def should_poll(self):
        """Return the name of the sensor."""
        return True

    @property
    def name(self):
        """Return the name of the sensor."""
        return "{} {}".format(self._hostname, self._sensor.name)

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit the value is expressed in."""
        return self._sensor.native_unit_of_measurement
