from functools import reduce
import operator

l = []
for i in range(6):
    a = int(input("Enter a numer"))
    l.append(a)

print(l)

m = [x*3 for x in l]

print(m)

print("Sum of original list: ", reduce(lambda a, b: a+b, l))
print("Sum of new list: ", reduce(lambda a, b: a+b, m))
