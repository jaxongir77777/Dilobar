string = "Hello World" 

capital_count = 0

for char in string:
    if 'A' <= char <= 'Z':
        capital_count += 1

print("Amount of Latin capital letters:", capital_count)
