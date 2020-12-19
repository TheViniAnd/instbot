import instabot
import json
import os
import time
import random


def like_users_media(bot):
    with open('users.json', 'r', encoding='utf-8') as f:
        text = json.load(f)

    for user_id in text:
        try:
            all_media = bot.get_total_user_medias(
                user_id)
            try:
                last_media = all_media[random.randint(0, 2)]
                bot.like_medias(last_media)
                print('Лайкнул пользователя')
            except:
                print('Нет медия файлов')
        except:
            print('Ошибка, пока неизвестная')
        time.sleep(random.randint(160, 360))