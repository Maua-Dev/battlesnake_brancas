from src.app.main import info, move


class Test_Main:
    def test_info(self):
        resp = info()
        
        assert resp == {
            "apiversion": "1",
            "author": "EhOBrancas",
            "color": "#2670FF",
            "head": "gamer",
            "tail": "rbc-necktie",
            "version": "1.4.4"
        }

    def test_move_1(self):
        body = {
            "board":{
                "height": 11,
                "width": 11,
                "food": [
                    {"x": 5, "y": 5}, 
                    {"x": 9, "y": 0}, 
                    {"x": 2, "y": 6}
                ],
                "hazards": [
                ],
                "snakes": [
                ]
            },
            "you":{
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
        }

        resp = move(request=body)

        assert resp.get("move") in ["up", "down", "left", "right"]
        assert resp.get("shout") != None
    
    def test_move_2(self):
        body = {
            "board":{
                "height": 11,
                "width": 11,
                "food": [
                    {"x": 5, "y": 5}, 
                    {"x": 9, "y": 0}, 
                    {"x": 2, "y": 6}
                ],
                "hazards": [
                ],
                "snakes": [
                ]
            },
            "you":{
                "id": "totally-unique-snake-id",
                "name": "Sneky McSnek Face",
                "health": 54,
                "body": [
                    {"x": 5, "y": 3}, 
                    {"x": 5, "y": 4}, 
                    {"x": 4, "y": 4}
                ],
                "latency": "123",
                "head": {"x": 5, "y": 3}, 
                "length": 3,
                "shout": "why are we shouting??",
                "squad": "1",
                "customizations":{
                    "color":"#26CF04",
                    "head":"smile",
                    "tail":"bolt"
                }
            }

        }

        resp = move(request=body)

        assert resp.get("move") in ["down", "left", "right"]
        assert resp.get("shout") != None

    def test_move_3(self):
        body = {
            "board":{
                "height": 11,
                "width": 11,
                "food": [
                    {"x": 5, "y": 5}, 
                    {"x": 9, "y": 0}, 
                    {"x": 2, "y": 6}
                ],
                "hazards": [
                ],
                "snakes": [
                ]
            },
            "you":{
                "id": "totally-unique-snake-id",
                "name": "Sneky McSnek Face",
                "health": 54,
                "body": [
                    {"x": 0, "y": 1}, 
                    {"x": 0, "y": 2}, 
                    {"x": 1, "y": 2},
                    {"x": 1, "y": 1}, 
                    {"x": 1, "y": 0}
                    
                ],
                "latency": "123",
                "head": {"x": 0, "y": 1}, 
                "length": 3,
                "shout": "why are we shouting??",
                "squad": "1",
                "customizations":{
                    "color":"#26CF04",
                    "head":"smile",
                    "tail":"bolt"
                }
            }

        }

        resp = move(request=body)

        assert resp.get("move") == "down"
        assert resp.get("shout") != None
    
    def test_move_4(self):
        body = {
            "board":{
                "height": 11,
                "width": 11,
                "food": [
                    {"x": 5, "y": 5}, 
                    {"x": 9, "y": 0}, 
                    {"x": 2, "y": 6}
                ],
                "hazards": [
                ],
                "snakes": [
                ]
            },
            "you":{
                "id": "totally-unique-snake-id",
                "name": "Sneky McSnek Face",
                "health": 54,
                "body": [
                    {"x": 5, "y": 4}, 
                    {"x": 5, "y": 3}, 
                    {"x": 5, "y": 2}
                ],
                "latency": "123",
                "head": {"x": 5, "y": 4}, 
                "length": 3,
                "shout": "why are we shouting??",
                "squad": "1",
                "customizations":{
                    "color":"#26CF04",
                    "head":"smile",
                    "tail":"bolt"
                }
            }

        }
        resp = move(request=body)

        assert resp.get("move") == "up"
        assert resp.get("shout") != None

    def test_move_5(self):
        body = {
            "board":{
                "height": 11,
                "width": 11,
                "food": [
                    {"x": 5, "y": 5}, 
                    {"x": 9, "y": 0}, 
                    {"x": 2, "y": 6}
                ],
                "hazards": [
                ],
                "snakes": [
                ]
            },
            "you":{
                "id": "totally-unique-snake-id",
                "name": "Sneky McSnek Face",
                "health": 54,
                "body": [
                    {"x": 5, "y": 4}, 
                    {"x": 5, "y": 3}, 
                    {"x": 5, "y": 2},
                    {"x": 5, "y": 1}
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
            }

        }
        resp = move(request=body)

        assert resp.get("move") == "left"
        assert resp.get("shout") != None
    