from src.app.main import info


class Test_App:
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

    # def test_get_item(self):
        
    #     resp = read_item(1)

    #     assert resp == {"item_id": 1}

    # def test_post_item(self):
    #     request = {"item_id": 1,
    #                "name": "test"}

    #     resp = create_item(request)

    #     assert resp == {"item_id": 1,
    #                     "name": "test"}