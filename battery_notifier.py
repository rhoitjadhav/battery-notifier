import time

from battery import Battery
from notifier import Notifier


class BatteryNotifier:
    def __init__(
            self,
            app_name: str,
            low_battery_summary: str,
            high_battery_summary: str,
            low_battery_message: str,
            high_battery_message: str,
            low_battery_icon: str,
            high_battery_icon: str
    ):
        self._app_name = app_name
        self._low_battery_summary = low_battery_summary
        self._high_battery_summary = high_battery_summary
        self._low_battery_message = low_battery_message
        self._high_battery_message = high_battery_message
        self._low_battery_icon = low_battery_icon
        self._high_battery_icon = high_battery_icon

        self._battery = Battery()
        self._notifier = Notifier(self._app_name)

    def check_for_low_battery(self, low_level: int = 40) -> None:
        """
        Checking of low battery percentage. By default it check for 80
        Args:
            low_level: battery percentage number
        """
        low_battery_flag = False
        try:
            while True:
                percentage = self._battery.get_percentage()
                plugged = self._battery.is_plugged()

                if (percentage <= low_level) and (plugged is False) and (low_battery_flag is False):
                    self._notifier.show(self._low_battery_summary,
                                        self._low_battery_message,
                                        self._low_battery_icon)
                    low_battery_flag = True

                if percentage > low_level:
                    low_battery_flag = False

                time.sleep(3)

        except KeyboardInterrupt:
            print("User interrupted!")

    def check_for_high_battery(self, high_level: int = 80) -> None:
        """
        Checking of low battery percentage. By default it check for 80
        Args:
            high_level: battery percentage number
        """
        high_battery_flag = False
        try:
            while True:
                percentage = self._battery.get_percentage()
                plugged = self._battery.is_plugged()

                if (percentage >= high_level) and plugged and (high_battery_flag is False):
                    self._notifier.show(self._high_battery_summary,
                                        self._high_battery_message,
                                        self._high_battery_icon)
                    high_battery_flag = True

                if percentage < high_level:
                    high_battery_flag = False

                time.sleep(3)

        except KeyboardInterrupt:
            print("User interrupted!")
