#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 3082893, #get it from https://my.telegram.org/auth
    api_hash="5850a6f672ab5bdb1467f9c57bd1d46f", #get it from https://my.telegram.org/auth
    bot_token="2132905159:AAHlzp4H2O5oNA_S-k7wrqKUFb3TYRUZZs4", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
    