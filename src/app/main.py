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


@app.post("/start")
def start(request: dict):
    """
    link: https://docs.battlesnake.com/api/requests/start
    """
    return None

@app.post("/end")
def end(request: dict):
    """
    link: https://docs.battlesnake.com/api/requests/end
    """
    return None

@app.post("/move")
def move(request: dict):
    """
    link: https://docs.battlesnake.com/api/requests/move
    """
    response = dict()
    
    # criação do shout 
    message = "sou uma cobra br, não falo inglês miauu"
    response["shout"] = message

handler = Mangum(app, lifespan="off")
