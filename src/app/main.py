from fastapi import FastAPI
from mangum import Mangum

from .shared.erro import Erro
from .shared.utils import Utils

from .shared.Arena import Arena
from .shared.BattleSnake import BattleSnake



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
    return {"body": "me ignora né safado"}

@app.post("/end")
def end(request: dict):
    """
    link: https://docs.battlesnake.com/api/requests/end
    """
    return {"body": "espero que tenha ganhado, minha cobra é insana"}

@app.post("/move")
def move(request: dict):
    """
    link: https://docs.battlesnake.com/api/requests/move
    """
    response = dict()
    
    # criação do shout 
    message = Utils.escolhe_frase()

    response["shout"] = message
    
    # movimento
    try:
        arena = Arena(body=request["board"])
        batalhadora = BattleSnake(body=request["you"], arena=arena)
        batalhadora.seta_modo()
        movimento = batalhadora.movimenta()
        response["move"] = movimento
        return response
    except Erro as err:
        return {"erro": err.message}

handler = Mangum(app, lifespan="off")
