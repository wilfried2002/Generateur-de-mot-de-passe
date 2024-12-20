import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password(length=12):
    # Définir les ensembles de caractères à utiliser pour le mot de passe
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Assurez-vous que le mot de passe contient au moins un caractère de chaque type
    password = [
        random.choice(string.ascii_lowercase),  # Lettre minuscule
        random.choice(string.ascii_uppercase),  # Lettre majuscule
        random.choice(string.digits),  # Chiffre
        random.choice(string.punctuation)  # Caractère spécial
    ]

    # Remplir le reste du mot de passe avec des caractères aléatoires
    password += random.choices(all_characters, k=length - 4)

    # Mélanger les caractères pour garantir que l'ordre est aléatoire
    random.shuffle(password)

    # Convertir la liste en chaîne et retourner le mot de passe
    return ''.join(password)


# Fonction pour afficher le mot de passe dans la fenêtre
def show_password():
    # Récupérer la longueur entrée par l'utilisateur, sinon utiliser 12 par défaut
    try:
        length = int(entry_length.get())
    except ValueError:
        length = 12  # Si la valeur n'est pas un entier, on utilise 12 par défaut

    # Générer le mot de passe
    password = generate_password(length)

    # Afficher le mot de passe dans le label
    label_password.config(text=f"Mot de passe généré : {password}")


# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur de Mot de Passe Sécurisé")

# Configuration de la fenêtre
root.geometry("400x200")

# Label pour instructions
label_instruction = tk.Label(root, text="Entrez la longueur du mot de passe :")
label_instruction.pack(pady=10)

# Champ de saisie pour la longueur du mot de passe
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Bouton pour générer le mot de passe
button_generate = tk.Button(root, text="Générer", command=show_password)
button_generate.pack(pady=10)

# Label pour afficher le mot de passe généré
label_password = tk.Label(root, text="Mot de passe généré :")
label_password.pack(pady=20)

# Lancer la boucle principale de Tkinter
root.mainloop()
