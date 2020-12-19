import json
import os
import time

import random
urls = os.path.join('../users.json')

with open(urls, 'r', encoding='utf-8') as f:
    text = json.load(f)

for user_id in text:
    t = random.randint(160, 420)
    print(user_id)
    print(t)
    time.sleep(t)