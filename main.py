import asyncio
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from bot.handlers import start, contact_us, back_to_start
from config import TOKEN, WEBHOOK_URL, PORT, WEB_LINK
import uvicorn

app = FastAPI()

# Create the bot application
application = Application.builder().token(TOKEN).build()

# Add bot data for shared resources
application.bot_data["web_link"] = WEB_LINK

# Add handlers to the application
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(contact_us, pattern="^contact_us$"))
application.add_handler(CallbackQueryHandler(back_to_start, pattern="^back_to_start$"))

# Webhook endpoint for Telegram updates
@app.post("/telegram")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, application.bot)
    await application.initialize()
    await application.process_update(update)
    return "OK"

# Health check endpoint
@app.get("/")
async def health():
    return {"status": "Bot is running and healthy!"}

# FastAPI startup event to set the webhook
@app.on_event("startup")
async def on_startup():
    await application.bot.set_webhook(f"{WEBHOOK_URL}/telegram")
    print(f"Webhook set to: {WEBHOOK_URL}/telegram")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
