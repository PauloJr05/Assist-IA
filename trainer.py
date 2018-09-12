# -*- coding: utf-8 -*-


from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot import ChatBot

import os


bot = ChatBot('Raquel')



class Trainer:
    def __init__(self):
        None


    def trainerCorpusPt(self):
        bot.set_trainer(ChatterBotCorpusTrainer)
        bot.train("chatterbot.corpus.portuguese")



    def trainerList(self):
        bot.set_trainer(ListTrainer)  # define metodo de treinamento modo lista

        for _file in os.listdir('Chats'): #Percorrer todos os arquivos e chats
            lines = open('Chats/' + _file, 'r').readlines()  # Ler as linhs dos arquivos dos chats
            bot.train(lines)

    def chatsFile(self, nameFile, talk):
        open('Chats/' + 'talking_' + str(nameFile), 'a').writelines(talk + "\n")

