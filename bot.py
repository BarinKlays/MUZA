# Зависимости: pip install python-telegram-bot
import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "7903702520:AAGzIN0qLtB3OyFQ0k2n_tfLn5kk-jxWXbQ"  # Получите у @BotFather
WEB_APP_URL = "https://your-web-app-url.com"  # Ссылка на ваш развернутый сайт фронтенда


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton(
                text="Открыть LoveLink 🎵",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text=f"Привет, {update.effective_user.first_name}! 👋\n\n"
             f"Добро пожаловать в **LoveLink** — сервис знакомств, где людей объединяет музыка.\n\n"
             f"Нажми кнопку ниже, чтобы найти свою историю 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()