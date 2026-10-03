damages=[10,25,5,30,15]
total=0

for damage in damages:
    if damage >= 20:
        total=total+damage

print(f"강한 공격 총 데미지: {total}")