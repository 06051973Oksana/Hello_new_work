# 6.Даны два списка чисел.
# Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
sp1 = 1,4,5,66,3,4
sp2 = 22,4,5,76,8
# print('l sp1:  ',len(sp1),'\n l sp2:  ', len(sp2))
set1 = set(sp1) # перевели во множество
set2 = set(sp2)
intersection = set1.intersection(set2) # количество пересечений в обоих множествах
print(len(intersection)) # вывести сколько раз встречались одинаковые цифры в обоих множествах