import pygame
import configuracoes
import assets
from personagem import Personagem
from habilidades import Habilidade
from projetil import Projetil

class Jogador(Personagem):

    _SPRITES=None
    _ANIM_SPEED={
        "parado":22,
        "caminhando":7,
        "pulo":1,
        "dash":1
    }