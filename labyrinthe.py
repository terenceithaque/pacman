# Labyrinthe
import pygame
from random import randint




class Labyrinthe:
    "Labyrinthe"

    def __init__(self, joueur, fantomes):
        self.forme = [[3, 3, 3, 3, 3, 3],
                      [1, 2, 2, 2, 2, 1],
                      [1, 0, 0, 0, 0, 1],
                      [1, 0, 0, 0, 0, 1],
                      [1, 0, 0, 0, 0, 1],
                      [1, 0, 0, 0, 0, 1],
                      [2, 2, 2, 2, 2, 1]]  # Forme du labyrinthe sous forme de liste. 0 : le joueur ou les fantômes peuvent passer. 1 : mur, le joueur ou les fantômes ne peuvent pas passer. 2 : pareil que 1, mais pour le haut et le bas du labyrinthe.
        self.joueur = joueur

        self.fantomes = fantomes

    def creer(self, screen):
        "Générer un labyrinthe"
        cell_height = 80
        cell_width = 140

        border_width = 0

        cell_size = cell_height * cell_width
        for i, row in enumerate(self.forme):
            print("colonne :", row)
            for j, cell in enumerate(row):
                print("j :", j)
                print("cell :", cell)
                if cell > 0 and cell < 2:
                    print("Dessiné à l'horizontale !")
                    pygame.draw.rect(screen, (0,0, 255, 1), pygame.Rect(
                        j*cell_width-border_width, i*cell_height, cell_width-border_width, cell_height))
                    
                if cell == 2:
                    print("Dessiné à la verticale !")
                    pygame.draw.rect(screen,(0,0,255,1), pygame.Rect(j*cell_width-border_width, i*cell_height, cell_width-border_width,cell_height))    

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
