player={
    "level": 12,
    "inventory": ["검","포션","열쇠"]
}

if player["level"] >=10 and "열쇠" in player["inventory"]:
    print("보스전 입장")
else:
    print("입장 불가")