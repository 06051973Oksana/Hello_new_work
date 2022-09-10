# 8.Дан словарь с числовыми значениями.
# Необходимо их все перемножить и вывести на экран.
slovar = {1:2, 2:4, 3:6}
print(slovar)
# print(sum(slovar.values()))
pr = 1
for key in slovar:
    pr = pr * slovar[key]
print(pr)

