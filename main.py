#1 - misol
roy = [2, 8, 4, 9, 2]
res = list(map(lambda son: son ** 2, roy))
print(res)

#2 - misol
roy_1 = [1, 2, 3]
roy_2 = [4, 5, 5]
res2 = list(map(lambda a, b: a+b, roy_1, roy_2))
print(res2)

#3 - misol
roy3 = ["tom", 'bob', 'ella']
res3 = list(map(lambda soz: soz.title(), roy3))
print(res3)

#4 - misol
roy4 = [2, 8, 4, 9, 2]
res4 = list(filter(lambda son: son % 2 == 0, roy4))
print(res4)

#5 - misol
roy5 = ["tombel", 'bob', 'ellaxon']
res5 = list(map(lambda soz: len(soz) > 5, roy5))
print(res5)

#6 - misol
roy6 = [2, 8, 4, 9, 2]
res6 = list(filter(lambda son: son % 3 == 1, roy6))
print(res6)

#7 - misol
roy7 = []
res7 = list(map(lambda son: son * 2 if son *2 < 10 else son / 10, roy7))
print(res7)

