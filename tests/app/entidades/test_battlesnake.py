import pytest
from src.shared.entidades.Arena import Arena
from src.shared.entidades.BattleSnake import BattleSnake
from src.shared.entidades.Ponto import Ponto
from src.shared.helpers.erro import Erro

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
ARENA = Arena(body=body)

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
                {
                    "id": "totally-unique-snake-id",
                    "name": "Sneky McSnek Face",
                    "health": 54,
                    "body": [
                        {"x": 0, "y": 1}, 
                        {"x": 1, "y": 1}, 
                        {"x": 2, "y": 1},
                        {"x": 3, "y": 1}
                    ],
                    "latency": "123",
                    "head": {"x": 0, "y": 1},
                    "length": 4,
                    "shout": "why are we shouting??",
                    "squad": "1",
                    "customizations":{
                        "color":"#26CF04",
                        "head":"smile",
                        "tail":"bolt"
                    }
                }
            ]
        }
ARENA_2 = Arena(body=body)

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
        }, arena=ARENA)
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
        }, arena=ARENA)
        
        battlesnake.seta_modo()
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
        }, arena=ARENA)
        
        battlesnake.seta_modo()
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
        }, arena=ARENA)
        
        battlesnake.seta_modo()
        assert battlesnake.modo == 3
        
    def test_battlesnake_modo_nao_setado(self):
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
        }, arena=ARENA)
        
        with pytest.raises(Erro):
            battlesnake.movimenta()
            
    def test_battlesnake_modo_invalido(self):
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
        }, arena=ARENA)
        battlesnake.modo = -1
        with pytest.raises(Erro):
            battlesnake.movimenta()
            
    def test_battlesnake_movimento_primeiro_modo_1(self):
        battlesnake = BattleSnake(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0},
                {"x": 0, "y": 1},
                {"x": 0, "y": 2},
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
        }, arena=ARENA)
        battlesnake.seta_modo()
        assert battlesnake.modo == 1
        assert battlesnake.movimenta() == "right"
        
    def test_battlesnake_movimento_primeiro_modo_2(self):
        battlesnake = BattleSnake(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 2},
                {"x": 0, "y": 3},
                {"x": 0, "y": 4},
            ],
            "latency": "123",
            "head": {"x": 0, "y": 2},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        }, arena=ARENA_2)
        battlesnake.seta_modo()
        assert battlesnake.modo == 1
        assert battlesnake.movimenta() == "right"
    
    def test_battlesnake_movimento_primeiro_modo_derrota(self):
        battlesnake = BattleSnake(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0},
                {"x": 1, "y": 0},
                {"x": 2, "y": 0},
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
        }, arena=ARENA_2)
        battlesnake.seta_modo()
        assert battlesnake.modo == 1
        with pytest.raises(Erro):
            battlesnake.movimenta()
            
    def test_battlesnake_movimento_segundo_modo_1(self):
        battlesnake = BattleSnake(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 0, "y": 0},
                {"x": 1, "y": 0},
                {"x": 2, "y": 0},
                {"x": 3, "y": 0}
            ],
            "latency": "123",
            "head": {"x": 3, "y": 0},
            "length": 4,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        }, arena=ARENA_2)
        battlesnake.seta_modo()
        assert battlesnake.modo == 2
        
        assert battlesnake.movimenta() == "right"
        
    def test_battlesnake_movimento_terceiro_modo_1(self):
        battlesnake = BattleSnake(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 5, "y": 5},
                {"x": 5, "y": 6},
                {"x": 5, "y": 7},
                {"x": 5, "y": 8}
            ],
            "latency": "123",
            "head": {"x": 5, "y": 5},
            "length": 4,
            "shout": "why are we shouting??",
            "squad": "1",
            "customizations":{
                "color":"#26CF04",
                "head":"smile",
                "tail":"bolt"
            }
        }, arena=ARENA)
        battlesnake.seta_modo()
        assert battlesnake.modo == 3
        
        assert battlesnake.movimenta() in ["down", "left"]
        
    def test_battlesnake_movimento_terceiro_modo_2(self):
        battlesnake = BattleSnake(body={
            "id": "totally-unique-snake-id",
            "name": "Sneky McSnek Face",
            "health": 54,
            "body": [
                {"x": 5, "y": 4},
                {"x": 5, "y": 5},
                {"x": 5, "y": 6},
                {"x": 5, "y": 7}
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
        }, arena=ARENA)
        battlesnake.seta_modo()
        assert battlesnake.modo == 3
        
        assert battlesnake.movimenta() == "left"
        
    
    