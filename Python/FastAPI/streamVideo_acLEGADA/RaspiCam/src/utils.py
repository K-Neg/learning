import json


def ip_check():
    # get local IP
    import os

    stream = os.popen("hostname -I")
    local_ip = stream.read().strip()
    return local_ip


def getJson():
    with open("templates/jsonFiles/selects.json") as json_file:
        data = json.load(json_file)
    #with open("templates/jsonFiles/resolutions.json") as json_file:
        #data = json.load(json_file)

    #data.update(buf)
    print(data)
    return data