import datetime


def readFile(path):
    with open(path) as f:
        l_strip = [convert2Obj(s.strip()) for s in f.readlines()]
    return l_strip


def convert2Obj(str):
    dateObj = {
        "year": int(str[:4]),
        "month": int(str[4:6]),
        "day": int(str[6:8]),
        "hour": int(str[8:10]),
        "minute": int(str[10:12]),
        "second": int(str[12:14]),
        "ip": str[15:].split(",")[0],
        "reactTime": str[15:].split(",")[1],
    }
    dateObj["time"] = datetime.datetime(
        dateObj["year"],
        dateObj["month"],
        dateObj["day"],
        dateObj["hour"],
        dateObj["minute"],
        dateObj["second"],
    )
    return dateObj
