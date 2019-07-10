from iotery_embedded_python_sdk import Iotery
from os import environ as env
from time import time

team_uuid = env.get("IOTERY_TEAM_UUID")
serial = env.get("IOTERY_DEVICE_SERIAL")
key = env.get("IOTERY_DEVICE_KEY")
secret = env.get("IOTERY_DEVICE_SECRET")

iotery = Iotery()

# Get the device token
sensor = iotery.getDeviceTokenBasic(data={"key": key,
                                     "serial": serial, "secret": secret, "teamUuid": team_uuid})
iotery.set_token(sensor["token"])
me = iotery.getMe()
t = time()

# Create the data packet and send it
data = {"packets":[{
        "timestamp": int(t),
        "deviceUuid": me["uuid"],
        "deviceTypeUuid": me["deviceTypeUuid"],
        "data":{"sensor_time": t}
    }]}

response = iotery.postData(deviceUuid=me["uuid"], data=data)

# Unexecuted commands come back from the data post
unexecuted_command_instances = response["unexecutedCommands"]["device"]

# loop through the unexecuted commands and print the command field value
for uc in unexecuted_command_instances:
    print(uc["_data"][0]["value"])

# Once the device processes the commands, they need to set them as executed
for uc in unexecuted_command_instances:
    iotery.setCommandInstanceAsExecuted(commandInstanceUuid=uc["uuid"], data={"timestamp":int(time())})
    print("Command Instance Executed!")
