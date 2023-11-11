# Script principal du jeu
import pygame
from joueur import *
pygame.init()


window = pygame.display.set_mode((800, 600))  # Créer une fenêtre de jeu
pygame.display.set_caption("Pacman !")

image_joueur = "assets/images/pacman.jpg"
joueur = Joueur(image_joueur)  # Créer un joueur

running = True  # Le jeu est en cours d'exécution

while running:
    window.fill((0, 0, 0))
    for evenement in pygame.event.get():  # Pour chaque évènement intercepté durant le jeu
        if evenement.type == pygame.QUIT:  # Si le joueur veut quitter la partie
            running = False

    keys = pygame.key.get_pressed()  # Obtenir toutes les touches pressées au clavier
    joueur.move_direction(keys)

    joueur.draw(window)
    pygame.display.flip()
