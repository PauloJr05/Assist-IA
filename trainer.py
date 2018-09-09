# -*- coding: utf-8 -*-


from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot import ChatBot

import os

bot = ChatBot('Raquel')

bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.portuguese")

bot.set_trainer(ListTrainer)  # define metodo de treinamento

for _file in os.listdir('Chats'):  # Percorrer todos os arquivos e chats
    lines = open('Chats/' + _file, 'r').readlines()  # Ler as linhs dos arquivos dos chats

    bot.train(lines)
