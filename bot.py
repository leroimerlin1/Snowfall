import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# ================== CONFIGURATION ==================
TOKEN = "8518259021:AAGMsr9h8ALE3YeeKL_fwGnrnt9edAm-L3o"  #Remplace par le token de BotFather

# URL de ta Mini App (boutique)
MINI_APP_URL = "https://leroimerlin1.github.io/Snowfall/"  # ← CHANGE ÇA avec l'URL réelle de ta mini app

# ===================================================

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /start"""
    keyboard = [
        [InlineKeyboardButton(
            text="🛒 Ouvrir ma Boutique",
            web_app=WebAppInfo(url=MINI_APP_URL)
        )]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Bienvenue chez **Coffee Snowfall44** !\n\n"
        "Clique sur le bouton ci-dessous pour accéder à ma boutique Mini App 🌱",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot Coffee Snowfall44\n\n"
        "Commandes disponibles :\n"
        "/start - Ouvrir la boutique\n"
        "/help - Afficher l'aide"
    )


def main():
    application = Application.builder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    print("🤖 Bot Popeye Farmz 76 démarré...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
