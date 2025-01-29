from aiogram import Router, types
from aiogram.filters import Command
from bot.services.weather_api import fetch_weather

router = Router()

@router.message(Command(commands=["weather"]))
async def weather_command(message: types.Message):
    """Показать погоду"""
    try:
        city = message.text.split(maxsplit=1)[1]
        weather_data = await fetch_weather(city)
        if "error" in weather_data:
            await message.reply(weather_data["error"])
        else:
            city_name = weather_data["name"]
            temp = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            await message.reply(f"Погода в {city_name}:\n{description.capitalize()}, {temp}°C")
    except IndexError:
        await message.reply("Укажите название города. Пример: /weather Киев")
    except Exception as e:
        await message.reply(f"Произошла ошибка: {str(e)}")
