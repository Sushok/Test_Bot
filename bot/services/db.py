import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / "database.db"

def init_db():
    create_subscriptions_table()
    """Инициализация базы данных и создание таблиц"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()

def add_task(user_id: int, description: str):
    """Добавить задачу в базу данных"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO tasks (user_id, description) VALUES (?, ?)
        """, (user_id, description))
        conn.commit()

def get_tasks(user_id: int):
    """Получить список задач пользователя"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id, description, created_at FROM tasks WHERE user_id = ? ORDER BY created_at DESC
        """, (user_id,))
        return cursor.fetchall()

def delete_task(task_id: int):
    """Удалить задачу по ID"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()

def create_subscriptions_table():
    """Создаёт таблицу для подписок"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                city TEXT NOT NULL,
                UNIQUE(user_id, city)
            )
        """)
    conn.close()

def add_subscription(user_id: int, city: str):
    """Добавить подписку в базу данных"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO subscriptions (user_id, city)
            VALUES (?, ?)
        """, (user_id, city))
    conn.commit()

def remove_subscription(user_id: int, city: str):
    """Удалить подписку из базы данных"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM subscriptions
            WHERE user_id = ? AND city = ?
        """, (user_id, city))
    conn.commit()

def get_subscriptions(user_id: int) -> list:
    """Получить все подписки пользователя"""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT city FROM subscriptions
            WHERE user_id = ?
        """, (user_id,))
        subscriptions = cursor.fetchall()
    return [city[0] for city in subscriptions]
