#!/usr/bin/env python
# -- coding: utf-8 --
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from html2image import Html2Image
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command is issued."""
    update.message.reply_text('Hi!')


def stop(update, context):
    """Send a message when the command is issued."""
    update.message.reply_text('Oo stree fir jarur aana')


def result(update, context):
    """Send a message when the command is issued."""
    text = str(update.message.text)
    #txt = "/result e19223035500018"
    text = text.upper()
    text = text.replace("/RESULT E","E")
    print(text)
    
    update.message.reply_text('Achha apna Result...  hmm')
    update.message.reply_text('Enrollment no sahi hai na...?')
    update.message.reply_text(text)
    
    # downloading logic
    filename = text+".png"
    link = "http://result.bteupexam.in/Odd_Semester/main/result.aspx?Roll_no="+text
    try:
        update.message.reply_text("\n\nDownloading.....{}\n\n".format(filename))
        hti = Html2Image()
        update.message.reply_text(link)
        update.message.reply_text("\n\ncopy paste this link in browser if not downloaded\n\n")
        hti.screenshot(url=link, save_as=filename)
        # context = {'img': image}

        update.message.reply_text("{} downloaded successfully.....\n".format(filename))
        chat_id = update.message.chat_id
        doc = open(filename, 'rb')
        context.bot.send_document(chat_id, doc)
        if os.path.exists(filename):
            os.remove(filename)
    
    except OSError:
        update.message.reply_text("\nUnfortunately failed to generate file. \nNot supported in current server.\n")
        update.message.reply_text(link)
        update.message.reply_text("Copy paste this link in browser if not downloaded\n")
        

def results(update, context):
    """Send a message when the command is issued."""
    update.message.reply_text('Array sabke chahiye Results...  hmm')
    text = str(update.message.text)
    #txt = "/result e19223035500018"
    print(text)
    text = text.upper()
    text = text.split(" ")
    print(text)
    upl = text[1]
    dwl = text[2]
    
    print(upl)
    print(dwl)
    
    update.message.reply_text('Enrollment range sahi hai na...?')
    update.message.reply_text(upl)
    update.message.reply_text(dwl)
    
    
    # downloading logic
    low = int(upl[1::])
    up = int(dwl[1::])
    up = up + 1
    
    for i in range(low, up) :
        enum = upl[:1:]
        i = f'{i}'
        enum = enum + i
        link = "http://result.bteupexam.in/Odd_Semester/main/result.aspx?Roll_no="+enum
        filename = enum+".png"
        try:
            update.message.reply_text("\n\nDownloading.....{}\n\n".format(filename))
            hti = Html2Image()
            update.message.reply_text(link)
            update.message.reply_text("\n\ncopy paste this link in browser if not downloaded\n\n")
            hti.screenshot(url=link, save_as=filename)
            # context = {'img': image}
    
            update.message.reply_text("{} downloaded successfully.....\n".format(filename))
            chat_id = update.message.chat_id
            doc = open(filename, 'rb')
            context.bot.send_document(chat_id, doc)
        except OSError:
            update.message.reply_text("\nUnfortunately failed to generate file. \nNot supported in current server.\n")
            update.message.reply_text(link)
            update.message.reply_text("Copy paste this link in browser if not downloaded\n")
        
  


def resume(update, context):
    """Send a message when the command is issued."""
    update.message.reply_text('Oh Resume bhi banana hai katayi professional huye jaa rahe ho...  hmm')


def chat(update, context):
    """Send a message when the command is issued."""
    chatapp = "https://vebhvv.pythonanywhere.com/help/?username=user"
    update.message.reply_text(f'click on the link\n\n\n{chatapp}')


def help(update, context):
    """Send a message when the command is issued."""
    update.message.reply_text('Help!')
    update.message.reply_text('For downloading single result, type "/result E19223035500007" to get your result.\n')
    update.message.reply_text('For downloading single result, type "/result E19223035500007 E19223035500047" to get your result.\n')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    tokencode = "5640201328:AAGsW4IKdKP11nYSRH7YcZiwqcNvyA2Yz3g"
    updater = Updater(tokencode, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("result", result))
    dp.add_handler(CommandHandler("results", results))
    dp.add_handler(CommandHandler("resume", resume))
    dp.add_handler(CommandHandler("chat", chat))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

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
