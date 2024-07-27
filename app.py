from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, filters
from credentials import BOT_TOKEN, BOT_USERNAME
import json

async def launch_web_ui(update: Update, callback: CallbackContext):
    # For now, we just display google.com...
    kb = [
        [KeyboardButton("Play in 1 Click", web_app=WebAppInfo("https://umarbrowser.github.io/gsu"))]
    ]
    await update.message.reply_text("Let's do this...", reply_markup=ReplyKeyboardMarkup(kb))

# async def launch_web_ui(update: Update, callback: CallbackContext):
#     # For now, let's just acknowledge that we received the command
#     await update.effective_chat.send_message("Barka da zuwa Muna kan aikine daga CEO Pyc0d3r")


if __name__ == '__main__':
    # when we run the script we want to first create the bot from the token:
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # and let's set a command listener for /start to trigger our Web UI
    application.add_handler(CommandHandler('start', launch_web_ui))

    # and send the bot on its way!
    print(f"Your bot is listening! Navigate to http://t.me/{BOT_USERNAME} to interact with it!")
    application.run_polling()