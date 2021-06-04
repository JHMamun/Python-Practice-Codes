name = " "
if not name.strip():
    print("Name is empty")

age = 22
if age >= 18 and age < 64:
    print("Eligible")

# Another way of writing compount conditions
if 18 <= age < 65:
    print("Eligible")
