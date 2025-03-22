# marsweight.py

# Prompt the user to enter their weight on Earth
earth_weight = float(input("Enter a weight on Earth: "))

# Calculate the equivalent weight on Mars (37.8% of Earth weight)
mars_weight = round(earth_weight * 0.378, 2)

# Print the result
print(f"The equivalent on Mars: {mars_weight}")

# planetaryweight.py

# Dictionary containing planet gravity factors relative to Earth
gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Prompt the user to enter their weight on Earth
earth_weight = float(input("Enter a weight on Earth: "))

# Prompt the user to enter a planet name
planet = input("Enter a planet: ")

# Calculate the equivalent weight on the chosen planet
if planet in gravity_factors:
    planetary_weight = round(earth_weight * gravity_factors[planet], 2)
    print(f"The equivalent weight on {planet}: {planetary_weight}")
else:
    print("Invalid planet name. Please enter a valid planet from the list.")

