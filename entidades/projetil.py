import pygame
import configuracoes

class Projetil(pygame.sprite.Sprite):

    def __init__(self, x,y,direcao,dono="jogador",velocidade=None,cor=None,dano=1):
        super().__init__()
        self.dono=dono
        largura=14
        altura=6
        self.image = pygame.Surface((largura,altura),pygame.SRCALPHA)
        if  cor is None and self.dono =="jogador":
            cor =  configuracoes.COR_PROJETIL_JOGADOR
        elif cor is None:
            cor =  configuracoes.COR_PROJETIL_INIMIGO
        pygame.draw.ellipse(self.image,cor,(0,0,largura,altura))
        self.rect=self.image.get_rect(center=(x,y))
        self.pos = pygame.Vector2(self.rect.center)
        self.velocidade = velocidade if velocidade is not None else configuracoes.VELOCIDADE_TIRO
        self.vel = pygame.Vector2(direcao).normalize * self.velocidade if direcao else pygame.Vector2(0,0)
        self.dano = dano
        self.vida = 90

    def atualizar(self, blocos):
        self.pos += self.vel
        self.rect.center = (round(self.pos.x),round(self.pos.y))
        self.life -= 1
        if (self.vida)<=0:
            self.kill()
            return
        for tile in blocos:
            if self.rect.colliderect(tile):
                self.kill()
                return

    def desenhar(self, surface, camera):
        surface.blit(self.image,camera.apply(self.rect))

                        