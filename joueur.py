# Joueur
import pygame
from tkinter import simpledialog, messagebox
from players import *


class Joueur(pygame.sprite.Sprite):
    "Joueur"

    def __init__(self, chemin_image):
        super().__init__()
        self.images = self.preload_images(["assets/images/pacman_droite.jpg", "assets/images/pacman_bas.png", "assets/images/pacman_gauche.png", "assets/images/pacman_haut.png"]) # Précharger chaque sprite du joueur
        self.pseudo = self.demander_pseudo()
        self.pseudo_font = pygame.font.Font(None, 20)
        # Charger en mémoire l'image du joueur
        self.image = pygame.image.load(chemin_image)
        # Réduire la taille de l'image à 50x50
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        # Direction dans laquelle le joueur se déplace. 0 = neutre.
        self.direction = 0
        self.x = 0  # Position x de départ du joueur
        self.y = 0  # Position y de départ du joueur
        self.rect.x = self.x  # Position x actuelle du joueur
        self.rect.y = self.y  # Position y actuelle du joueur
        self.cannot_move = False  # Le joueur peut-il avancer ?

    def demander_pseudo(self):
        "Demander au joueur de remplir son pseudo"
        pseudo = simpledialog.askstring(
            "Saisissez votre pseudo", "Renseignez votre pseudo:")  # Pseudo du joueur
        if pseudo == "" or pseudo == None:
            messagebox.showinfo("Votre pseudo sera Joueur anonyme", "Etant donné que vous n'avez renseigné(e) aucun pseudo, vous aurez le pseudo temporaire 'Joueur anonyme'. Cela veut dire que les informations le concernant seront effacées lorsque quelqu'un d'autre n'aura saisit aucun pseudo. ")
            pseudo = "Joueur anonyme"
            supprimer_dossier_joueur(pseudo) # Détruire tout dossier d'un joueur anonyme précédent

        creer_dossier_joueur(pseudo)
        return pseudo    



    def move_direction(self, key, window):
        "Déplacer le joueur vers le haut, le bas, l'avant et l'arrière"
        if self.cannot_move:
            self.direction = 0
        if key[pygame.K_UP]:  # Si le joueur presse la touche "flèche vers le haut"
            self.direction = 2
            self.image = self.images[3]
            self.image = pygame.transform.scale(self.image, (30, 30))
            #window.fill((0,0,0))

            self.deplacer(3)
        if key[pygame.K_DOWN]:  # Si le joueur presse la touche "flèche vers le bas"
            self.direction = -2
            self.image = self.images[1]
            self.image = pygame.transform.scale(self.image, (30, 30))
            #window.fill((0,0,0))

            self.deplacer(3)

        if key[pygame.K_LEFT]:  # Si le joueur presse la touche "flèche vers la gauche"
            self.direction = -1
            
            self.image = self.images[2]
            self.image = pygame.transform.scale(self.image, (30, 30))
            #window.fill((0,0,0))

            self.deplacer(3)

        if key[pygame.K_RIGHT]:  # Si le joueur presse la touche "flèche vers la droite"
            self.direction = 1
            self.image = self.images[0]
            self.image = pygame.transform.scale(self.image, (30, 30))
            #window.fill((0,0,0))


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
            if self.rect.y < 0:
                self.rect.y = 0

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

    def display_pseudo(self, screen):
        "Afficher le pseudo du joueur à l'écran"
        pseudo_joueur = self.pseudo_font.render(
            self.pseudo, True, (255, 255, 255))
        screen.blit(pseudo_joueur, (self.rect.x, self.rect.y - 15))

    def preload_images(self, images):
        "Précharger chaque image du joueur"
        images_chargees = [] # On liste toute image chargée en mémoire
        for image in images: # Pour chaque image qu'on doit charger
            images_chargees.append(pygame.image.load(image)) # On charge chaque image et on l'ajoute à la liste

        return images_chargees    

    def draw(self, screen):
        screen.fill((0, 0, 0), self.rect)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # screen.fill((0, 0, 0))


