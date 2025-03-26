import random  

def start_game():
    player_health = 100       # Здоровье игрока
    player_potions = 2        # Количество лечебных зелий
    player_attack_min = 10    # Минимальный урон игрока
    player_attack_max = 30    # Максимальный урон игрока
    player_weapon = "Кинжал"  # Начальное оружие
    player_weapon_bonus = 0   # Дополнительный бонус к урону от оружия
    player_xp = 0             # Опыт игрока
    player_level = 1          # Уровень игрока
    # Определяем врагов в игре
    enemies = {
        "тролль": {"health": 50, "attack_min": 5, "attack_max": 20, "xp": 20},
        "волк": {"health": 30, "attack_min": 8, "attack_max": 15, "xp": 15},
        "призрак": {"health": 40, "attack_min": 10, "attack_max": 25, "xp": 25}
    }

  
    def level_up():
        nonlocal player_xp, player_level, player_attack_min, player_attack_max, player_health
        if player_xp >= player_level * 30:
            player_level += 1
            player_xp = 0
            player_health += 20
            player_attack_min += 5
            player_attack_max += 10
            print(f"Поздравляем! Вы достигли уровня {player_level}! Ваши характеристики улучшены!")
    
    print("Вы оказались в темном лесу. Перед вами две тропы.")
    choice1 = input("Выберите: налево (1) или направо (2)? ")
    
    if choice1 == "1":
        print("Вы пошли налево и встретили странного старца.")
        choice2 = input("Будете с ним разговаривать (1), уйдете (2) или попытаетесь украсть его посох (3)? ")
        
        if choice2 == "1":
            print("Старец предлагает вам отгадать загадку: 'Что всегда идет, но никогда не приходит?'")
            answer = input("Ваш ответ: ").lower()
            if answer in ["время", "времена"]:
                print("Старец улыбается и дает вам магический меч! Теперь ваши атаки стали намного сильнее!")
                player_weapon = "Магический меч"
                player_weapon_bonus = 15
                player_attack_min += player_weapon_bonus
                player_attack_max += player_weapon_bonus
            else:
                print("Старец расстроен и исчезает. Вы продолжаете путь, но вскоре теряетесь в лесу. Игра окончена.")
                return
        elif choice2 == "2":
            choice3 = input("Вы ушли, но заблудились в лесу. Перед вами две пещеры. Выберите (1) или (2):")
            if choice3 == "1":
                print("В пещере находится злодей")
                enemy = random.choice(list(enemies.keys()))  # Выбираем случайного врага
                enemy_stats = enemies[enemy]
                print(f"Вы пошли направо и встретили {enemy}!")
                choice3 = input("Будете сражаться (1), убегать (2) или попробовать обмануть его (3)? ")
                if choice3 == "1":
                    print(f"Вы вступаете в бой с {enemy}!")
                    while player_health > 0 and enemy_stats["health"] > 0:
                        action = input("Атаковать (1) или выпить зелье (2)? ")
                        if action == "1":
                            attack = random.randint(player_attack_min, player_attack_max)  # Вычисляем случайный урон
                            print(f"Вы атакуете {enemy} своим {player_weapon} и отнимаете {attack} HP!")
                            enemy_stats["health"] -= attack
                            if enemy_stats["health"] <= 0:
                                print(f"Вы победили {enemy}! Вы получили {enemy_stats['xp']} опыта!")
                                player_xp += enemy_stats["xp"]
                                level_up()
                                break
                    
                        enemy_attack = random.randint(enemy_stats["attack_min"], enemy_stats["attack_max"])  # Враг атакует
                        print(f"{enemy} атакует вас и наносит {enemy_attack} HP урона!")
                        player_health -= enemy_attack
                        if player_health <= 0:
                            print(f"{enemy} вас победил... Игра окончена.")
                            return
                        elif action == "2" and player_potions > 0:
                            heal = random.randint(15, 30)  # Восстановление здоровья зельем
                            player_health += heal
                            player_potions -= 1
                            print(f"Вы выпили зелье и восстановили {heal} HP! У вас осталось {player_potions} зелья.")
                        else:
                            print("У вас нет зелий! Вы вынуждены сражаться!")
                    
        elif choice3 == "3":
            print(f"Вы убежали, но упали в яму. А там вас ждал {enemy}")
            print(f"Вы вступаете в бой с {enemy} чтобы выйти живым из ямы!")
            while player_health > 0 and enemy_stats["health"] > 0:
                action = input("Атаковать (1) или выпить зелье (2)? ")
                if action == "1":
                    attack = random.randint(player_attack_min, player_attack_max)  # Вычисляем случайный урон
                    print(f"Вы атакуете {enemy} своим {player_weapon} и отнимаете {attack} HP!")
                    enemy_stats["health"] -= attack
                    if enemy_stats["health"] <= 0:
                        print(f"Вы победили {enemy}! Вы получили {enemy_stats['xp']} опыта!")
                        player_xp += enemy_stats["xp"]
                        level_up()
                        break
                    
                    enemy_attack = random.randint(enemy_stats["attack_min"], enemy_stats["attack_max"])  # Враг атакует
                    print(f"{enemy} атакует вас и наносит {enemy_attack} HP урона!")
                    player_health -= enemy_attack
                    if player_health <= 0:
                        print(f"{enemy} вас победил... Игра окончена.")
                        return
                    elif action == "2" and player_potions > 0:
                        heal = random.randint(15, 30)  # Восстановление здоровья зельем
                        player_health += heal
                        player_potions -= 1
                        print(f"Вы выпили зелье и восстановили {heal} HP! У вас осталось {player_potions} зелья.")
                    else:
                        print("У вас нет зелий! Вы вынуждены сражаться!")
            return
        
        else:
            print("У вас нет зелий! Вы вынуждены сражаться!")
            return
   ###################################################################################################################
    elif choice1 == "2":
        while True:
            print("Перед вами красивый лес и вы решили отдохнуть, но уснули в лесу.")
            print("А вас поймали в плен, и вы перед вожаком. Он дает вам шанс")
            choice2 = input("Выберите (1) или (2):")

            if choice2 == "1":
                print("Сражаться в племени")
                print("Вы встретили Самого сильного человека в племени!")
                choice3 = input("Будете сражаться (1), убегать (2)? ")
                if choice3 == "1":
                    aktion =input("Вы вступаете в бой с сильным человеком в племени!(1)или(2)")
                    if aktion == "1":
                        choice4 = input("Противник хочеть ударить вас с мечом. Ваша действия (1) или (2):")
                        if choice4 =="1":
                            v1=input("Вы оборонялись с мечом и отступили.Следующий ваш шаг (1) или (2): ")
                            if v1 == "1":
                                print("Вы наносили тяжелый удар ногу противника и он принял поражение.")
                                print("Вожак убил вашего противника, а вас сделал своим помощником в племени")
                            elif v1 =="2":
                                v2=input("Противник наносил тяжелый удар в вашу руку и вам тяжело сражаться (1) или (2).")
                                if v2 == "1":
                                    print("Вы погибли сражаясь как мужчина и вожак похоронил вас достойно")
                                elif v2 =="2":
                                    print("Вы приняли поражение и вожак вас отдал тиграм в обед")
                                    # return
                           
                    elif aktion =="2":
                        choice4 = input("Противник хочеть ударить вас с мечом. Ваша действия (1) или (2):")
                        if choice4 =="1":
                            v1=input("Вы оборонялись с мечом. Ваш следющий шаг (1) или (2): ")
                            if v1 == "1":
                                n1=input("Вы наносили тяжелый удар ногу противника а он ранил вашу руку .")
                                if n1 == "1":
                                    print("Вы договаривались с противником для ничьи")
                                    print("И вас обоих отдали тиграм на обед")
                                elif n1 == "2":
                                    n2 = input("Ваш след. шаг (1) или (2)")
                                    if n2 =="1":
                                        print("Наносить удар по голове и убить противника")
                                    else:
                                        print("Вы приняли поражение и вожак вас отдал тиграм в обед")
                                        return
                elif choice3 == "2":
                    print("Умереть от страха")
                    return
            elif choice2 == "2":
                print("Стать рабом в племени")
                return
            break


                    
    else:
        print("Неверный выбор. Попробуйте снова.")
        start_game()
        
if __name__ == "__main__":
    start_game()  





        

