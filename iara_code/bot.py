"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

import microphone_recognition

from config import Config

API_TOKEN = Config.bot_api.rstrip("\n")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    #await message.answer(message.text)
    res = microphone_recognition.Faz(message.text.lower())
    await message.answer(res)

def Start():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    #executor.start_polling(dp, skip_updates=True)
    Start()