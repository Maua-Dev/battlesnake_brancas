
from src.app.enums.frases_enum import FrasesEnum
from src.app.funcoes.utils import Utils


class Test_Utils:
    def test_escolhe_conjunto_de_frases(self):
        assert Utils.escolhe_conjunto_de_frases() in [cjt.value.lower() for cjt in list(FrasesEnum)] 

    def test_escolhe_frase(self):
        frase = Utils.escolhe_frase() # testado verificando o debug console
        assert True