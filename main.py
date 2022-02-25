import random
import time

import instabot
from itertools import groupby
from stem import Signal
from stem.control import Controller
from datetime import datetime

from work_class.get_users import get_id_user
from work_class.like_user import like_users_media

USERNAME = "lollipopstickshop"
PASSWORD = "**"
user_login = 'lhofmannita'

def main():
    bot = instabot.Bot()
    bot.login(username=USERNAME, password=PASSWORD, ask_for_code=True)

    get_id_user(bot, user_login)
    like_users_media(bot)

if __name__ == "__main__":
    main()

