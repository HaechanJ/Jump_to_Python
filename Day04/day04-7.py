damages = [10, 25, 5, 30, 15, 40]
count = 0

for damage in damages:
    if damage >= 20:
        count=count+1

print(f"강한 공격 횟수: {count}")