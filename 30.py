num = 345

if 0 < num < 10:
    num_digits = 1
elif 9 < num < 100:
    num_digits = 2
else:
    num_digits = 3

is_even = num % 2 == 0

if num_digits == 1:
    description = "one-digit"
elif num_digits == 2:
    description = "two-digit"
else:
    description = "three-digit"

if is_even:
    description += " even number"
else:
    description += " odd number"

print("Description:", description)
