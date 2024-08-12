from uuid import uuid4
from telegram import (InlineQueryResultArticle, InputTextMessageContent,
                      InlineQueryResultsButton, Update, InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import ContextTypes
from random import randint
from loader import storage


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the inline query. This is run when you type: @botusername <query>"""
    user = update.effective_user

    confessions_keyboard = [
        [InlineKeyboardButton('random int', switch_inline_query_current_chat=' ')],
    ]

    await update.inline_query.answer([
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="random int",
            input_message_content=InputTextMessageContent(str(randint(0, 100))),
            description="random(0-100)",
            reply_markup=InlineKeyboardMarkup(confessions_keyboard)
        ),
    ], cache_time=0, is_personal=True,
        # кнопка перехода в бота, разобраться в стартовом параметре и возможностью добавить ссылку на другой канал
        button=InlineQueryResultsButton(text='Перейти в бота', start_parameter='start')

    )
