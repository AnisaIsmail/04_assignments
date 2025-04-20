earth_weight = float(input("Enter a weight on Earth: "))

# Mars ka weight calculate karna
mars_weight = earth_weight * 0.378

# Result round karna 2 decimal tak
rounded_weight = round(mars_weight, 2)

# Print result
print("The equivalent on Mars:", rounded_weight)
