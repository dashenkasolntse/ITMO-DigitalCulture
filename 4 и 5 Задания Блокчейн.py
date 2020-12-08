#Задание 4
a = 281
c = 624
d = 970

#Задание 5
one = "43c727ee4fc7250574d2ef90cfa16626388a10e1b30d36ece1c272953ad2ed9e"     # в "..." вставляем hash, который уже дан по заданию
two = 723     # пишим число, которое дано по заданию




# Ничего не тронгай ниже
import hashlib
x = 1
b = 1
print("Задание 4:")
o = str(hashlib.sha256(str(a).encode()).hexdigest())
print("1:",o)
h = o + str(hashlib.sha256(str(c).encode()).hexdigest())
o = str(hashlib.sha256(str(h).encode()).hexdigest())
print("2:",o)
j = o + str(hashlib.sha256(str(d).encode()).hexdigest())
o = str(hashlib.sha256(str(j).encode()).hexdigest())
print("3:",o)
two1 = hashlib.sha256(str(two).encode()).hexdigest()
string = one + two1
while x != 1001:
    s = hashlib.sha256(str(b).encode()).hexdigest()
    gg = string
    gg += s
    gg = hashlib.sha256(str(gg).encode()).hexdigest()
    if gg[:2] == "00":
        i = gg
    x += 1
    b += 1
print()
print("Задание 5:")
print("Пишешь в ответ:", i)
