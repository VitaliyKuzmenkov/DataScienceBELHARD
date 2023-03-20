import random
# lst = [random.randint(0,100) for i in range(20)]
# s = sum(lst)
# n = len(lst)
# sr = s/n
#
# print(lst)
# print(len(lst))
# print(sr)
#
# lst1 = [random.randint(-8,10) for i in range(10)]
#
# print(lst1)

lst2 = [random.randint(-8,10) for i in range(15)]

print(lst2)
#
# set1 = set(lst1)
# set2 = set(lst2)
# set3 = list(set1.symmetric_difference(set2))
# print(set3)
# print(sorted(list(set3),reverse=True))

m = min(lst2)
ind = lst2.index(m)
del lst2[:ind]
print(lst2)

# lst3 = [random.randint(-10,10) for i in range(10)]
# print(lst3)
# print(sorted(lst3, reverse=True))

# a = "aassshhhddd"
#
# s = set(a)
#
# print(s, len(s))
