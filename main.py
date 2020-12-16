import requests
import random
from environs import Env


def get_photo_url():
    tag = ["sportcars",
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
    random_tag = random.choice(tag)
    params = {
        "key": key_pixabay,
        "q": random_tag,
    }
    url = "https://pixabay.com/api/"
    random_photo = requests.get(url, params=params)
    return random_photo.json()["hits"][1]["fullHDURL"]


def send_photo():
    bot_url = f"https://api.telegram.org/bot{token_tg}"
    parameters = {
        "chat_id": "672168284",
        "photo": get_photo_url()
    }
    photo_bot = requests.post(f"{bot_url}/sendPhoto", data=parameters)
    return photo_bot


if __name__ == "__main__":
    env = Env()
    env.read_env()

    key_pixabay = env.str("API_PIXABAY")
    token_tg = env.str("TOKEN_TG")

    try:
        send_photo()
    except KeyError:
        print("Непредвиденная ошибка")
