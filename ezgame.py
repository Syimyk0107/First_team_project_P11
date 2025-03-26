import random
num = random.randint(1, 10)
while True:
    chis = int(input("Введите число: "))
    if num == chis:
        print(f"Победа. Ты должен был угодать число - {num}")
        break
    elif num < chis:
        print(f"Твое число меньше {chis}")
    elif num > chis:
        print(f"Твое число больше {chis}")


