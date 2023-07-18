from src.shared.entidades.Arena import Arena
from src.shared.entidades.Ponto import Ponto

COBRA = {
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
        }

class Test_Arena:
    def test_arena(self):
        body = {
            "height": 11,
            "width": 11,
            "food": [
                {"x": 5, "y": 5}, 
                {"x": 9, "y": 0}, 
                {"x": 2, "y": 6}
            ],
            "hazards": [
                {"x": 0, "y": 0}, 
                {"x": 0, "y": 1}, 
                {"x": 0, "y": 2}
            ],
            "snakes": [
                COBRA
            ]
        }
        arena = Arena(body=body)
        assert True

    def test_arena_centro_1(self):
        body = {
            "height": 12,
            "width": 12,
            "food": [
                {"x": 5, "y": 5}, 
                {"x": 9, "y": 0}, 
                {"x": 2, "y": 6}
            ],
            "hazards": [
                {"x": 0, "y": 0}, 
                {"x": 0, "y": 1}, 
                {"x": 0, "y": 2}
            ],
            "snakes": [
                COBRA
            ]
        }
        arena = Arena(body=body)
        centro = arena.retorna_centro()
        assert len(centro) == 4

        x = 5
        y = 5
        esperado = [
            Ponto(x=x,y=y),
            Ponto(x=x+1,y=y),
            Ponto(x=x,y=y+1),
            Ponto(x=x+1,y=y+1)
        ]        
        assert all([centro[i] == esperado[i] for i in range(4)])

    def test_arena_centro_2(self):
        body = {
            "height": 6,
            "width": 3,
            "food": [
                {"x": 5, "y": 5}, 
                {"x": 9, "y": 0}, 
                {"x": 2, "y": 6}
            ],
            "hazards": [
                {"x": 0, "y": 0}, 
                {"x": 0, "y": 1}, 
                {"x": 0, "y": 2}
            ],
            "snakes": [
                COBRA
            ]
        }
        arena = Arena(body=body)
        centro = arena.retorna_centro()
        assert len(centro) == 4

        x = 0
        y = 2
        esperado = [
            Ponto(x=x,y=y),
            Ponto(x=x+1,y=y),
            Ponto(x=x,y=y+1),
            Ponto(x=x+1,y=y+1)
        ]        
        assert all([centro[i] == esperado[i] for i in range(4)])

    def test_arena_centro_3(self):
        body = {
            "height": 7,
            "width": 8,
            "food": [
                {"x": 5, "y": 5}, 
                {"x": 9, "y": 0}, 
                {"x": 2, "y": 6}
            ],
            "hazards": [
                {"x": 0, "y": 0}, 
                {"x": 0, "y": 1}, 
                {"x": 0, "y": 2}
            ],
            "snakes": [
                COBRA
            ]
        }
        arena = Arena(body=body)
        centro = arena.retorna_centro()
        assert len(centro) == 4

        x = 3
        y = 2
        esperado = [
            Ponto(x=x,y=y),
            Ponto(x=x+1,y=y),
            Ponto(x=x,y=y+1),
            Ponto(x=x+1,y=y+1)
        ]        
        assert all([centro[i] == esperado[i] for i in range(4)])

    def test_arena_centro_4(self):
        body = {
            "height": 11,
            "width": 11,
            "food": [
                {"x": 5, "y": 5}, 
                {"x": 9, "y": 0}, 
                {"x": 2, "y": 6}
            ],
            "hazards": [
                {"x": 0, "y": 0}, 
                {"x": 0, "y": 1}, 
                {"x": 0, "y": 2}
            ],
            "snakes": [
                COBRA
            ]
        }
        arena = Arena(body=body)
        centro = arena.retorna_centro()
        assert len(centro) == 4

        x = 4
        y = 4
        esperado = [
            Ponto(x=x,y=y),
            Ponto(x=x+1,y=y),
            Ponto(x=x,y=y+1),
            Ponto(x=x+1,y=y+1)
        ]        
        assert all([centro[i] == esperado[i] for i in range(4)])

    def test_arena_comida(self):
        body = {
            "height": 12,
            "width": 12,
            "food": [
                {"x": 5, "y": 5}, 
                {"x": 9, "y": 0}, 
                {"x": 2, "y": 6}
            ],
            "hazards": [
                {"x": 0, "y": 0}, 
                {"x": 0, "y": 1}, 
                {"x": 0, "y": 2}
            ],
            "snakes": [
                COBRA
            ]
        }
        arena = Arena(body=body)
        comidas = arena.retorna_comidas()
        assert len(comidas) == 3
        
        esperado = [Ponto(x=5,y=5), Ponto(x=9,y=0), Ponto(x=2,y=6)]
        assert all([comidas[i] == esperado[i] for i in range(3)])

    

    