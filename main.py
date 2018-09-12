# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from trainer import Trainer
import sys

arg = sys.argv

#Trainer().trainerCorpusPt()
#Trainer().trainerList()


bot = ChatBot('Raquel', read_only = True)
while True:
    eu = input('Eu: ')

    print('Raquel:{}'.format(bot.get_response(eu)))
    Trainer().chatsFile(arg[1], eu)
    if (eu == 'Que tal treinar?'):
        Trainer().trainerList()