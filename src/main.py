import telebot
import os
from loguru import logger



class Bot:
    def __init__(self):
       self.bot = telebot.TeleBot(
            os.environ['TELEGRAMBOT_TOKEN'], parse_mode = None)
       self.send_welcome = self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)


    def run(self):
        logger.info('Running bot...')
        self.bot.polling()

    
    def send_welcome(self, message):
        print(dir(message))
        self.bot.reply_to(message, "Hey, how are you doing?")
	    


if __name__ == '__main__':
    bot = Bot()
    bot.run()

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")


# print("Starting bot...")
#bot.polling()    