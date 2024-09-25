#print ("Hello world !")

#import random

#n = random.randint(1, 100)
#print(n)

#verif = True
#ESSAIS = 3  

#for i in range(ESSAIS):
#    m = int(input("Entrez un numéro: ")) 
#    if m == n:
#        print("Bien joué, c'est bien le numéro !")
#        verif = False
#        break
#    elif m < n:
#        print("Le nombre est plus grand.")
#    else:
#        print("Le nombre est plus petit.")

#if verif: 
#    print(f"Vous avez effectué vos {ESSAIS} essais, le nombre était {n}. Merci.")



import random
import tkinter as tk
from tkinter import messagebox


def verifier_nombre():
    global essais_restants
    try:
        m = int(entree.get())  # Récupère la saisie de l'utilisateur
    except ValueError:
        messagebox.showwarning("Erreur", "Veuillez entrer un nombre valide.")
        return

    if m == n:
        messagebox.showinfo("Félicitations", "Bien joué, c'est bien le numéro !")
        reset_jeu()
    elif m < n:
        result_label.config(text="Le nombre est plus grand.")
    else:
        result_label.config(text="Le nombre est plus petit.")
    
    essais_restants -= 1
    essais_label.config(text=f"Essais restants : {essais_restants}")

    if essais_restants == 0:
        messagebox.showinfo("Dommage", f"Vous avez effectué vos {ESSAIS} essais. Le nombre était {n}.")
        reset_jeu()


def reset_jeu():
    global n, essais_restants
    n = random.randint(1, 100)
    essais_restants = ESSAIS
    result_label.config(text="Tentez votre chance !")
    essais_label.config(text=f"Essais restants : {essais_restants}")
    entree.delete(0, tk.END)


ESSAIS = 3
n = random.randint(1, 100)
essais_restants = ESSAIS


root = tk.Tk()
root.title("Devinez le nombre")


tk.Label(root, text="Devinez le nombre (entre 1 et 100)").pack(pady=10)

entree = tk.Entry(root)
entree.pack(pady=5)

bouton_verifier = tk.Button(root, text="Vérifier", command=verifier_nombre)
bouton_verifier.pack(pady=10)

result_label = tk.Label(root, text="Tentez votre chance !")
result_label.pack(pady=5)

essais_label = tk.Label(root, text=f"Essais restants : {ESSAIS}")
essais_label.pack(pady=5)

reset_jeu()  
root.mainloop()
