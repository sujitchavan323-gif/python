

# Input
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))

# Current year
current_year = 2026

# Calculate age
age = current_year - year_of_birth

# Check senior citizen
if age >= 60:
    print(name, "is a Senior Citizen.")
else:
    print(name, "is not a Senior Citizen.")

# Display age
print("Age:", age)