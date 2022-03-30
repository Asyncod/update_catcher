# -*- coding: utf-8 -*-
from json import loads
from time import sleep
import requests



id_group = "" # your ID or group ID (with -)
token = "" # Bot's token from @BotFather
chat_id_list = ["956692649430093904", "950849051358822431", "946124073400938497"] # Aptos's channel ID
ds_token = "" # Discord from your acc



# TEST RESPONSE
def test_inp():
    try:
        msg = "*Запуск бота для получения обновлений Aptos*"
        url = f"chat_id={id_group}&text={msg}&parse_mode=markdown"
        requests.get(f"https://api.telegram.org/bot{token}/sendMessage", url)
    except:
        sleep(300)


# SESSION FOR REQUESTS
def session_create():
    session = requests.Session()
    session.headers['Authorization'] = ds_token
    # Use another user agent or leave this one
    session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.1.932 Yowser/2.5 Safari/537.36"

    return session


# CHECK BOT'S WORKING
def check_work():
    try:
        msg = "*Бот работает*"
        url = f"chat_id={id_group}&text={msg}&parse_mode=markdown"
        requests.get(f"https://api.telegram.org/bot{token}/sendMessage", url)
    except:
        sleep(300)


def sender_info(msg):
    try:
        # If you receive updates in a chat with several people,
        # then just add their ID to the message.
        # Don't forget to escape "_"
        msg = f"{msg}\n\n@asynco @Timq\_nnm"
        url = f"chat_id={id_group}&text={msg}&parse_mode=markdown"
        requests.get(f"https://api.telegram.org/bot{token}/sendMessage", url)
    except:
        sleep(300)


# CHECK APTOS'S UPDATE
def check_news():
    test_inp()
    session = session_create()
    last_id = []

    while True:
        for link in chat_id_list:
            mess = loads(session.get(f'https://discord.com/api/v9/channels/{link}/messages?limit=1').text) # get bebra
            
            if mess[0]["id"] not in last_id:
                last_id.append(mess[0]["id"])
                sender_info(mess[0]["content"])
                print(mess[0]["content"])
            else:
                pass # ID already in list

            sleep(3)

        sleep(3669) # Time for sleep (this 1 hour, use another time or leave this)
        check_work()


if __name__ == '__main__':
    print("Bot work")
    check_news()
