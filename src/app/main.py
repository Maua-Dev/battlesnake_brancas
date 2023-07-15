from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

"""
GET /
POST /start
POST /move
POST /end
"""

@app.get("/")
def info():
    """
    link: https://docs.battlesnake.com/api/requests/info
    {
        "apiversion": "1",
        "author": "MyUsername",
        "color": "#888888",
        "head": "default",
        "tail": "default",
        "version": "0.0.1-beta"
    }
    """
    return {
        "apiversion": "1",
        "author": "EhOBrancas",
        "color": "#2670FF",
        "head": "gamer",
        "tail": "rbc-necktie",
        "version": "1.4.4"
    }


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/create_item")
def create_item(request: dict):
    item_id = request.get("item_id")
    name = request.get("name")

    return {"item_id": item_id,
            "name": name}   


handler = Mangum(app, lifespan="off")
