from aiogram.types import Message
from aiogram import Bot
import requests
async def start_command_answer(message: Message, bot: Bot):
    await message.answer("🖐 Assalomu Aleykum botimizga xush kelibsiz\nBu bot sizga uzun url larni qisqartirib beradi\n\nUrl jonating")



async def messageAnswer(message: Message, bot: Bot):
    url = message.text
    url = "https://shorturl9.p.rapidapi.com/functions/api.php"
    payload = { "url": url }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "34fe6d2e50msh7e10501cd13c417p19e723jsnc12607a15468",
        "X-RapidAPI-Host": "shorturl9.p.rapidapi.com"
    }
    response = requests.post(url, data=payload, headers=headers)
    data = response.json()
    return data['url']

    await message.answer(f"Qisqa url: {url}")