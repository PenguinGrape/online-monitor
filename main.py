import time
import json
import telebot
from telethon.sync import TelegramClient
from telethon import functions, types


if __name__ == '__main__':
    with open("config.json", "r") as tmp:
        config = json.load(tmp)
        api_id, api_hash, bot, uid, me = config["api_id"], config["api_hash"], telebot.TeleBot(config['token']), config[
            'user_id'], config['send_to_id']
        client = TelegramClient('Monitor', api_id, api_hash)
        client.start()
    last = None
    try:
        while True:
            result = client(functions.contacts.GetStatusesRequest())
            for x in result:
                if x.user_id == uid:
                    if type(x.status) == types.UserStatusOnline:
                        current = True
                        if last != current:
                            bot.send_message(me, "Went online!")
                    else:
                        current = False
                        if last != current:
                            bot.send_message(me, "Went offline!")
                    last = current
            time.sleep(1)
    except KeyboardInterrupt:
        print("Got KeyboardInterrupt. Exiting...")
        exit(0)
