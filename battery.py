import psutil


class Battery:
    def __init__(self) -> None:
        self._battery = psutil.sensors_battery()

    def get_percentage(self) -> int:
        """
        Returns battery percentage
        """
        return self._battery.percent

    def is_plugged(self) -> bool:
        """
        Returns boolean whether the battery power plugged or not
        """
        return self._battery.power_plugged
