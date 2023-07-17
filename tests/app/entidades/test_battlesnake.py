from src.app.entidades.Arena import Arena
from src.app.entidades.BattleSnake import BattleSnake
from src.app.entidades.Ponto import Ponto


class Test_BattleSnake:
    def test_battlesnake(self):
        
        battlesnake = BattleSnake(body={
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
        
    def test_battlesnake_setar_modo_1(self): 
        battlesnake = BattleSnake(body={
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
            ]
        }
        arena = Arena(body=body)
        battlesnake.seta_modo(arena=arena)
        assert battlesnake.modo == 1
        
    def test_battlesnake_setar_modo_2(self): 
        battlesnake = BattleSnake(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0},
                {"x": 2, "y": 1}
            ],
            "latency": "123",
            "head": {"x": 0, "y": 0},
            "length": 4,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })
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
            ]
        }
        arena = Arena(body=body)
        battlesnake.seta_modo(arena=arena)
        assert battlesnake.modo == 2
        
    def test_battlesnake_setar_modo_3(self): 
        battlesnake = BattleSnake(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 5, "y": 5},
                {"x": 5, "y": 4},
                {"x": 4, "y": 4},
                {"x": 4, "y": 5},
            ],
            "latency": "123",
            "head": {"x": 5, "y": 4},
            "length": 4,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        })
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
            ]
        }
        arena = Arena(body=body)
        battlesnake.seta_modo(arena=arena)
        assert battlesnake.modo == 3
