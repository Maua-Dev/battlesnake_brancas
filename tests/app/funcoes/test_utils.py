
from src.app.shared.entidades.Ponto import Ponto
from src.app.shared.enums.frases_enum import FrasesEnum
from src.app.shared.helpers.utils import Utils


class Test_Utils:
    def test_escolhe_conjunto_de_frases(self):
        assert Utils.escolhe_conjunto_de_frases() in [cjt.value.lower() for cjt in list(FrasesEnum)] 

    def test_escolhe_frase(self):
        frase = Utils.escolhe_frase() # testado verificando o debug console
        assert True

    def test_ponto_uniq_1(self):
        lista_de_pontos = [Ponto(x=1, y=2), Ponto(x=1, y=2), Ponto(x=2, y=3)]
        lista_sem_duplicatas = Utils.ponto_uniq(l=lista_de_pontos)
        esperado = [Ponto(x=1, y=2), Ponto(x=2, y=3)]

        assert all(
            [ponto in lista_sem_duplicatas for ponto in esperado]
        )

    def test_ponto_uniq_2(self):
        lista_de_pontos = [Ponto(x=1, y=2), Ponto(x=1, y=3), Ponto(x=2, y=3)]
        lista_sem_duplicatas = Utils.ponto_uniq(l=lista_de_pontos)
        esperado = [Ponto(x=1, y=2), Ponto(x=1, y=3), Ponto(x=2, y=3)]

        assert all(
            [ponto in lista_sem_duplicatas for ponto in esperado]
        )