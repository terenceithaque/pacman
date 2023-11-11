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

    def move_direction(self, key):
        "Déplacer le joueur vers le haut, le bas, l'avant et l'arrière"
        if key[pygame.K_UP]:  # Si le joueur presse la touche "flèche vers le haut"
            self.direction = 2
            self.deplacer(3)
        if key[pygame.K_DOWN]:  # Si le joueur presse la touche "flèche vers le bas"
            self.direction = -2
            self.deplacer(3)

        if key[pygame.K_LEFT]:  # Si le joueur presse la touche "flèche vers la gauche"
            self.direction = -1
            self.deplacer(3)

        if key[pygame.K_RIGHT]:  # Si le joueur presse la touche "flèche vers la droite"
            self.direction = 1
            self.deplacer(3)

        if not key:  # Si le joueur ne presse aucune touche
            self.direction = 0   # Remettre la direction sur "neutre"

    def obtenir_direction(self):
        "Obtenir la direction courante du joueur"
        return self.direction

    def deplacer(self, pas):
        "Déplacer le joueur"
        if self.direction == 2:
            print("Je me déplace vers le haut")
            self.rect.y -= pas
            if self.rect.y < -20:
                self.rect.y = -20

            print("self.rect.y :", self.rect.y)

        if self.direction == -2:
            print("Je me déplace vers le bas")
            self.rect.y += pas
            if self.rect.y > 500:
                self.rect.y = 500
            print("self.rect.y :", self.rect.y)

        if self.direction == -1:
            print("Je me déplace vers la gauche")
            self.rect.x -= pas
            if self.rect.x < 0:
                self.rect.x = 0
            print("self.rect.x :", self.rect.x)

        if self.direction == 1:
            print("Je me déplace vers la droite")
            self.rect.x += pas
            if self.rect.x > 690:
                self.rect.x = 690
            print("self.rect.x :", self.rect.x)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
