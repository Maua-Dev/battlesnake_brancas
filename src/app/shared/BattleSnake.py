from typing import List
from .Arena import Arena
from .Cobra import Cobra
from .Ponto import Ponto
from .erro import Erro


class BattleSnake(Cobra):
    """
    link: https://docs.battlesnake.com/api/objects/battlesnake
    """
    __health:int
    __body:List[Ponto]
    __head:Ponto
    __length:int
    modo: int = None
    movimentos: dict = {
        "up": (0,1),
        "down": (0,-1),
        "left": (-1,0),
        "right": (1,0)
    }

    def __init__(self, body:dict, arena: Arena):
        """
        EX:

        body = {
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

        modo: 1, 2, 3
        1: pegar tamanho = 4
            - deve buscar uma comida até ter tamanho = 4
        2: encontrar o centro
            - após atingir o tamanho determinado, deve encontrar o centro de batalha a fim de realizar a estratégia
        3: se manter no centro
            - ficar girando em circulos até morrer/partida acabar

        """
        super().__init__(body=body)
        self.arena = arena

    def seta_modo(self) -> None:
        if self.get_length() < 4:
            self.modo = 1
            return None
        
        centros = self.arena.retorna_centro()
        if str(self.get_head()) not in [str(centro) for centro in centros]:
            self.modo = 2
            return None
        
        else:
            self.modo = 3
            return None
        
    def chega_em_ponto(self, possiveis_movimentos: dict, ponto: Ponto) -> str:
        cabeca = self.get_head()

        for movimento in self.movimentos:
            if cabeca.x + self.movimentos[movimento][0] < 0 or cabeca.y + self.movimentos[movimento][1] < 0 or str(Ponto(
                x=cabeca.x + self.movimentos[movimento][0],
                y=cabeca.y + self.movimentos[movimento][1]
            )) in [str(perigo) for perigo in self.arena.retorna_perigos()]:
                try:
                    possiveis_movimentos.pop(movimento)
                except: pass

        possiveis_movimentos = [(k, v) for k,v in possiveis_movimentos.items()]
        chaves = [v[0] for v in possiveis_movimentos]

        if "right" in chaves and "left" in chaves and cabeca.x != ponto.x:
            direita = [val for val in possiveis_movimentos if val[0] == "right"][0]
            esquerda = [val for val in possiveis_movimentos if val[0] == "left"][0]
            resto = [tp for tp in possiveis_movimentos if tp[0] not in ["right", "left"]]
            if cabeca.x > ponto.x: 
                possiveis_movimentos = [esquerda, direita]
                possiveis_movimentos.extend(resto)
            elif cabeca.x < ponto.x: 
                possiveis_movimentos = [direita, esquerda]
                possiveis_movimentos.extend(resto)
        
        chaves = [v[0] for v in possiveis_movimentos]
        if "up" in chaves and "down" in chaves and cabeca.y != ponto.y:
                cima = [val for val in possiveis_movimentos if val[0] == "up"][0]
                baixo = [val for val in possiveis_movimentos if val[0] == "down"][0]
                resto = [tp for tp in possiveis_movimentos if tp[0] not in ["up", "down"]]
                if cabeca.y > ponto.y:
                    possiveis_movimentos = [baixo, cima]
                    possiveis_movimentos.extend(resto)
                elif cabeca.y < ponto.y:
                    possiveis_movimentos = [cima, baixo]
                    possiveis_movimentos.extend(resto)
            
        
        if len(possiveis_movimentos) == 0:
                raise Erro("Não há movimentos possíveis, derrota da cobra")    
            
        return possiveis_movimentos[0][0]
        
    def movimenta(self) -> None:
        if self.modo == None:
            raise Erro("Modo não setado")
        
        possiveis_movimentos = self.movimentos.copy()

        corpo = self.get_body()
        if len(corpo) < 2:
            raise Erro("Corpo inválido")
        
        cabeca = self.get_head()
        if corpo[0] != cabeca:
            raise Erro("Cabeça não é a primeira na lista que representa o corpo da cobra")

        pescoco = corpo[1]
        if pescoco.x < cabeca.x and pescoco.y == cabeca.y: possiveis_movimentos.pop("left")
        elif pescoco.x > cabeca.x and pescoco.y == cabeca.y: possiveis_movimentos.pop("right")
        elif pescoco.x == cabeca.x and pescoco.y < cabeca.y: possiveis_movimentos.pop("down")
        elif pescoco.x == cabeca.x and pescoco.y > cabeca.y: possiveis_movimentos.pop("up")
        else:
            raise Erro("Pescoco inválido")



        if self.modo == 1: 
            comida = self.encontra_ponto_mais_perto(lista_de_pontos=self.arena.retorna_comidas())
            return self.chega_em_ponto(possiveis_movimentos=possiveis_movimentos, ponto=comida)

        elif self.modo == 2: 
            centros = self.arena.retorna_centro()
            centro = self.encontra_ponto_mais_perto(lista_de_pontos=centros)
            return self.chega_em_ponto(possiveis_movimentos=possiveis_movimentos, ponto=centro)
            
        elif self.modo == 3:
            centros_possiveis = self.arena.retorna_centro()

            for centro in centros_possiveis:
                if centro == cabeca:
                    centros_possiveis.remove(centro)
                    break
            
            for centro in centros_possiveis:
                if centro.x != cabeca.x and centro.y != cabeca.y:
                    centros_possiveis.remove(centro)
                    break

            centros_sem_perigo = []
            for centro in centros_possiveis:
                if str(centro) not in [str(perigo) for perigo in self.arena.retorna_perigos()]:
                    centros_sem_perigo.append(centro) 
            
            if len(centros_sem_perigo) >= 1:
                return self.chega_em_ponto(ponto=centros_sem_perigo[0], possiveis_movimentos=possiveis_movimentos)
                
            else:
                comida = self.encontra_ponto_mais_perto(lista_de_pontos=self.arena.retorna_comidas())
                return self.chega_em_ponto(possiveis_movimentos=possiveis_movimentos, ponto=comida)
                
        
        else:
            raise Erro("Modo inválido")