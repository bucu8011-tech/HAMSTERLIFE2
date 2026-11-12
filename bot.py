
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
GAME_URL = "https://bucu8011-tech.github.io/HAMSTERLIFE2/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton("🐹 PLAY HAMSTER LIFE", url=GAME_URL)
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome to HAMSTER LIFE!\n\n"
        "Tap, Earn and Upgrade!\n"
        "Click below to play.",
        reply_markup=reply_markup
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is missing")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
