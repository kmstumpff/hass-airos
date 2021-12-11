"""The airos integration."""
from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_HOST,
    CONF_PASSWORD,  
    CONF_USERNAME,
    # Platform
)
from homeassistant.core import HomeAssistant
from homeassistant.util import Throttle

from .airos_api.airos_api import AirOSApi
from .const import DOMAIN

PLATFORMS: list[str] = ["sensor"]

_LOGGER = logging.getLogger(__name__)
MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=5)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up airos from a config entry."""

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = AirOSStats(hass, entry)

    hass.config_entries.async_setup_platforms(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok

class AirOSStats:
    """This class handles communication, services, and stores the data."""

    def __init__(self, hass, entry=None):
        """Initialize the class."""
        self.hass = hass
        self.entry = entry.entry_id
        self.host = entry.data[CONF_HOST]
        self.username = entry.data[CONF_USERNAME]
        self.password = entry.data[CONF_PASSWORD]
        self.airos = AirOSApi(host=self.host, verify=False)
        self.data = None

    def get_hostname(self):
        self.airos.login(self.username, self.password)
        return self.airos.get_hostname()

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update_data(self):
        """Update data."""
        self.airos.login(self.username, self.password)
        self.data = self.airos.get_local_status()
