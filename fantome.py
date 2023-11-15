# Fantôme
import pygame
from random import randint, random


class Fantome(pygame.sprite.Sprite):
    "Fantôme qui doit attraper le joueur"

    def __init__(self, nom, image, joueur_a_attraper, instances):
        super().__init__()
        self.joueur_a_attraper = joueur_a_attraper
        # Charger en mémoire l'image du fantôme
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.x = 0  # Position de départ x du fantôme
        self.y = 0  # Position de départ y du fantôme
        self.rect.x = self.x  # Position x actuelle du fantôme
        self.rect.y = self.y  # Position y actuelle du fantôme
        # Champ de vision en x dans lequel le fantôme peut repérer le joueur
        self.champ_vision_x = self.joueur_a_attraper.rect.x - self.rect.x
        # Champ de vision en y dans lequel le fantôme peut repérer le joueur
        self.champ_vision_y = self.joueur_a_attraper.rect.y - self.rect.y
        self.nom = nom  # Nom du fantôme
        # Direction dans laquelle se dirige le fantôme. 0 = neutre.
        self.direction = 0
        # Permet de repérer les autres instances de cette classe. instances est une liste
        self.instances = instances

        self.nom_font = pygame.font.Font(None, 20)
        self.cannot_move = False

    def move_direction(self):
        "Décider de la direction vers laquelle se diriger"
        if not self.cannot_move:
            self.direction = randint(-2, 2)
        else:
            self.direction = randint(-2, 2)

        for instance in self.instances:
            if instance.nom != self.nom:  # On identifie si l'instance vérifiée est un autre fantôme par son nom
                if self.rect.x == instance.rect.x or self.rect.y == instance.rect.y:
                    print(
                        f"{self.nom} est entré en collision avec {instance.nom} et change de direction.")
                    # Choisir une autre direction
                    self.direction = randint(-2, 2)

        if self.champ_vision_x >= 10 or self.champ_vision_y >= 10:
            if random() <= 0.8:  # 80 % de chances que le fantôme poursuive le joueur s'il le repère. Cela fait comme s'il le "perdait de vue" après un certain moment.
                if self.rect.x != self.joueur_a_attraper.rect.x and self.rect.y != self.joueur_a_attraper.rect.y:
                    print(f"{self.nom} vous a repéré !")
                    self.direction = self.joueur_a_attraper.direction
            else:
                print(f"{self.nom} vous a perdu de vue !")

        self.move(3)

    def move(self, pas):
        "Aller dans une direction"
        if self.direction == 2:
            self.rect.y -= pas
            if self.rect.y < 0:
                self.rect.y = 0
            self.champ_vision_y = self.joueur_a_attraper.rect.y - self.rect.y
            print("champ de vision y:", self.champ_vision_y)

        if self.direction == -2:
            self.rect.y += pas
            if self.rect.y > 500:
                self.rect.y = 500

            self.champ_vision_y = self.joueur_a_attraper.rect.y - self.rect.y

            print("champ de vision y:", self.champ_vision_y)

        if self.direction == -1:
            self.rect.x -= pas
            if self.rect.x < 0:
                self.rect.x = 0

            self.champ_vision_x = self.joueur_a_attraper.rect.x - self.rect.x

            print("champ de vision x:", self.champ_vision_x)

        if self.direction == 1:
            self.rect.x += pas
            if self.rect.x > 690:
                self.rect.x = 690

            self.champ_vision_x = self.joueur_a_attraper.rect.x - self.rect.x

            print("champ de vision x:", self.champ_vision_x)

    def afficher_nom(self, screen):
        "Afficher le nom du fantôme"
        nom_fantome = self.nom_font.render(self.nom, True, (254, 254, 254))
        screen.blit(nom_fantome, (self.rect.x, self.rect.y - 10))

    def draw(self, screen):
        screen.fill((0, 0, 0), self.rect)
        screen.blit(self.image, (self.rect.x, self.rect.y))
