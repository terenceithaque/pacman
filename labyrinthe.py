# Labyrinthe
import pygame
from random import randint




class Labyrinthe:
    "Labyrinthe"

    def __init__(self, joueur,window, fantomes):
        self.forme = [[3, 3, 3, 3, 3, 3],
                      [1, 2, 2, 2, 2, 2],
                      [1, 0, 0, 0, 0, 2],
                      [1, 0, 0, 2, 0, 2],
                      [1, 0, 0, 1, 0, 2],
                      [1, 0, 0, 0, 0, 2],
                      [2, 2, 2, 2, 2, 2]]  # Forme du labyrinthe sous forme de liste. 0 : le joueur ou les fantômes peuvent passer. 1 : mur, le joueur ou les fantômes ne peuvent pas passer. 2 : pareil que 1, mais pour le haut et le bas du labyrinthe.
        self.joueur = joueur

        self.fantomes = fantomes
        self.cell_height = 80
        self.cell_width = 140
        self.window = window

    def creer(self, screen):
        "Générer un labyrinthe"
        cell_height = self.cell_height
        cell_width = self.cell_width

        border_width = 10

        cell_size = cell_height * cell_width
        for i, row in enumerate(self.forme):
            #print("colonne :", row)
            for j, cell in enumerate(row):
                #print("j :", j)
                #print("cell :", cell)
                if cell > 0 and cell < 2:
                   # print("Dessiné à l'horizontale !")
                    pygame.draw.rect(screen, (0,0,255,1), pygame.Rect(j*cell_width, i*cell_height, cell_width, cell_height), border_width)
                if cell == 2:
                    #print("Dessiné à la verticale !")
                    pygame.draw.rect(screen, (0,0,255,1), pygame.Rect(j*cell_width, i*cell_height, cell_width, cell_height), border_width)
        #self.update(screen)

    """def hit_wall(self):
        "Vérifier si une entité entre en collision avec un mur"
        cell_size = self.cell_height * self.cell_width
        joueur_x = int((self.joueur.rect.x - cell_size/2) / cell_size)
        joueur_y = int((self.joueur.rect.y - cell_size/2) / cell_size)
        if self.forme[joueur_x][joueur_y] >= 1:
            print("Le joueur est entrée en collision avec un mur")
            pygame.time.wait(500)
            self.joueur.cannot_move = True"""

    def obtenir_dimensions(self):
        "Obtenir les dimensions du labyrinthe à l'échelle de la fenêtre de jeu"
        total_width = 1
        total_height = 1
        for liste in self.forme:
            width = 140
            width = width * len(liste)
            total_width = width
            for colonne in enumerate(self.forme):
                print(colonne)
                height = 80
                height = height * len(colonne[1])
                total_height = height

        return total_width, total_height        





            


    def block_move(self):
        "Empêcher le joueur ou les fantômes de dépasser les dimensions du terrain" 
        dimension_terrain_x = self.obtenir_dimensions()[0]
        dimension_terrain_y = self.obtenir_dimensions()[1]
        if self.joueur.rect.x > dimension_terrain_x:
            print("Empêché le joueur de sortir du terrain !")
            self.joueur.rect.x = dimension_terrain_x

        if self.joueur.rect.x < 0:
            print("Empêché le joueur de sortir du terrain !")
            self.joueur.rect.x = 0
           

        if self.joueur.rect.y > dimension_terrain_y:
            print("Empêché le joueur de sortir du terrain !")
            self.joueur.rect.x = dimension_terrain_x 
            

        if self.joueur.rect.y < 0:
            print("Empêché le joueur de sortir du terrain !")
            self.joueur.rect.x = 0 

                      
            

        

    
