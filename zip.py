x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = ['a', 'b', 'c', 'd']

for a, b in zip(x, y):
    print(a, b)


for a, b, c in zip(x, y, z):
    print(list(zip(x, y, z)))


[print(x, y, z) for x, y, z in zip(x, y, z)]
print(x)
