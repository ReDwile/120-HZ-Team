tokenpath = "/Users/lalkalol/Desktop/bot/Data/TG_TOKEN.txt"

def getToken(path):
    with open(path, "r") as file:
        res = str(file.read())
    return res

TG_TOKEN = getToken(tokenpath)

TG_API_URL = ""
