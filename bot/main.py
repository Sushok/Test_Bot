import asyncio
from aiogram import Bot, Dispatcher
from bot.config import BOT_TOKEN
from bot.handlers import base, tasks
from bot.services.db import init_db
from bot.handlers import base, tasks, weather, subscriptions

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def main():
    init_db()

    dp.include_router(base.router)
    dp.include_router(tasks.router)
    dp.include_router(weather.router)
    dp.include_router(subscriptions.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
