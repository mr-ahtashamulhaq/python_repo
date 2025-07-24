# Create a dictionary named person with keys: "name", "age", and "city" and assign your own values.

person={"name":"ahtasham","age":18,"city":"Lahore"}

#print the value of "city" using: [] notation & .get() method
print(person["city"])
print(person.get("city"))

# add a new key "email" with some value to the person dictionary.
person["email"]="ahtasham@gmail.com"
print(person.items())
print("\n")
# Change the "age" value in the dictionary to a new number.
person["age"]=20
print(person.items())
