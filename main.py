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
            "bears"]
    random_tag = random.choice(tag)
    parameters = {
        "key": key_pixabay,
        "q": random_tag,
    }
    url = "https://pixabay.com/api/"
    random_photos = requests.get(url, params=parameters)
    photo_urls = [pic["fullHDURL"] for pic in random_photos.json()["hits"]]
    random_photos.raise_for_status()
    return random.choice(photo_urls)


def send_photo():
    bot_url = f"https://api.telegram.org/bot{token_tg}"
    parameters = {
        "chat_id": chat_id_tg,
        "photo": get_photo_url()
    }
    response = requests.post(f"{bot_url}/sendPhoto", data=parameters)
    response.raise_for_status()
    return response


if __name__ == "__main__":
    env = Env()
    env.read_env()

    key_pixabay = env.str("API_PIXABAY")
    token_tg = env.str("TOKEN_TG")
    chat_id_tg = env.str("CHAT_ID_TG")

    try:
        send_photo()
    except requests.exceptions.HTTPError as err:
        print(err)
