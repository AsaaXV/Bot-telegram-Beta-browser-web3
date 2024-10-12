from telegram import Update, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Fungsi untuk menangani perintah /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Buat tombol untuk membuka Web App
    keyboard = [
        [InlineKeyboardButton("Open Search App", web_app=WebAppInfo(url="https://your-website-url.com"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Kirim pesan ke pengguna dengan tombol
    await update.message.reply_text("Klik tombol di bawah untuk membuka aplikasi pencarian:", reply_markup=reply_markup)

if __name__ == '__main__':
    # Ganti 'YOUR_TELEGRAM_BOT_API_TOKEN' dengan Token API bot Anda
    application = ApplicationBuilder().token('7737638661:AAGC4_yaZNLRoM3wAivAybYjKNAWw1xRb-Q').build()

    # Daftarkan handler untuk menangani perintah /start
    application.add_handler(CommandHandler("start", start))

    # Jalankan bot
    application.run_polling()