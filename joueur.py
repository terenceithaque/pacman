# Joueur
import pygame
from pygame.sprite import _Group


class Joueur(pygame.sprite.Sprite):
    "Joueur"

    def __init__(self, chemin_image):
        super().__init__()
        # Charger en mémoire l'image du joueur
        self.image = pygame.image.load(chemin_image)
