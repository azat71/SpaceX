# Задание 4:
    # Вам даны несколько последовательностей чисел:
    # sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
    # sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
    # sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
    # sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')

    # Нужно проверить, все ли числа в КАЖДОЙ последовательности уникальны.
    # Если в последовательности были найдены дубликаты ---> Выведите на экран: "Последовательность не уникальна."
    # Если в последовательности дубликатов найдено не было ---> Выведите на экран: "Последовательность уникальна."
    # Если в решении задания не присутствует цикл ---> Задание не защитано.
    #=============================================================================================================
# a = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
# b = (14,10,35,45,'60',70,90,0,105,150,'70')
# c = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
# d = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')

# q = set(a)
# for i in q:
#     if len(a) == len(q):
#         print("Последовательность уникальна.")
#         break
#     else:
#         print("Последовательность не уникальна")
#         break

# w = set(b)
# for i in w:
#     if len(b) == len(w):
#         print("Последовательность уникальна.")
#         break
#     else:
#         print("Последовательность не уникальна")
#         break

# e = set(c)
# for i in e:
#     if len(c) == len(e):
#         print("Последовательность уникальна.")
#         break
#     else:
#         print("Последовательность не уникальна")
#         break

# r = set(d)
# for i in r:
#     if len(d) == len(r):
#         print("Последовательность уникальна.")
#         break
#     else:
#         print("Последовательность не уникальна")
#         break