# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from trainer import Trainer
import sys
from time import sleep

arg = sys.argv
bot = ChatBot('Raquel')


while True:

    if arg[1] == 'Conversa':

        eu = input('Eu: ')
        print('Raquel:{}'.format(bot.get_response(eu)))

    elif arg[1] == 'Treino':
        Trainer().trainerFeedback()

    elif arg[1] == 'Corpus':
        Trainer().trainerCorpusPt()
        break

    elif arg[1] == 'Lista':
        Trainer().trainerList()
        break


