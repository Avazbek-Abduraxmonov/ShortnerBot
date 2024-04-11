from aiogram import Bot, Dispatcher, F
from asyncio import run
from aiogram.types import BotCommand
from config import token, admin_id
from function import *
dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(admin_id, 'Bot ishga tushdi ✅')

async def shutdown_answer(bot: Bot):
    await bot.send_message(admin_id, 'Bot ishdan toxtadi')


async def start():
    dp.startup.register(startup_answer)

    dp.message.register(start_command_answer)
    dp.message.register(messageAnswer)

    dp.shutdown.register(shutdown_answer)

    bot = Bot(token=token)

    await bot.set_my_commands([
    BotCommand(command='start', description='Botni ishga tushurish')    
    ])


    await dp.start_polling(bot, polling_timeout=1)

run(start())