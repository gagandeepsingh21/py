myset=set()

myset.add(1)
myset.add(2)
myset.add(2)
myset.add(4)
print(myset)

myset.remove(1)
print(myset)

myset.add(5)
myset.add(6)
myset.add(7)
myset.add(8)
print(myset)
print(f"The length of the set is {len(myset)}")
