#  4.
# a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# print(a[4::-2])   # ['quux', 'baz', 'foo']
# print(a[:])    #is a True
# print(a[-5:-3])  #['bar', 'baz']

# 5.  [1, 2, 4, 5]
# a = [1, 2, 3, 4, 5]
# del a[2]
# print(a)
# a.remove(3)
# print(a)

# 6.
# t = ('foo', 'bar', 'baz')
# print(t[1])

# 11.
# c = tuple('absbd')
# print(c)
# b = ['c','v','h']
# d = tuple(b)
# # print(d)
# e = tuple(tuple(d))
# print(e)

# 12.
# a = (1,2,3)
# b = [4,5,6]
# c = 2
# d = (a+tuple(b))*c
# print(d)

#  15
# d = {'foo':1, 'bar':2, 'baz':3}
# print(d)
# del d['baz']
# print(d)

#  16 Какой результат будет у d['bar':'baz']
# d = {'foo': 100, 'bar': 200, 'baz': 300}
# print(d['bar':'baz'])

# 17.
# x = ['a','b',{'foo':1,
#               'bar':{'x':10, 'y':20, 'z':30},
#               'baz':3},
#      'c','d']
# print(x)
# print(x[2]["bar"]["z"])

# 18
d = {'цвет': 'синий',  'фрукт':  'яьлоко', 'животное': 'собака'}
# # for key in d:  # перебрать ключи в d
# #     print(key)
#
# # 19
# b = d.items()
# print(b)

# print(d.keys())

#  23
# a = [1,2,3,4,5,6,1,2,3,4,5,6]
# x = len(set(a)) # посчитает кол-во элем во множестве, будет 6, т.к. не должны повторятся
# print(x)