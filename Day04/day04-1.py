turn = 0

while turn < 5:
    turn = turn + 1
    if turn ==3:
        print("3턴은 기절 상태")
        continue
    print(f"{turn}턴 공격!")
