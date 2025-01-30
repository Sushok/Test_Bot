from aiogram import Router, types
from aiogram.filters import Command 
from bot.services.db import add_user, get_username_by_id
import re

router = Router()

@router.message(Command(commands=["start"]))
async def start_command(message: types.Message):
    user = message.from_user
    user_name = get_username_by_id(user.id)
    if user_name is None:
        add_user(
            user_id = user.id,
            username = user.username,
            name = user.first_name,
            surname = user.last_name     
        )
        await message.reply("Привет! Я бот для управления задачами..")
    else: 
        surname, name = user_name
        await message.reply(f"Привет, {re.sub(r'[^a-zA-Zа-яА-ЯёЁ\s]', '', name)} {re.sub(r'[^a-zA-Zа-яА-ЯёЁ\s]', '', surname)}! Я тебя помню!")


@router.message(Command(commands=["help"]))
async def help_command(message: types.Message):
    await message.reply("Доступные команды:\n
/start - знакомство с ботом\n
/help - справка по командам\n
/add- /add Задача1 и название задачи добавляет задачу\n
/subscribe - подписка на уведомления \n
/list - список задач\n
/delete - /delete 1 и номер задачи которую нужно удалить \n
/weather - /weather Киев погода в указанном городе\n
/unsubscribe - отписка от уведомлений\n
/subscriptions - список подписок\n")
