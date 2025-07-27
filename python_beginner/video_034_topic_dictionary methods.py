# Create a dictionary car = {"brand": "Toyota", "year": 2020} Use get() to access "brand" Use get() to access "model" (which doesn’t exist)
car = {"brand": "Toyota", "year": 2020}
print(car.get("brand"))
print(car.get("model"))

# From the dictionary, print all the keys and values.
print(f"keys are {car.keys()}")
print(f"\nvalues are {car.values()}")

# Update the "year" to 2023 Add a new key "color" with value "Red"
car.update({"year":2023,"color":"Red"})

# Print all key-value pairs
print("\n")
print(car.items())

# Remove the "brand" key from the dictionary and print the removed value.
temp=car.pop("brand")
print("\n")
print(f"Removed Value is {temp}")
print("updated items are:",car.items())

# Clear the dictionary and print it to confirm it’s empty.
car.clear()
print("\n")
print(car)