from utils import readFile


lines = readFile("./sampleInput.txt")
malfunctionDst = {}
outputList = []
for line in lines:
    ip = line["ip"]
    isOk = True if line["reactTime"] != "-" else False
    if isOk:
        if ip in malfunctionDst:
            deltaTime = line["time"] - malfunctionDst.pop(ip)
            outputList.append([ip, deltaTime.total_seconds()])
    else:
        if ip not in malfunctionDst:
            malfunctionDst[ip] = line["time"]
print(outputList)
