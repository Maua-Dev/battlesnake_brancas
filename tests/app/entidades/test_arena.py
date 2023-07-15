import pytest
from src.app.entidades.Arena import Arena
from src.app.entidades.Ponto import Ponto
from src.app.helpers.erro import Erro

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
                {"id": "snake-one"},
                {"id": "snake-two"},
                {"id": "snake-three"}
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
                {"id": "snake-one"},
                {"id": "snake-two"},
                {"id": "snake-three"}
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
                {"id": "snake-one"},
                {"id": "snake-two"},
                {"id": "snake-three"}
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
                {"id": "snake-one"},
                {"id": "snake-two"},
                {"id": "snake-three"}
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
                {"id": "snake-one"},
                {"id": "snake-two"},
                {"id": "snake-three"}
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


    

    