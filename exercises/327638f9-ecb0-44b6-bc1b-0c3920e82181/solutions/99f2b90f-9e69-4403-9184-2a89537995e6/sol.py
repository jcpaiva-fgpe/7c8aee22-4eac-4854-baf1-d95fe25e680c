import json

def sensors(sensor_array):
    # TODO this is what you need to complete
    result = ""
    for i in range(len(sensor_array)):
        if i == 0:
            result += f"Sensor {i+1}: {readings[i]} °C"
        else:
            result += f", Sensor {i+1}: {readings[i]} °C"
    print(result)


############## DO NOT TOUCH AREA: START #################
if __name__ == '__main__':
    inp = input()
    sensor_array = json.loads(inp)
    sensors(sensor_array)
############## DO NOT TOUCH AREA: END ###################
