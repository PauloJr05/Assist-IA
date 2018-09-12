# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from trainer import Trainer
import sys
from time import sleep

arg = sys.argv

bot = ChatBot('Raquel', read_only = True)
while True:
    eu = input('Eu: ')

    print('Raquel:{}'.format(bot.get_response(eu)))
    Trainer().chatsFile(arg[1], eu)
    Trainer().chatsFile(arg[1],str(bot.get_response(eu)))
    if (eu == 'Que tal treinar?'):
        sleep(3.0)
        Trainer().trainerList()
