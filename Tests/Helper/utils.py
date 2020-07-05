import json
import jsonpath

def getDataFromJson(body,path):
    json_resp = json.loads(body.content)
    data = jsonpath.jsonpath(json_resp,path)
    return data[0]
