import os
import logging
import responses
from telegram.ext import *
from dotenv import load_dotenv

# we use this to get api key from env files
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Set up the logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


# We defined this fuction to use as commands
# all update.message are reply from bots to user
def start(update, context):
    update.message.reply_text(
        'Hello there, I\'m an AI bot who can converse with you or assist you in completing tasks.\n To start, say hey, hi, or hello.')


def help(update, context):
    update.message.reply_text('Type cmd for options or click /cmd')


def cmd(update, context):
    update.message.reply_text('Availble Commands:\nFor notes- /notes\n ')


def notes(update, context):
    update.message.reply_text(
        'Soon, you\'ll be able to get your hands on some notes.')


def list(update, context):
    update.message.reply_text(
        'All commands you can use\n /help : offcourse for help dumbo\n\n /notes: To get notes\n\n /projects : for all projects🔥')

# there two methods to crete functions to get repond from bot this is 2nd one


def socials(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="https://www.instagram.com/Shaurya_king_")


def source_code(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="the source code can be accessed here\n {Github}\n https://github.com/ItsAttitudeking/human-robot")


def projects(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="join @attitude_galaxy for project update")


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programms from here
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands handler which callback our commands when user ask for it
    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CommandHandler('help', help))

    dp.add_handler(CommandHandler('cmd', cmd))

    dp.add_handler(CommandHandler('notes', notes))

    dp.add_handler(CommandHandler('list', list))

    dp.add_handler(CommandHandler('socials', socials))

    dp.add_handler(CommandHandler('source_code', source_code))

    dp.add_handler(CommandHandler('projects', projects))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    # Idle state give bot time to go in idle
    updater.idle()
