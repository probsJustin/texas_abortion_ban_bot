
import json


class TABB_configuration:
    dict_configData = dict()
    with open('./config.json') as json_configData:
        dict_configData = json.load(json_configData)

