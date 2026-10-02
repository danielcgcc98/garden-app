# Get user input for season and plant type.
season = input("Enter the season: ").strip().lower()
plant_type = input("Enter the plant type: ").strip().lower()


def get_season_advice(season):
    """Return gardening advice based on the season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No advice for this season."


def get_plant_advice(plant_type):
    """Return gardening advice based on the type of plant."""
    if plant_type == "flower":
        return "Use fertilizer to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def get_watering_advice(plant_type):
    """Return watering advice based on the type of plant."""
    if plant_type == "flower":
        return "Water flowers regularly, especially during hot weather."
    elif plant_type == "vegetable":
        return "Water vegetables deeply and keep the soil consistently moist."
    else:
        return "Check the specific watering needs of your plant."


# Generate advice using the functions.
season_advice = get_season_advice(season)
plant_advice = get_plant_advice(plant_type)
watering_advice = get_watering_advice(plant_type)

# Display the gardening advice.
print(season_advice)
print(plant_advice)
print(watering_advice)