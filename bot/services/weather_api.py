import aiohttp
import os
from dotenv import load_dotenv

# Загрузка переменных из .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

async def fetch_weather(city: str) -> dict:
    """Получить прогноз погоды для города"""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as response:
            if response.status == 200:
                return await response.json()
            else:
                return {"error": f"Ошибка: {response.status}"}
