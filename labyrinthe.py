# Labyrinthe
import pygame
from random import randint


class Labyrinthe:
    "Labyrinthe"

    def __init__(self, joueur, fantomes):
        self.forme = [[1, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 0],
                      [0, 1, 1, 1, 0],
                      [0, 1, 1, 1, 0],
                      [1, 1, 1, 1, 1]]  # Forme du labyrinthe sous forme de liste. 0 : le joueur ou les fantômes peuvent passer. 1 : mur, le joueur ou les fantômes ne peuvent pas passer.
        self.joueur = joueur

        self.fantomes = fantomes

    def creer(self, screen):
        "Générer un labyrinthe"
        for i, liste in enumerate(self.forme):
            for j, nombre in enumerate(liste):
                if nombre == 1:
                    pygame.draw.line(
                        screen, (200, 200, 200), (j * 60, i * 60), ((j + 1) * 60, (i + 1) * 60))

                self.update(screen)

    def hit_wall(self):
        "Vérifier si une entité entre en collision avec un mur"
        cell_size = 60
        joueur_x = int((self.joueur.rect.x - cell_size/2) / cell_size)
        joueur_y = int((self.joueur.rect.y - cell_size/2) / cell_size)
        print("position x du joueur :", self.joueur.rect.x)
        print("position x du joueur (convertie pour tableau) :", joueur_x)
        print("position y du joueur :", self.joueur.rect.y)
        print("position y du joueur (convertie pour tableau) :", joueur_y)
        if self.forme[joueur_x][joueur_y] >= 1:
            self.joueur.cannot_move = True  # Le joueur ne peut pas traverser le mur
            print("Le joueur entre en collision avec un mur !")

        for fantome in self.fantomes:
            fantome_x = int((fantome.rect.x + cell_size / 2) / cell_size)
            fantome_y = int((fantome.rect.y + cell_size / 2) / cell_size)
            if self.forme[fantome_x][fantome_y] >= 1:
                fantome.cannot_move = True
                print(f"{fantome.nom} entre en collision avec un mur !")

    def update(self, screen):
        pygame.display.flip()