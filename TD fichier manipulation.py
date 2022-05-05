def moyenne(liste):
    ### retourne la moyenne des " notes contenus dans la liste
    # à partir de l'indice i"
    return (int(liste[1]) + int(liste[2]) + int(liste[3])) / 3

f_in = open("notes.py", "r")
f_out = open("moyennes", "w")
for ligne in f_in:
    liste = ligne.split()
    moy = moyenne(liste)
    f_out.write(ligne[:-1] + str(moy) + "\n")
    #print(ligne, moy)

f_in.close
f_out.close

