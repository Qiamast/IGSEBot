import logging
import sys
import os
import time
import telebot
from telebot import types

# Config
Telegram_API_Token = os.environ['Telegram_API_Token']
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
SEARCH_ENGINE_ID = os.environ['SEARCH_ENGINE_ID']

bot = telebot.TeleBot(Telegram_API_Token)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger()


@bot.inline_handler(lambda query: query.query != '')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result1', types.InputTextMessageContent('سلام این اولین نمونه سرچ در گوگل است'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('سلام این دومین نمونه از سرچ در گوگل است'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)



@bot.inline_handler(lambda query: len(query.query) == 0)
def default_query(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'برای سرچ در گوگل ، لطفا چیزی بنویسید', types.InputTextMessageContent('این پیام پیشفرض است'))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


def main_loop():
    bot.infinity_polling()
    while 1:
        time.sleep(2)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)