damages = [10, 25, 5, 30, 15, 40]
total = 0
count = 0

for damage in damages:
    if damage >= 20:
        count = count + 1
        total = total + damage

print(f"강한 공격 횟수: {count}")
print(f"강한 공격 총 데미지: {total}")
