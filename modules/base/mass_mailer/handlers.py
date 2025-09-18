from aiogram import Router, types, F
from aiogram.filters import Command
from Gear.db import db
from Gear.models import User

router = Router()

@router.message(Command("broadcast"))
async def cmd_broadcast(msg: types.Message):
    # проверка что админ
    if msg.from_user.id != 123456789:  # свой id сюда
        return await msg.answer("Нет доступа")

    text = msg.get_args()
    if not text:
        return await msg.answer("Используй: /broadcast текст_сообщения")

    db.connect()
    users = User.select(User.id)
    db.close()

    count = 0
    for u in users:
        try:
            await msg.bot.send_message(u.id, text)
            count += 1
        except:
            pass

    await msg.answer(f"Рассылка завершена. Доставлено {count} сообщений.")
