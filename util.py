import requests, json, pprint


def createJsonFIle():
    url = "https://api.exchangerate.host/latest"

    response = requests.get(url)

    jsonData = json.dumps(response.json()['rates'], indent=3)

    with open("jsonFile.json", 'w') as jf:
        jf.write(jsonData)



createJsonFIle()

