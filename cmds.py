# -*- coding: utf-8 -*-


class Cmds:

    def __init__(self):
        None

    def calc(self, speaks):
        speaks.lower().capitalize()
        temp = speaks.split('Calcule')
        try:
            
            return eval(temp[1])
                
        except:
            pass
        return 'Não foi possivel calcular!'

        
