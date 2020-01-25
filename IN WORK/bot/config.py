import configparser

tokenpath = "./Data/TG_TOKENS.ini"

def getToken(path):

    config = configparser.RawConfigParser()
    config.read(tokenpath)

    return config.get('Config', 'Config.test_token')

TG_TOKEN = getToken(tokenpath)

TG_API_URL = ""

