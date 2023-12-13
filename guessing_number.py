from random import randint
import os
import time

user_attempts = 0
user_score = 0

pc_attempts = 0
pc_score = 0


def play_user():
    global user_attempts, user_score
    print("Boshladik!")

    n = randint(1, 100)
    print("- Men bir son o'yladim. Topishga harakat qiling:")

    while True:
        gn = int(input("- "))
        user_attempts += 1
        if gn < n:
            print("- Men o'ylagan son bundan kattaroq. Yana urinib ko'ring.")
            continue
        elif n < gn:
            print("- Men o'ylagan son bundan kichikroq. Qayta urining.")
            continue
        elif gn == n:
            print("- Tabriklayman! Topdingiz!")
            print(f"- {user_attempts} ta urinishda topdingiz.")
            break
    print()


def play_pc():
    print("- 1 dan 10 gacha son o'ylang. Men topaman")
    input("- O'ylagan bo'lsangiz ENTER tugmasini bosing")

    print("- Boshladik!")
    min, max = 1, 10
    global pc_attempts, pc_score

    while True:
        gn = randint(min, max)
        print(f"- Siz {gn} sonini o'ylagansiz.")

        correct = input("(xa/kattaroq (+)/kichikroq (-))  ")
        pc_attempts += 1
        if correct.lower() == "xa":
            print("- URAAA! Topdim!")
            print(f"- {pc_attempts} ta urinishda topdim")
            break
        elif correct == "-":
            max = gn - 1
            continue
        elif correct == "+":
            min = gn + 1
            continue
    print()


def play():
    global user_attempts, user_score, pc_attempts, pc_score
    first, second = None, None

    print('- Assalomu alaykum! Siz "Son top" o\'yinini ishga tushirdingiz')
    player = input("- Kim birinchi boshlaydi? (user/pc)  \n- ")

    if player == "user":
        first, second = play_user, play_pc
    else:
        first, second = play_pc, play_user

    first()
    time.sleep(5)
    os.system("cls")
    second()
    time.sleep(5)
    os.system("cls")
    if user_attempts > pc_attempts:
        pc_score += 1
    elif pc_attempts > user_attempts:
        user_score += 1

    user_attempts, pc_attempts = 0, 0

    print("- O'yin tugadi")
    print(f"   Hisob\nuser - PC\n  {user_score}  -  {pc_score}")


play()
