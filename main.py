#!/usr/bin/env python3
from aiotg import Bot, Chat

from config import TG_TOKEN

bot = Bot(api_token=TG_TOKEN)


@bot.command(r"ping")
def ping(chat: Chat):
    return chat.reply('pong')


if __name__ == "__main__":
    bot.run()
