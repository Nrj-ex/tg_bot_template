from telegram import Update
from telegram.ext import ContextTypes
from loader import storage
from handlers.help import help


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""

    user = update.effective_user
    storage.add_user(user=user)

    await context.bot.send_message(chat_id=user.id,
                                   text=f"Привет, {update.effective_user.name}")

    await help(update, context)
