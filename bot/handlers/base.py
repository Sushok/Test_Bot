from aiogram import Router, types
from aiogram.filters import Command 

router = Router()

@router.message(Command(commands=["start"]))
async def start_command(message: types.Message):
    await message.reply("Привет! Я бот для управления задачами.")

@router.message(Command(commands=["help"]))
async def help_command(message: types.Message):
    await message.reply("Доступные команды:\n/start - начать работу\n/help - помощь")
