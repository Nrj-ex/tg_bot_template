from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from constants import MENU


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""

    user = update.effective_user
    help_text = f"""help text"""
    keyboard = [
        [
            InlineKeyboardButton('menu', callback_data=MENU),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=user.id, text=help_text, reply_markup=reply_markup)
