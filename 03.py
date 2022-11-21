from utils import readFile
from collections import deque


lines = readFile("./sampleInput.txt")
N, M, T = map(int, input().split())
malfunctionDst = {}
reactionTime = {}
outputList = []
for line in lines:
    ip = line["ip"]
    isOk = True if line["reactTime"] != "-" else False

    if isOk:
        if ip in malfunctionDst:
            if malfunctionDst[ip]["count"] >= N:
                deltaTime = line["time"] - malfunctionDst.pop(ip)["time"]
                outputList.append([ip, deltaTime.total_seconds()])
            else:
                malfunctionDst.pop(ip)
    else:
        if ip not in malfunctionDst:
            malfunctionDst[ip] = {"time": line["time"], "count": 1}
        else:
            malfunctionDst[ip]["count"] += 1
print(outputList)
