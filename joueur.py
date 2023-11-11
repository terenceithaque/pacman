# Joueur
import pygame


class Joueur(pygame.sprite.Sprite):
    "Joueur"

    def __init__(self, chemin_image):
        super().__init__()
        # Charger en mémoire l'image du joueur
        self.image = pygame.image.load(chemin_image)
        # Réduire la taille de l'image à 50x50
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # Direction dans laquelle le joueur se déplace. 0 = neutre.
        self.direction = 0
        self.x = 0  # Position x de départ du joueur
        self.y = 0  # Position y de départ du joueur
        self.rect.x = self.x  # Position x actuelle du joueur
        self.rect.y = self.y  # Position y actuelle du joueur

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
