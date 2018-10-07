# -*- coding: utf-8 -*-


from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot import ChatBot

import os

CONVERSATION = 'learning_conversation'

bot = ChatBot('Raquel',
              storage_adapter="chatterbot.storage.SQLStorageAdapter",
              logic_adapters=["chatterbot.logic.BestMatch",
                              "chatterbot.logic.MathematicalEvaluation",
                              "chatterbot.logic.TimeLogicAdapter"]
              
              )


class Trainer:
    def __init__(self):
        None

    def trainerCorpusPt(self):
        bot.set_trainer(ChatterBotCorpusTrainer)
        bot.train("chatterbot.corpus.portuguese")


    def trainerList(self):
        bot.set_trainer(ListTrainer)  # define metodo de treinamento modo lista

        for _file in os.listdir('Chat_Manual'):  # Percorrer todos os arquivos e chats
            lines = open('Chat_Manual/' + _file, 'r').readlines()  # Ler as linhs dos arquivos dos chats
            bot.train(lines)

        for _file in os.listdir('Chat_Auto'):  # Percorrer todos os arquivos e chats
            lines = open('Chat_Auto/' + _file, 'r').readlines()  # Ler as linhs dos arquivos dos chats
            bot.train(lines)

    def trainerListUpdate(self, _file):
        bot.set_trainer(ListTrainer)
        lines = open('Chat_Auto/' + 'talking_' + str(_file)+ '.txt', 'r').readlines()
        bot.train(lines)

    def chatsFile(self, nameFile, talk):
        open('Chat_Auto/' + 'talking_' + str(nameFile) + '.txt', 'a').writelines(talk + "\n")

    def getFeedback(self):

        text = str(input())

        if 'sim' in text.lower():
            return False
        elif 'não' in text.lower() or 'nao' in text.lower():
            return True
        else:
            print('Por favor responda sim ou não')
            return self.getFeedback()

    def trainerFeedback(self):
        while True:
            # try:
            # print("Eu:")
            input_statement = str(input("Eu: "))
            input_statement = bot.input.process_input_statement(input_statement)
            # input_statement = bot.input.process_input_statement(input_statement)
            # bot.input.process_input()
            response = bot.get_response(input_statement)
            # botResponse = bot.process_response(response)
            # print("Raquel: {}".format(response))

            print('\n Raquel: É "{}" a resposta coerente para "{}"? \n'.format(response, input_statement))
            if self.getFeedback():
                # print("Então, qual o correto?")
                response1 = str(input("Então, qual o correto?\n Eu: "))
                response1 = bot.input.process_input_statement(response1)
                # bot.input.process_input()

                bot.learn_response(response1, input_statement)
                print("Ok! Aprendido")
                self.chatsFile('learning_01', str(input_statement))
                self.chatsFile('learning_01', str(response1))
                self.trainerListUpdate('learning_01')
            # bot.save()

    # Press ctrl-c or ctrl-d on the keyboard to exit
    # except(KeyboardInterrupt, EOFError, SystemExit):
    # break
