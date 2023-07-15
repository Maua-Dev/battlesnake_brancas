import random

from src.app.enums.frases_enum import FrasesEnum
class Utils:
    @staticmethod
    def escolhe_frase():
        pass

    @staticmethod
    def escolhe_conjunto_de_frases():   
        return random.choice(list(FrasesEnum)).value.lower()