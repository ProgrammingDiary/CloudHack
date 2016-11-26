from telegram.ext import Updater, CommandHandler
import telegram
import logging
import requests

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token = '314860602:AAFQTb32RcGtEthJWZVT0aNcJknCiKsamO0')
dispatcher = updater.dispatcher


def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Hi!!")



start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()