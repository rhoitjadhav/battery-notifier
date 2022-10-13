# Battery-Notifier

This project aims to notify the user when the battery levels are below low and high. The ideal low and high battery
levels are 40 and 80 respectively, so that user don't need to check the battery percentage, a user
can simply rely on this application whenever battery is charged or at low levels.

## Requirements

- Python 3.8+
- Psutil
- Notify2
- Dbus-Python

## Installation

`install.sh` will install all dependencies required to run this application which includes python 3, pipenv, psutil,
notify2, dbus-python and other required packages which is defined in requirements.txt. Additionally, it will ask you for
the permission to install the packages.

**Note:** Before executing the `install.sh` script please make sure to go through the file and make necessary changes
according to your needs if any.

## Running Application

```bash
python3 main.py
```
