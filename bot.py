import logging
import telegram
import os
import sys
import requests
from sys import argv
import urllib
import urllib.request
from bs4 import BeautifulSoup
import datetime






import bot
from telegram.ext import ConversationHandler


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

GENDER, NAMER, VOICE, IMG = range(4)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    update.message.reply_text('I Am Online')
    update.message.reply_text('This Bot Was Made By @g4_media')
    update.message.reply_text('Please Consider Subscribing our Youtube Channel https://www.youtube.com/channel/UCad4U0t57KqjvHxqqdmZW_w')
    update.message.reply_text('This Bot Helps You to download instagram photos')
    

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')
    update.message.reply_text("This is a Multi Function Bot\nThis Bot was Made By @g4_media\n\nThis Bot Can Rename Files Upto 100MB\n	For This you Have to send the document to this bot\n	And provide new name whwn asked\n\nThis Bot Can Convert Voice Messege to audio file and audio document\n	For this you Have to send the voice message to this bot\n	And provide filename with disired filetype extention\n	eg : music.mp3\n	You will get the voice message as audio file and audio document\n\nThis Bot Can Convert Audio file to voice message\n	For this you have to send the audio file to ths bot\n	And you will get the audio file as voice message\n\nThis Bot Can Clear Captions of image\n	Just Send the image \n	You will get the Image as caption cleared")

def fuck(update, context):
    """Send a message when the command /fuck is issued."""
    update.message.reply_text('come lets do sex!')

def hai(update, context):
    """Send a message when the command /hai is issued."""
    update.message.reply_text('hello how are you')

def download(update, context):
    fileURL=update.message.text
    update.message.reply_text ('Downloading image...')
    f = urllib.request.urlopen(fileURL)
    htmlSource = f.read()
    soup = BeautifulSoup(htmlSource,'html.parser')
    metaTag = soup.find_all('meta', {'property':'og:image'})
    imgURL = metaTag[0]['content']
    fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.jpg'
    urllib.request.urlretrieve(imgURL, fileName)
    update.message.reply_text ('Done. Image saved to disk as ' + fileName)
    context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(fileName, 'rb'), filename=fileName)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(fileName,'rb'))
    os.remove(fileName)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    update.message.reply_text("Sorry Error Occured   " + str(context.error))

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(os.environ['bottoken'], use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("fuck", fuck))
    dp.add_handler(CommandHandler("hai", hai))

    dp.add_handler(MessageHandler(Filters.text, download))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
   main()
