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
                "length": 5,
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
    
    def test_move_6(self):
        body = {
                    "game":{
                        "id":"ab249877-697a-4d2c-bc05-1b3485856c9d",
                        "ruleset":{
                            "name":"standard",
                            "version":"v1.2.3",
                            "settings":{
                                "foodSpawnChance":15,
                                "minimumFood":1,
                                "hazardDamagePerTurn":0,
                                "hazardMap":"",
                                "hazardMapAuthor":"",
                                "royale":{
                                "shrinkEveryNTurns":0
                                },
                                "squad":{
                                "allowBodyCollisions":False,
                                "sharedElimination":False,
                                "sharedHealth":False,
                                "sharedLength":False
                                }
                            }
                        },
                        "map":"standard",
                        "timeout":500,
                        "source":"custom"
                    },
                    "turn":3,
                    "board":{
                        "height":11,
                        "width":11,
                        "snakes":[
                            {
                                "id":"gs_QMbXX9gPhwVchxJ9dk8dCwTP",
                                "name":"isapizi",
                                "latency":"48",
                                "health":99,
                                "body":[
                                {
                                    "x":5,
                                    "y":10
                                },
                                {
                                    "x":4,
                                    "y":10
                                },
                                {
                                    "x":4,
                                    "y":9
                                },
                                {
                                    "x":5,
                                    "y":9
                                }
                                ],
                                "head":{
                                "x":5,
                                "y":10
                                },
                                "length":4,
                                "shout":"Tá ligado, cachorro do mangue?",
                                "squad":"",
                                "customizations":{
                                "color":"#9370db",
                                "head":"caffeine",
                                "tail":"weight"
                                }
                            },
                            {
                                "id":"gs_cKTHghxDXc7PRmYDvQBMGFKQ",
                                "name":"Scared Bot",
                                "latency":"1",
                                "health":97,
                                "body":[
                                {
                                    "x":10,
                                    "y":3
                                },
                                {
                                    "x":9,
                                    "y":3
                                },
                                {
                                    "x":9,
                                    "y":4
                                }
                                ],
                                "head":{
                                "x":10,
                                "y":3
                                },
                                "length":3,
                                "shout":"",
                                "squad":"",
                                "customizations":{
                                "color":"#000000",
                                "head":"bendr",
                                "tail":"curled"
                                }
                            },
                            {
                                "id":"gs_qBw64K8gdDjpSrgYXFr6Kvy8",
                                "name":"Loopy Bot",
                                "latency":"1",
                                "health":97,
                                "body":[
                                {
                                    "x":5,
                                    "y":0
                                },
                                {
                                    "x":4,
                                    "y":0
                                },
                                {
                                    "x":4,
                                    "y":1
                                }
                                ],
                                "head":{
                                "x":5,
                                "y":0
                                },
                                "length":3,
                                "shout":"",
                                "squad":"",
                                "customizations":{
                                "color":"#800080",
                                "head":"caffeine",
                                "tail":"iguana"
                                }
                            },
                            {
                                "id":"gs_qbchpCMxHPC4D69TmgPd66M4",
                                "name":"Right Bot",
                                "latency":"1",
                                "health":97,
                                "body":[
                                {
                                    "x":4,
                                    "y":5
                                },
                                {
                                    "x":3,
                                    "y":5
                                },
                                {
                                    "x":2,
                                    "y":5
                                }
                                ],
                                "head":{
                                "x":4,
                                "y":5
                                },
                                "length":3,
                                "shout":"",
                                "squad":"",
                                "customizations":{
                                "color":"#33beff",
                                "head":"missile",
                                "tail":"ion"
                                }
                            },
                            {
                                "id":"gs_tthRHJQrjy4WYvJyqH7Y4qXP",
                                "name":"Hungry Bot",
                                "latency":"1",
                                "health":99,
                                "body":[
                                {
                                    "x":3,
                                    "y":0
                                },
                                {
                                    "x":2,
                                    "y":0
                                },
                                {
                                    "x":1,
                                    "y":0
                                },
                                {
                                    "x":1,
                                    "y":1
                                }
                                ],
                                "head":{
                                "x":3,
                                "y":0
                                },
                                "length":4,
                                "shout":"",
                                "squad":"",
                                "customizations":{
                                "color":"#00cc00",
                                "head":"alligator",
                                "tail":"alligator"
                                }
                            }
                        ],
                        "food":[
                            {
                                "x":10,
                                "y":4
                            },
                            {
                                "x":6,
                                "y":0
                            },
                            {
                                "x":0,
                                "y":4
                            },
                            {
                                "x":5,
                                "y":5
                            },
                            {
                                "x":0,
                                "y":5
                            },
                            {
                                "x":8,
                                "y":3
                            }
                        ],
                        "hazards":[
                            
                        ]
                    },
                    "you":{
                        "id":"gs_QMbXX9gPhwVchxJ9dk8dCwTP",
                        "name":"isapizi",
                        "latency":"48",
                        "health":99,
                        "body":[
                            {
                                "x":5,
                                "y":10
                            },
                            {
                                "x":4,
                                "y":10
                            },
                            {
                                "x":4,
                                "y":9
                            },
                            {
                                "x":5,
                                "y":9
                            }
                        ],
                        "head":{
                            "x":5,
                            "y":10
                        },
                        "length":4,
                        "shout":"Tá ligado, cachorro do mangue?",
                        "squad":"",
                        "customizations":{
                            "color":"#9370db",
                            "head":"caffeine",
                            "tail":"weight"
                        }
                    }
        }

        resp = move(request=body)
        assert resp.get("move") == "up"
        assert resp.get("shout") != None

    def test_move_7(self):
        body = {
            "board":{
                "height": 10,
                "width": 10,
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
                    {"x": 4, "y": 4}, 
                    {"x": 5, "y": 4}, 
                    {"x": 5, "y": 5},
                    {"x": 4, "y": 5}
                ],
                "latency": "123",
                "head": {"x": 4, "y": 4}, 
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
        assert resp.get("move") == "up"
        assert resp.get("shout") != None