# Script principal du jeu
import pygame
from joueur import *
from fantome import *
from labyrinthe import *
from tkinter import messagebox
pygame.init()
pygame.mixer.init()

TIMER_EVENT = pygame.USEREVENT + 1


window = pygame.display.set_mode((800, 600))  # Créer une fenêtre de jeu
pygame.display.set_caption("Pacman !")



# fantome = Fantome(nom="Joe", image=image_fantome, joueur_a_attraper=joueur)
window = pygame.display.set_mode((800, 600))  # Créer une fenêtre de jeu
pygame.display.set_caption("Pacman !")

image_joueur = "assets/images/pacman_droite.jpg"
joueur = Joueur(image_joueur, )  # Créer un joueur
image_fantome = "assets/images/ghost.png"

noms_fantomes = ["Joe", "Jack", "William", "Averell"]
liste_fantomes = []
fantomes = pygame.sprite.Group()
for i in range(len(noms_fantomes)):
    fantome = Fantome(
        nom=noms_fantomes[i],screen = window, image=image_fantome, joueur_a_attraper=joueur, instances=liste_fantomes)
    fantomes.add(fantome)
    liste_fantomes.append(fantome)


# fantome = Fantome(nom="Joe", image=image_fantome, joueur_a_attraper=joueur)
labyrinthe = Labyrinthe(joueur,window, fantomes)


running = True  # Le jeu est en cours d'exécution
pause = False  # Le jeu est-il en pause ?


def set_pause(event, unpause = True):
    "Mettre le jeu en pause"
    global pause

    if not pause:
        pause = True
        print("jeu mis en pause")
        pause_font = pygame.font.Font(None, 36)
        str_pause = "Pause ! (Touche espace pour reprendre)"
        pause_text = pause_font.render(str_pause, True, (255, 255, 255))
        window.blit(pause_text, (300, 239))
        pygame.display.flip()
    
    else:
            window.fill((0, 0, 0))
            pause = False
            print("Fin de la pause")

def ask_quit(evenement):
    "Demander au joueur s'il souhaite quitter le jeu"
    set_pause(evenement)
    quit = messagebox.askquestion("Quitter le jeu ?", "Souhaitez-vous quitter le jeu ?")
    if quit == "yes":
        return True
    return False        


def play_music():
    pygame.mixer.music.play(-1)




#pygame.display.update()
chemin_musique = "assets/musique/original_theme.mp3"
pygame.mixer.music.load(chemin_musique)
play_music()

def update():
    window.fill((0,0,0))


while running:
    

    pygame.time.set_timer(TIMER_EVENT, 500)

    keys = pygame.key.get_pressed()  # Obtenir toutes les touches pressées au clavier
    #labyrinthe.hit_wall()

   # set_pause(keys)

    for evenement in pygame.event.get():  # Pour chaque évènement intercepté durant le jeu
        if evenement.type == pygame.QUIT or keys[pygame.K_ESCAPE]:  # Si le joueur veut quitter la partie
            if ask_quit(evenement) == True:
                running = False

        if evenement.type == pygame.KEYUP:
            if evenement.key == pygame.K_SPACE:
                set_pause(evenement)

    if not pause:
        update()


        labyrinthe.creer(window)
        labyrinthe.block_move()
        
        joueur.display_pseudo(window)

        joueur.move_direction(keys, window)

        joueur.draw(window)


        for fantome in fantomes:

            fantome.move_direction()
            fantome.afficher_nom()
            fantome.draw()

    
        pygame.display.update()
        

