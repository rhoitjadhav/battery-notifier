# Packages
import notify2
from notify2 import Notification


class Notifier:
    """
    Notifier class is responsible for creating and managing the
    notification
    Args:
        summary: title of the notification
        message: message to be displayed
        icon: icon of notification bar
    """

    def __init__(self, app_name: str, summary: str, message: str = "", icon: str = "") -> None:
        self._app_name = app_name
        self._summary = summary
        self._message = message
        self._icon = icon

        notify2.init(self._app_name)
        self._notification = Notification(self._summary, self._message, self._icon)

    def show(self) -> None:
        """
        Show notification bar
        """
        self._notification.show()

    def close(self) -> None:
        """
        Remove notification bar from tray
        """
        self._notification.close()
