import random
n = input("Выберите один из вариантов (1) or (2):")
if n =="1": 
    print("Вы выбрали игру под номером (1) 'Угадай число'")
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
elif n == "2":
    print("Вы выбрали игру под номером (2) 'Камень, ножница и бумага'")
    def play():
        while True:    
            list = ['камень', 'ножница','бумага']
            comp_vibor = random.choice(list)
            print('Выберите один из вариантов: камень, ножница или бумага')
            vash_vibor = input()
            if vash_vibor == comp_vibor:
                print(f'Ничья! Оба выбрали {vash_vibor}.')
            elif(vash_vibor == 'ножница' and comp_vibor == 'камень') or \
                (vash_vibor == 'бумага' and comp_vibor == 'ножница') or \
                (vash_vibor == 'камень' and comp_vibor == 'бумага'):
                print(f'Ты проиграл! Ваш противник выбрал {comp_vibor}.')
            else:        
                print(f'Ты выиграл, повезло! Ваш противник выбрал  {comp_vibor}.')
                break
    play()