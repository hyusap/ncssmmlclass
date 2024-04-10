limit = 1e-6
x = 1.5
last_x = 0
while abs(x - last_x) > limit:
    last_x = x
    x = x - (x**2 - 2) / (2 * x)
print(x)
