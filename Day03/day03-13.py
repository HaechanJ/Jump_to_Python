enemy_hp=30

while enemy_hp >0:
    print("공격!")
    enemy_hp=enemy_hp-10
    print(f"남은 HP:{enemy_hp}")

    if enemy_hp <=0:
        print("적을 쓰러뜨렸습니다!")
        break