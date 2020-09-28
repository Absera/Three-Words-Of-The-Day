        import telegram
import time
import schedule
import emoji
from vocablury import *

TOKEN = "1121128262:AAHVx5CJQLEfcA4zwkeC7gtnOYxPNT9QevY"
bot = telegram.Bot(token=TOKEN)

def sendSeparator():
    global bot
    separator = "*****"
    bot.sendMessage(chat_id="@ThreeWordsOfTheDay", text=separator)

            
def sendVocablury():
    global bot
    generated = generateRandom()
    text = f"""
\n
\U00002B50 Word: *{generated['word']}*   
\n
\U00002B50 Type: *{generated["type"]}*
\n
\U00002B50 Definition:
_{generated['definition']}_
\n
Share @ThreeWordsOfTheDay
            """
    try:
        bot.sendMessage(chat_id="@ThreeWordsOfTheDay", text=text, parse_mode=telegram.ParseMode.MARKDOWN)
        print("Sent!")
    except:
        print("Retrying...")
        time.sleep(1)
        sendVocablury()


def sendAll():
	sendVocablury()
	sendVocablury()
	sendVocablury()
	sendSeparator()

schedule.every().day.at("03:00").do(sendAll)

while True:
    schedule.run_pending()
    time.sleep(1)
