import telebot 
import config

bot = telebot.TeleBot(config.telegramApi, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	print("done")
	print(message.message_id)
user = bot.get_me()
print(user)

bot.polling()

