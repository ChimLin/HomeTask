d1 = {"Россия":"Moscow", "Ukraina":"Kiev"}
d1["USA"] = "New yourk"
print(d1)
d1["USA"] = "New dgs"
print(d1)

del d1["USA"]
print(d1)

print(type( d1.values()))

user= set(["df","dfs","dfs"])
print(user)
user.add("Igor")
print(user)
user.remove("df")
print(user)
user2 = user.copy()
user3 = user.union(user2)
print(user3)

from array import *
arr = array('i',[1,2,3,4,5])
arr.insert(0,-1)
arr.append(9)
arr[1] = 87
arr.extend([345,78])
arr.pop(3)
print(arr)
print(arr[1:4:5])

for x in arr:
    print(x)

#test decima

from decimal import Decimal
x = Decimal("0.1")
x = x + x + x
print(x)

y = Decimal("0.555")
y = y.quantize(Decimal("1.000"))
print(y)

