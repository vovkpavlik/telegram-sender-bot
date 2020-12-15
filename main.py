import requests
import random
from environs import Env

env = Env()
env.read_env()

KEY = env.str("API_PIXABAY")


def get_photo_url():
    category = ["sportcars",
            "animals",
            "space",
            "ships",
            "planes",
            "girls",
            "summer",
            "winter",
            "buildings",
            "russia",
            "bears"
            ]
    random_category = random.choice(category)
    params = {
        "key": KEY,
        "category": random_category,
        # "image_type": "photo",
        # "editor_choice": "TRUE",
    }
    url = "https://pixabay.com/api/"
    random_photo = requests.get(url, params=params)
    return random_photo.json()["hits"][1]["largeImageURL"]


file_name = "random picture.jpg"
response = requests.get(get_photo_url())
with open(file_name, "wb") as file:
    file.write(response.content)

print(get_photo_url())

