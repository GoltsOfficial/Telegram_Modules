from aiogram import Router, types
from aiogram.filters import Command

router = Router()

catalog = {
    "item1": {"title": "Товар 1", "price": 100},
    "item2": {"title": "Товар 2", "price": 250},
}

@router.message(Command("shop"))
async def cmd_shop(msg: types.Message):
    kb = types.InlineKeyboardMarkup()
    for k, v in catalog.items():
        kb.add(types.InlineKeyboardButton(text=f"{v['title']} - {v['price']} ₽", callback_data=f"buy:{k}"))
    await msg.answer("Выберите товар:", reply_markup=kb)

@router.callback_query()
async def process_buy(call: types.CallbackQuery):
    if call.data.startswith("buy:"):
        key = call.data.split(":")[1]
        item = catalog[key]
        await call.message.answer(f"Вы выбрали {item['title']} за {item['price']} ₽.\nПереход к оплате...")
        await call.answer()
