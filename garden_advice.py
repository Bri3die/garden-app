# Get season and plant type from the user instead of hardcoding values.
# This allows the program to give personalised advice each time it runs.
season = input("Enter the current season (summer/winter): ").strip().lower()
plant_type = input("Enter your plant type (flower/vegetable): ").strip().lower()

# Variable to hold the gardening advice that will be built up below
advice = ""

# Determine advice based on the season the user entered
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice available for this season.\n"

# Determine advice based on the plant type the user entered
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice available for this type of plant."

# Print the final combined advice for the user
print(advice)