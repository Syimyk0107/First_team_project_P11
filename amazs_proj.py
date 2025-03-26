import random
import time
num = random.randint(1, 2)
print("Загрузка...")
if num == 1:
    time.sleep(2)
    print("Орел")
elif num == 2:
    time.sleep(2)
    print("Решка")