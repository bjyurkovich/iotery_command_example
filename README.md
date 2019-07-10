# Iotery Command Example in Python

The following code is an example utilizing a server and a device to create a command instance, have the device process the command, and set the command as executed.

Make sure you are using Python 3!

## Getting Started

Clone the repo:

```
git clone https://github.com/bjyurkovich/iotery_command_example.git
```

Activate your virtualenv and install the dependencies:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

The `server.py` and `device.py` assume you have some environment variables set:

```
export IOTERY_API_KEY=your-api-key-found-on-iotery-dashboard

export IOTERY_TEAM_UUID=your-iotery-team-uuid-found-on-dashboard

export IOTERY_DEVICE_SERIAL=your-device-serial-that-you-create
export IOTERY_DEVICE_KEY=your-device-serial-that-you-create
export IOTERY_DEVICE_SECRET=your-device-serial-that-you-create
```

If you are new to Iotery an creating device types and devices, [check out this tutorial](https://dev.to/bjyurkovich/get-started-with-your-iot-devices-using-iotery-io-4c2d).

## Running the Example:

Then run the server:

```
python server.py
```

> `server.py` assumes you have already created a device (identity set in your env vars), command type called `SENSOR_COMMAND_1`, and a command field for that command type called `TIME_TO_TURN_ON`. The server will create a `command instance` that will be retrieved by the device when it posts data

and then run the device:

```
python device.py
```

> `device.py` assumes you have created your device in iotery and will post data to the cloud, and if a command instance exists from your server, will set it executed after printing out the command field.
