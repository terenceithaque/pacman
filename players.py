# Script pour gérer les différents joueurs
import os 

def pseudo_existe(pseudo):
    "Vérifier si un pseudo a déjà été utilisé par un joueur"
    pseudos_existants = os.listdir("joueurs") # On fait une liste de tous les joueurs, chaque dossier étant équivalent au pseudo d'un joueur.
    if pseudo in pseudos_existants: # Si le pseudo existe déjà
        return True 
    return False

def creer_dossier_joueur(pseudo):
    "Créer un nouveau dossier de joueur"
    if not pseudo_existe(pseudo): # Si le pseudo n'a pas été déjà pris par un joueur
        os.mkdir(f"joueurs/{pseudo}")

def supprimer_dossier_joueur(pseudo):
    "Supprimer le dossier d'un joueur existant"
    if pseudo_existe(pseudo):
        os.rmdir(f"joueurs/{pseudo}") # Supprimer le dossier 
        print(f"Le dossier {pseudo} a été détruit.") 
    