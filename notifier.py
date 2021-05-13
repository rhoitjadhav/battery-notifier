import notify2


class Notifier:
    def __init__(self, app_name: str) -> None:
        notify2.init(app_name)

    @staticmethod
    def show(summary: str, message: str = "", icon: str = "") -> None:
        """
        Show notification bar
        Args:
            summary: title of the notification
            message: message to be displayed
            icon: icon of notification bar
        """
        notification = notify2.Notification(summary, message, icon)
        notification.show()
