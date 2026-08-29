from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    CommandHandler, 
    Application,
    MessageHandler,
    filters,
)
from config import TOKEN

async def unknown_command(update, context):
    await update.message.reply_text('Данную команду пока наш бот не знает(')

async def menu_command(update, context):
    with open("menu.jpg", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption="Вот наше меню" 
        )

async def start(update, context):
    keyboard = [
        ["🍽 Меню"],
        ["📍 Адрес", "📞 Контакты"]
    ]
    menu_keyboard = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
    await update.message.reply_text(
        'Привет, Никита! Добро пожаловать в ресторан.',
        reply_markup=menu_keyboard
    )
async def help_command(update, context):
    await update.message.reply_text(
        "Доступные команды:\n/start — открыть главное меню\n/menu — посмотреть меню\n/help — получить помощь"
    )
async def handle_text(update, context):
    text = update.message.text.strip().lower()
    if text == "привет":
        await update.message.reply_text("Привет, гость!")
    elif text in ("меню", "🍽 меню"):
        await menu_command(update, context)
    elif text in ("адрес", "📍 адрес"):
        await update.message.reply_text("Данные ресторана пока еще уточняются")
    elif text in ("контакты", "📞 контакты"):
        await update.message.reply_text("Данные ресторана пока еще уточняются")
    else:
        await update.message.reply_text("Я пока не понимаю это сообщение. Напиши 'меню'")

application_builder = Application.builder()


start_handler = CommandHandler("start", start)
menu_handler = CommandHandler("menu", menu_command)
help_handler = CommandHandler("help", help_command)
unknown_handler = MessageHandler(filters.COMMAND, unknown_command)
text_handler = MessageHandler(
    filters.TEXT & ~filters.COMMAND,
    handle_text
)

application = application_builder.token(TOKEN).build()

application.add_handler(start_handler)
application.add_handler(menu_handler)
application.add_handler(help_handler)
application.add_handler(text_handler)
application.add_handler(unknown_handler)

application.run_polling()
