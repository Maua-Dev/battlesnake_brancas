import random

from src.app.enums.frases_enum import FrasesEnum
class Utils:
    @staticmethod
    def escolhe_frase():
        conjunto = Utils.escolhe_conjunto_de_frases()
        with open(f"src/app/frases/{conjunto}.txt", 'r') as f:
            frases = f.readlines()
            frase = random.choice(frases).replace('\n', '')
            f.close()
        return frase
        

    @staticmethod
    def escolhe_conjunto_de_frases() -> str:   
        return random.choice(list(FrasesEnum)).value.lower()