
# Server Imports
from iotery_python_server_sdk import Iotery
from os import environ as env
from time import time


""" SERVER CODE """
api_key = env.get("IOTERY_API_KEY")

iotery = Iotery(api_key)

# Get the sensor we want to command
# Note that I have already created a device in Iotery
sensorList = iotery.getDeviceList({"serial":"SENSOR_COMMAND_1"})
sensor = sensorList["results"][0]

# Get my command type that I created already
commandTypeList = iotery.getCommandTypeList({"enum":"SENSOR_COMMAND_ON"})
on_command_type = commandTypeList["results"][0]
command_field = on_command_type["commandFieldList"][0]

# Create the command
iotery.createDeviceCommandInstance(deviceUuid=sensor["uuid"], data={
    "commandTypeUuid": on_command_type["uuid"],
    "commandFields": [{"commandFieldUuid":command_field["uuid"], "value":int(time())}]
  }
)

