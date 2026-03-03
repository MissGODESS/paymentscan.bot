from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN_HERE"

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 👋 Welcome to my bot!")

# Add command
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        num1 = int(context.args[0])
        num2 = int(context.args[1])
        result = num1 + num2
        await update.message.reply_text(f"Result: {result}")
    except:
        await update.message.reply_text("Usage: /add 5 10")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add))

print("Bot is running...")
app.run_polling()
