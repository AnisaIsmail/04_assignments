earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

# Gravity multipliers
if planet == "Mercury":
    multiplier = 0.376
elif planet == "Venus":
    multiplier = 0.889
elif planet == "Mars":
    multiplier = 0.378
elif planet == "Jupiter":
    multiplier = 2.36
elif planet == "Saturn":
    multiplier = 1.081
elif planet == "Uranus":
    multiplier = 0.815
elif planet == "Neptune":
    multiplier = 1.14
else:
    print("Invalid planet name! Please enter a valid planet.")
    exit()  

planet_weight = earth_weight * multiplier

print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")