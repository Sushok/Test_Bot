from aiogram import Router, types
from aiogram.filters import Command
from bot.services.db import add_subscription, remove_subscription, get_subscriptions

router = Router()

@router.message(Command(commands=["subscribe"]))
async def subscribe_command(message: types.Message):
    """Подписка на уведомления"""
    try:
        city = message.text.split(maxsplit=1)[1]
        add_subscription(message.from_user.id, city)
        await message.reply(f"Вы подписались на уведомления о погоде в городе {city}.")
    except IndexError:
        await message.reply("Укажите название города. Пример: /subscribe Киев")
    except Exception as e:
        await message.reply(f"Произошла ошибка: {str(e)}")

@router.message(Command(commands=["unsubscribe"]))
async def unsubscribe_command(message: types.Message):
    """Отписка от уведомлений"""
    try:
        city = message.text.split(maxsplit=1)[1]
        remove_subscription(message.from_user.id, city)
        await message.reply(f"Вы отписались от уведомлений о погоде в городе {city}.")
    except IndexError:
        await message.reply("Укажите название города. Пример: /unsubscribe Киев")
    except Exception as e:
        await message.reply(f"Произошла ошибка: {str(e)}")

@router.message(Command(commands=["subscriptions"]))
async def subscriptions_command(message: types.Message):
    """Список подписок"""
    subscriptions = get_subscriptions(message.from_user.id)
    if subscriptions:
        await message.reply("Ваши подписки:\n" + "\n".join(subscriptions))
    else:
        await message.reply("У вас пока нет подписок.")
