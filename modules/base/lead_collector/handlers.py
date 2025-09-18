from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("lead"))
async def cmd_lead(msg: types.Message):
    await msg.answer("Введите ваш email для связи:")

@router.message()
async def collect_lead(msg: types.Message):
    email = msg.text
    # Здесь должен быть вызов Google Sheets API (сервисный аккаунт)
    # но для простоты пока просто вывод
    await msg.answer(f"Спасибо! Ваш email сохранён: {email}")
