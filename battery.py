# Packages
import psutil


class Battery:
    """
    Batteru class is responsible for getting battery
    related information
    """

    @staticmethod
    def _sensors_battery():
        """
        Returns battery information
        """
        return psutil.sensors_battery()

    def get_percentage(self) -> int:
        """
        Returns battery percentage
        """
        return self._sensors_battery().percent

    def is_plugged(self) -> bool:
        """
        Returns boolean whether the battery power plugged or not
        """
        return self._sensors_battery().power_plugged
