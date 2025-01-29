from aiogram import Router, types
from aiogram.filters import Command
from bot.services.db import add_task, get_tasks, delete_task

router = Router()

@router.message(Command(commands=["add"]))
async def add_task_command(message: types.Message):
    """Добавить задачу"""
    description = message.text.split(maxsplit=1)[-1]
    if not description:
        await message.reply("Пожалуйста, укажите описание задачи. Пример: /add Купить молоко")
        return
    add_task(message.from_user.id, description)
    await message.reply("Задача добавлена!")

@router.message(Command(commands=["list"]))
async def list_tasks_command(message: types.Message):
    """Показать список задач"""
    tasks = get_tasks(message.from_user.id)
    if not tasks:
        await message.reply("У вас пока нет задач.")
        return

    tasks_list = "\n".join([f"{task[0]}. {task[1]} (Создано: {task[2]})" for task in tasks])
    await message.reply(f"Ваши задачи:\n{tasks_list}")

@router.message(Command(commands=["delete"]))
async def delete_task_command(message: types.Message):
    """Удалить задачу"""
    try:
        task_id = int(message.text.split(maxsplit=1)[-1])
        delete_task(task_id)
        await message.reply("Задача удалена!")
    except (ValueError, IndexError):
        await message.reply("Пожалуйста, укажите ID задачи для удаления. Пример: /delete 1")
