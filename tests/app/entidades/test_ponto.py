import pytest
from src.app.entidades.Ponto import Ponto
from src.app.helpers.erro import Erro


class Test_Ponto:
    def test_ponto(self):
        ponto = Ponto(x=1, y=2)
        assert ponto.x == 1
        assert ponto.y == 2

    def test_ponto_nao_inteiro(self):
        with pytest.raises(Erro):
            Ponto(x=1.5, y=2)

        with pytest.raises(Erro):
            Ponto(x=1, y=2.5)

    def test_ponto_coordenadas_negativas(self):
        with pytest.raises(Erro):
            Ponto(x=-1, y=2)

        with pytest.raises(Erro):
            Ponto(x=1, y=-2)

    def test_ponto_distancia_1(self):
        ponto = Ponto(x=1, y=2)
        ponto2 = Ponto(x=2, y=2)
        assert ponto.distancia(ponto2) == 1

    def test_ponto_distancia_2(self):
        ponto = Ponto(x=0, y=3)
        ponto2 = Ponto(x=4, y=0)
        assert ponto.distancia(ponto2) == 5

    def test_ponto_distancia_3(self):
        ponto = Ponto(x=0, y=0)
        ponto2 = Ponto(x=2, y=2)
        assert ponto.distancia(ponto2) == 2.828427

    def test_ponto_str(self):
        ponto = Ponto(x=1, y=2)    
        assert str(ponto) == "(1,2)"

    def test_ponto_eq(self):
        ponto = Ponto(x=1, y=2)
        ponto2 = Ponto(x=1, y=2)
        ponto3 = Ponto(x=2, y=2)

        assert ponto == ponto2
        assert ponto != ponto3

    def test_construtor_em_string_1(self):
        ponto = Ponto(ponto_string="(1,2)")
        assert ponto.x == 1
        assert ponto.y == 2
        
    def test_construtor_em_string_2(self):
        ponto = Ponto(ponto_string="(12,23)")
        assert ponto.x == 12
        assert ponto.y == 23
        
    def test_construtor_em_string_3(self):
        ponto = Ponto(x=1, y=2)
        ponto = Ponto(ponto_string=str(ponto))
        assert ponto.x == 1
        assert ponto.y == 2

    def test_construtor_em_string_erro(self):
        with pytest.raises(Erro):
            Ponto(ponto_string="(x=1, y=2)")
