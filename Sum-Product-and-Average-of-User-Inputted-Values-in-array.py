T = [0.0] * 10
total = 0.0
product = 1.0

for i in range(10):
    T[i] = float(input(f"Enter a real number for position {i + 1}: "))
    total += T[i]
    product *= T[i]

avg = total / 10

print("Sum of the numbers:", total)
print("Product of the numbers:", product)
print("Average of the numbers:", avg)
