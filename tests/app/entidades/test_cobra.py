from src.app.shared.Cobra import Cobra
from src.app.shared.Ponto import Ponto


class Test_Cobra:
    def test_cobra(self):
        
        cobra = Cobra(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0}
            ],
            "latency": "123",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })
        assert True

    def test_cobra_redondezas_da_cabeca_1(self):
        cobra = Cobra(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 1, "y": 1}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0}
            ],
            "latency": "123",
            "head": {"x": 1, "y": 1},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })
    
        redondezas = cobra.retorna_redondezas_da_cabeca(altura_max=100, largura_max=100)
        esperado = [
            Ponto(x=1,y=2),
            Ponto(x=1,y=0),
            Ponto(x=2,y=1),
            Ponto(x=0,y=1)
        ]
        assert len(redondezas) == len(esperado)
        assert all([p in esperado for p in redondezas])

    def test_cobra_redondezas_da_cabeca_2(self):
        cobra = Cobra(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0}
            ],
            "latency": "123",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })
    
        redondezas = cobra.retorna_redondezas_da_cabeca(altura_max=100, largura_max=100)
        esperado = [
            Ponto(x=1,y=0),
            Ponto(x=0,y=1)
        ]
        assert len(redondezas) == len(esperado)
        assert all([p in esperado for p in redondezas])

    def test_cobra_redondezas_da_cabeca_3(self):
        cobra = Cobra(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 1, "y": 1}, 
            ],
            "latency": "123",
            "head": {"x": 1, "y": 1},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })
    
        redondezas = cobra.retorna_redondezas_da_cabeca(altura_max=2, largura_max=2)
        esperado = [
            Ponto(x=1,y=0),
            Ponto(x=0,y=1)
        ]
        assert len(redondezas) == len(esperado)
        assert all([p in esperado for p in redondezas])

    def test_cobra_perigos_1(self):
        cobra = Cobra(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0}, 
                {"x": 3, "y": 0}, 
                {"x": 3, "y": 1}, 
            ],
            "latency": "123",
            "head": {"x": 3, "y": 1},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })
    
        perigos = cobra.retorna_perigos(altura_max=4, largura_max=4)
        esperado = [
            Ponto(x=0,y=0),
            Ponto(x=1,y=0),
            Ponto(x=2,y=0),
            Ponto(x=3,y=0),
            Ponto(x=3,y=1),
        ]
        assert len(perigos) == len(esperado)
        assert all([p in esperado for p in perigos])

    def test_cobra_perigos_2(self):
        cobra = Cobra(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0}, 
                {"x": 0, "y": 1}, 
                {"x": 1, "y": 1}, 
                {"x": 2, "y": 1}, 
                {"x": 0, "y": 2}, 
                {"x": 1, "y": 2}, 
                {"x": 2, "y": 2}, 
            ],
            "latency": "123",
            "head": {"x": 1, "y": 1},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })
    
        perigos = cobra.retorna_perigos(altura_max=4, largura_max=4)
        esperado = [
            Ponto(x=0,y=0),
            Ponto(x=1,y=0),
            Ponto(x=2,y=0),
            Ponto(x=0,y=1),
            Ponto(x=1,y=1),
            Ponto(x=2,y=1),
            Ponto(x=0,y=2),
            Ponto(x=1,y=2),
            Ponto(x=2,y=2)
        ]
        assert len(perigos) == len(esperado)
        assert all([p in esperado for p in perigos])

    def test_cobra_perigos_3(self):
        cobra = Cobra(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0}, 
            ],
            "latency": "123",
            "head": {"x": 2, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })
    
        perigos = cobra.retorna_perigos(altura_max=1, largura_max=3)
        esperado = [
            Ponto(x=0,y=0),
            Ponto(x=1,y=0),
            Ponto(x=2,y=0),
        ]
        assert len(perigos) == len(esperado)
        assert all([p in esperado for p in perigos])

    def test_cobra_perigos_4(self):
        cobra = Cobra(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0}, 
            ],
            "latency": "123",
            "head": {"x": 2, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })
    
        perigos = cobra.retorna_perigos(altura_max=1, largura_max=4)
        esperado = [
            Ponto(x=0,y=0),
            Ponto(x=1,y=0),
            Ponto(x=2,y=0),
        ]
        assert len(perigos) == len(esperado)
        assert all([p in esperado for p in perigos])

    def test_cobra_encontra_ponto_mais_perto_0(self): 
        cobra = Cobra(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0}, 
            ],
            "latency": "123",
            "head": {"x": 2, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })
        assert cobra.encontra_ponto_mais_perto([]) is None
    

    def test_cobra_encontra_comida_mais_perto_1(self): 
        cobra = Cobra(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0}, 
            ],
            "latency": "123",
            "head": {"x": 2, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })
        assert cobra.encontra_ponto_mais_perto(lista_de_pontos=[Ponto(x=1,y=1)]) == Ponto(x=1,y=1)


    def test_cobra_encontra_ponto_mais_perto_1_mais(self): 
        cobra = Cobra(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0}, 
            ],
            "latency": "123",
            "head": {"x": 3, "y": 4},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })

        lista_de_pontos = [
            Ponto(x=0,y=4),
            Ponto(x=3,y=0),
            Ponto(x=0,y=0)
        ]

        assert cobra.encontra_ponto_mais_perto(lista_de_pontos=lista_de_pontos) == Ponto(x=0,y=4)
        
