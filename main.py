import logging
import sys
import os
import time

import telebot
from telebot import types

API_TOKEN = os.environ['token']

bot = telebot.TeleBot(API_TOKEN)
telebot.logger.setLevel(logging.DEBUG)


@bot.inline_handler(lambda query: query.query == 'text')
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