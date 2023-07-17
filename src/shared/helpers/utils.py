import random
from typing import List
from src.shared.entidades.Ponto import Ponto

from src.shared.enums.frases_enum import FrasesEnum

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
    
    @staticmethod
    def ponto_uniq(l: List[Ponto]) -> List[Ponto]:
        l_str = list(set([str(ponto) for ponto in l]))
        return [Ponto(ponto_string=ponto) for ponto in l_str]
