tolerance = 1e-6
sum = 0
denominator = 1
direction = 1
n = 0
while (1 / denominator) > tolerance:
    sum += 1 / denominator * direction
    denominator += 2
    direction *= -1
    n += 1
print(sum * 4, n)
