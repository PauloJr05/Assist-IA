# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import sys
from time import sleep

from trainer import Trainer
from cmds import Cmds

arg = sys.argv
bot = ChatBot('Raquel')


while True:

    if arg[1] == 'Conversa':

        eu = str(input('Eu: ')).lower().capitalize()
        if ('Calcule' in eu):
            temp1 = Cmds().calc(eu)
            print('Raquel: O resultado é: {}, mais alguma coisa?'.format(temp1))
        else:
            print('Raquel:{}'.format(bot.get_response(eu)))

    elif arg[1] == 'Treino':
        Trainer().trainerFeedback()

    elif arg[1] == 'Corpus':
        Trainer().trainerCorpusPt()
        break

    elif arg[1] == 'Lista':
        Trainer().trainerList()
        break


