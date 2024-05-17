import math

X = 0.5  
N = 5  

total = 0

for i in range(1, N + 1):
    term = (-1) ** (i - 1) * (X ** i) / i
    total += term

ln_approx = total
print("Approximate value of ln(1 + X):", ln_approx)

ln_actual = math.log(1 + X)
print("Actual value of ln(1 + X):", ln_actual)
