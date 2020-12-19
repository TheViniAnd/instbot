import instabot
import json
import os


def get_id_user(bot, user):
    print('Начал получать айди пользователей')
    try:
        result = bot.get_user_followers(user)
    except ConnectionError as e:
        print('Ошибка подключения:\n', e)

    urls = os.path.join('users.json')

    with open(urls, 'w', encoding='utf-8') as outfile:
        json.dump(result, outfile, ensure_ascii=False, indent=4)

