import json

configPath = "../config/config.json"
customerPath = "../DotaWatcher/customerInfo.json"
lastMatchPath = "../DotaWatcher/lastMatch.json"


# config
def getConfig():
    with open(configPath, "r", encoding='utf-8') as f:
        return json.load(f)


def setConfig(data):
    with open(configPath, "w", encoding='utf-8') as f:
        json.dump(data, f)


# customerinfo
def getCustomerInfo():
    with open(customerPath, "r", encoding='utf-8') as f:
        return json.load(f)

def setCustomerInfo(data):
    with open(customerPath, "w", encoding='utf-8') as f:
        json.dump(data, f)


# lastmatch
def getLastMatch():
    with open(lastMatchPath, "r", encoding='utf-8') as f:
        return json.load(f)


def setLastMatch(data):
    with open(lastMatchPath, "w", encoding='utf-8') as f:
        json.dump(data, f)
