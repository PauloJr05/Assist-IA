# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot




bot = ChatBot('Raquel', read_only = True)
while True:
    eu = input('Eu: ')
    print('Bot:{}'.format(bot.get_response(eu)))
