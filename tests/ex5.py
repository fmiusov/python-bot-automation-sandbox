name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cent_height = 74 * 2.54
metric_weight = float(180 * 0.45359237)

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall, which is {cent_height} in centimeters.")
print(f"He's {weight} pounds heavy, which is {metric_weight} in kilograms.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
metric_total = float(age + cent_height + metric_weight)
print(f"If I add {age}, {height}, and {weight} I get {total}, or {metric_total}.")

