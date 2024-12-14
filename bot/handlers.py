from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Open Wallet", web_app={'url': context.bot_data["web_link"]})],
        [InlineKeyboardButton("Contact Us", callback_data="contact_us")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Please choose an option:", reply_markup=reply_markup)

async def contact_us(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Twitter", url="https://x.com/endubiswallet"),
            InlineKeyboardButton("Telegram", url="https://t.me/endubiswallet"),
        ],
        [InlineKeyboardButton("Back to Menu", callback_data="back_to_start")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Contact us through these links:", reply_markup=reply_markup)

async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    # Reuse the start function's logic here
    keyboard = [
        [InlineKeyboardButton("Open Wallet", web_app={'url': context.bot_data["web_link"]})],
        [InlineKeyboardButton("Contact Us", callback_data="contact_us")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Welcome! Please choose an option:", reply_markup=reply_markup)
