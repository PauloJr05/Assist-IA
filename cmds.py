# -*- coding: utf-8 -*-

import subprocess as subProc

class Cmds:

    def __init__(self):
        None

    def calc(self, speaks):
        speaks.lower().capitalize()
        temp = speaks.replace('Calcule ', '')
        try:
            return eval(temp)      
        except:
            pass
        return 'Não foi possivel calcular!'

    def executaProg(self, command):
        #command.lower().capitalize()
        #temp = command.slip('Execute')
        try:
            subProc.Popen(str(command))
            return str(command)
        except FileNotFoundError:
            subProc.Popen(['xdg-open',str(command)])
            return str(command)
            

        
