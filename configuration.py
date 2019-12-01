from person import Person

camera = {
    # Device id for your camera.
    "device_id": None,
}

telegram = {
    # Telegram Bot Token, find this with BotFather
    "token": "",
}

# Names of the persons that you want to detect.
# ** YOU MUST NAME YOUR IMAGE FILES THE NAMES ENTERED HERE **
persons = [
    # Fill this with the Person object.
    Person("John", "1234567890"),
    Person("Jane", "1234567890"),
]