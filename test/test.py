import instabot
from itertools import groupby
from stem import Signal
from stem.control import Controller
from datetime import datetime
import random
import time
import json
import os

USERNAME = "lollipopstickshop"
PASSWORD = "vpluskravnolove"

bot = instabot.Bot()
bot.login(username=USERNAME, password=PASSWORD, ask_for_code=True)

user = 'theviniand'
user_id = bot.get_user_id_from_username(user)

all_media = bot.get_total_user_medias(
    user_id)
last_media = all_media[random.randint(0, 2)]
bot.like_medias(last_media)
#bot.like_user(last_media, filtration=False)