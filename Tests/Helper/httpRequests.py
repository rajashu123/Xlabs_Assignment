import requests


def makePostRequest(url,data):
    try:
        response  = requests.post(url = url,body = data)
        return response
    except Exception as err:
        print('Issue happened while making the post request :',err)
        return None
    else:
        print('Post request successful')


def makeGetRequest(url,verify=True):
    try:
        response = requests.get(url = url,verify = verify)
        return response
    except Exception as err:
        print('Issue happened while making the get request :', err)
        return None
    else:
        print('Get request successful')
