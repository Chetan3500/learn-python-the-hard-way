"Use of Format string"

my_name = "Chetan"
my_age = 25
my_height = 5.9
my_weight = 74
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let talk about {my_name}.")
print(f"He's {my_height} feet tall.")
print(f"He's {my_weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"He's teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactily right
total = my_age + my_height + my_weight 
print(f"If I add {my_height}, {my_age}, and {my_weight} I get {total}.")
