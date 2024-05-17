price_per_kg = 5.75 

for weight in range(12, 21, 2):
    weight_in_kg = weight / 10
    cost = price_per_kg * weight_in_kg
    print(f"Cost of {weight_in_kg} kg of sweets: ${cost:.2f}")
