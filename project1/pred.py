x0 = 2367.299385482273
x1 = 1.1644757731346644
xsqrt = -104.77016426573157

x = int(input("Enter a year: "))

y = x0 + x1 * x + xsqrt * x**0.5
print(f"Estimated time: {y} seconds")
