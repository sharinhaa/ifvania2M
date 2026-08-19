from abc import ABC,abstractmethod
import pygame
import configuracoes

class Personagem(pygame.sprint.Sprite,ABC):

    def __init__(self,
                 x,
                 y,
                 largura,
                 altura,
                 vida):
        super().__init__()
        self.largura,self.altura = largura,altura
        self.pos = pygame.Vector(x,y)
        self.vel = pygame.Vector(0,0)
        self.rect = pygame.Rect(x,y,largura,altura)
        self.maximo_vidas = vida
        self.vidas = vida
        self.vivo = True
        self.contato_dano = 1
        self.imagem=None

    @abstractmethod
    def update(self, *args,**kwargs):
        pass

    def tomar_dano(self,dano,contra_ataque=(0,0)):
        if not self.vivo:
            return
        self.vida -=dano
        if self.vida <=0:
            self.vida = 0
            self.vivo=False
