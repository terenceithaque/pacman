# Script principal du jeu
import pygame
from joueur import *
pygame.init()

TIMER_EVENT = pygame.USEREVENT + 1


window = pygame.display.set_mode((800, 600))  # Créer une fenêtre de jeu
pygame.display.set_caption("Pacman !")

image_joueur = "assets/images/pacman.jpg"
joueur = Joueur(image_joueur)  # Créer un joueur


running = True  # Le jeu est en cours d'exécution
pause = False  # Le jeu est-il en pause ?


def set_pause(key):
    "Mettre le jeu en pause"
    global pause

    if key[pygame.K_SPACE]:
        if not pause:
            pause = True
            print("jeu mis en pause")
            pygame.time.wait(10)
        else:
            pause = False
            print("Fin de la pause")
            pygame.time.wait(10)


while running:
    pygame.time.set_timer(TIMER_EVENT, 500)

    keys = pygame.key.get_pressed()  # Obtenir toutes les touches pressées au clavier

    set_pause(keys)

    window.fill((0, 0, 0))
    for evenement in pygame.event.get():  # Pour chaque évènement intercepté durant le jeu
        if evenement.type == pygame.QUIT:  # Si le joueur veut quitter la partie
            running = False

        if evenement.type == TIMER_EVENT:
            set_pause(keys)

    if not pause:
        joueur.move_direction(keys)
        joueur.display_pseudo(window)

        joueur.draw(window)
        pygame.display.flip()
