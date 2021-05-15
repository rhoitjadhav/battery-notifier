# Packages
import time
from threading import Thread

# Modules
from battery_notifier import BatteryNotifier

# Configuration
app_name = 'Battery Notifier'
low_battery_summary = 'Battery Low'
high_battery_summary = 'Battery High'
low_battery_message = 'Rohit, plugged in the power'
high_battery_message = 'Rohit, remove the power plug'
low_battery_icon = 'battery-low'
high_battery_icon = 'battery-full'
low_level_percentage = 40
high_level_percentage = 80

# BatteryNotifier instance
bn = BatteryNotifier(app_name,
                     low_battery_summary,
                     high_battery_summary,
                     low_battery_message,
                     high_battery_message,
                     low_battery_icon,
                     high_battery_icon)

low_battery_thread = Thread(target=bn.check_for_low_battery, args=(low_level_percentage,))
low_battery_thread.setDaemon(True)

high_battery_thread = Thread(target=bn.check_for_high_battery, args=(high_level_percentage,))
high_battery_thread.setDaemon(True)

low_battery_thread.start()
high_battery_thread.start()

try:
    print("Battery Notifier service is started!")
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    print("User interrupted! Exiting...")
