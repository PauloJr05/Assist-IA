# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from time import sleep
from gtts import gTTS
import os
import sys
from trainer import Trainer
from cmds import Cmds


def voice (voice):
    
    tts = gTTS(text=str(voice), lang='pt')
    tts.save("voice.mp3")
    os.system("mpg321 voice.mp3")

arg = sys.argv
bot = ChatBot('Raquel')


while True:

    if arg[1] == 'Conversa':

        eu = str(input('Eu: ')).lower().capitalize()
        if 'Calcule' in eu:
            resp = Cmds().calc(eu)
            print('Raquel: O resultado é: {}, deseja algo mais?'.format(resp))
            temp = 'O resultado é: {}, deseja algo mais?'.format(resp)
            voice(temp)

        elif 'Abra' in eu:
            resp = Cmds().executaProg(bot.get_response(eu))
            print('Raquel: O {} foi aberto com sucesso, deseja algo mais?'.format(resp))
            
        else:
            temp = bot.get_response(eu)
            print('Raquel:{}'.format(bot.get_response(eu)))
            voice(temp)

    elif arg[1] == 'Treino':
        Trainer().trainerFeedback()

    elif arg[1] == 'Corpus':
        Trainer().trainerCorpusPt()
        break

    elif arg[1] == 'Lista':
        Trainer().trainerList()
        break


