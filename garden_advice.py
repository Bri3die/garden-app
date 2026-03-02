"""
garden_advice.py

A simple gardening advice app that gives personalised tips
based on the current season and the type of plant the user is growing.
"""


def get_season_advice(season):
    """
    Return gardening advice based on the current season.

    Args:
        season: The current season.

    Returns:
        str: Advice relevant to that season.
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice available for this season.\n"


def get_plant_advice(plant_type):
    """
    Return gardening advice based on the type of plant.

    Args:
        plant_type: The type of plant.

    Returns:
        str: Advice relevant to that plant type.
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice available for this type of plant."


def main():
    """
    Main function — collects user input, builds advice, and prints it.
    """
    season = input("Enter the current season (summer/winter): ").strip().lower()
    plant_type = input("Enter your plant type (flower/vegetable): ").strip().lower()

    advice = get_season_advice(season) + get_plant_advice(plant_type)

    print(advice)


if __name__ == "__main__":
    main()