# -*- coding: utf-8 -*-
from json import loads
from time import sleep
import requests


# id_group = "-1001447252368"
id_group = "1095119526"
# token = "5273864774:AAH-0ABpnglxbn8VyJqoM9rhBOatU3_kwD4"
token = "1720011320:AAGI5SUo0AbwynunYicPJnpSff2o4Kjj81U"
# chat_id_list = ["956692649430093904", "950849051358822431", "946124073400938497"]
chat_id_list = ["958348625451307051", "958390758979821628"]



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
    session.headers['Authorization'] = "OTM1ODI3NzE4NTY0NjE0MTU1.YkMBhw.dIDROR-adrSV_zrj57mRy4T-5ro"
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
        msg = f"{msg}\n\n@asynco @jjouwie @Timq\_nnm @Portal286 @crinzhlove @kurilshik282 @jokilom @NeznaykoNn @iarsikk"
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
            mess = loads(session.get(f'https://discord.com/api/v9/channels/{link}/messages?limit=1').text)

            if mess[0]["id"] not in last_id:
                last_id.append(mess[0]["id"])
                sender_info(mess[0]["content"])
                print(mess[0]["content"])
            else:
                pass # ID already in list

            sleep(3)

        sleep(3669)
        check_work()


if __name__ == '__main__':
    print("Bot work")
    check_news()
