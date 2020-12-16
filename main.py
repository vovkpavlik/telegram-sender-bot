import requests
import random
from environs import Env
import pprint
env = Env()
env.read_env()

key_pixabay = env.str("API_PIXABAY")

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
    random_photos = requests.get(url, params=params)
    photo_urls = [pic["fullHDURL"] for pic in random_photos.json()["hits"]]
    return random.choice(photo_urls)


def send_photo():
    bot_url = f"https://api.telegram.org/bot{token_tg}"
    parameters = {
        "chat_id": "CHAT_ID_TG",
        "photo": get_photo_url()
    }
    photo_bot = requests.post(f"{bot_url}/sendPhoto", data=parameters)
    photo_bot.raise_for_status()
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
