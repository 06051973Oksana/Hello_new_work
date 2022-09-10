# Создать кортеж с числами от 1 до 50 используя генератор списков
import random

kort = tuple(random.randint(1,50) for a in range(7))
print(kort)