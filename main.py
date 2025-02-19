import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7792197713:AAHWld468uMzSG0bPWHyC6AF_Dhes1DzCeo"  # Замените на ваш токен бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Открыть Mini-App", web_app=InlineKeyboardButton.WebAppInfo("https://prostoyy2008.github.io/BotMiniAApp/"))
    keyboard.add(button)
    
    bot.send_message(message.chat.id, "Добрый!", reply_markup=keyboard)

if __name__ == "__main__":
    bot.polling(none_stop=True)
