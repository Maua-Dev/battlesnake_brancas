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

    def test_move(self):
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