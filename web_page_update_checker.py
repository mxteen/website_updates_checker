import hashlib
import time
import datetime
from random import randint
import json
import requests

# Min and max wait time between checks (in seconds)
min_wait_time, max_wait_time = 3000, 4200

# Reading url, telegram-bot token and telegram chat id
with open('credentials.json') as f:
    json_str = f.read()   
credentials = json.loads(json_str)
token = credentials['token']
chat_id = credentials['chat_id']
url = credentials['url_to_check']

# Initail conditions
i = 0  # Counter of checks
wait_time = (min_wait_time + max_wait_time) / 2  # Wait time between checks, s
response = requests.get(url)  # Retrieve the website content
current_hash = hashlib.sha256(response.content).hexdigest() # Hash the content
print(current_hash, '\n')
time.sleep(wait_time)  # Pause before a checking loop starts

while True:
    # Retrieve the website content
    response = requests.get(url)

    # Hash the website content using SHA256
    new_hash = hashlib.sha256(response.content).hexdigest()

    # Setting the next random pause between checks
    wait_time = randint(min_wait_time, max_wait_time)

    # Printing out the status messages: number, time of checks and a hash
    i += 1
    status = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + \
             ' Проверка {}, hash: {}'.format(i, new_hash)
    print(status)

    # Compare the new hash with the old hash
    if new_hash != current_hash:
        # If the hashes are different, update the old hash and send a notification
        current_hash = new_hash
        message = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + \
                  ' Сайт {} обновлён. Было проверок: {}.'.format(url, i)
        url_telegram = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url_telegram).json()) # this sends the message
        print(message)
        break  # this can be deleted if we want to have an infinite checking loop
    else:
        # If the hashes are the same, wait for the specified time before checking again
        time.sleep(wait_time)
