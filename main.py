import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

TOKEN = "7792197713:AAHWld468uMzSG0bPWHyC6AF_Dhes1DzCeo"  # Замените на ваш токен

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть mini-app", web_app=types.WebAppInfo(url="https://prostoyy2008.github.io/BotMiniAApp/"))]
        ]
    )
    await message.answer("Добрый!", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
