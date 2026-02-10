x = [2, 8, 9, 48, 8, 22, -12, 2]
y = set()

for num in x:
    if num > 5:
        z = num + 2
        y.add(z)

print(x)
print(y)