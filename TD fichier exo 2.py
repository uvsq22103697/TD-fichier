def nb_lignes(words):
    ### retourne le nombre de lignes du fichier dont le nom est passé en argument
    f = open(words, "r")
    cpt = 0
    for ligne in f:
        cpt += 1
    f.close() 
    return cpt

print(nb_lignes("words.py"))

def ecrit_liste_mots(n):
    fic_in = open("words.py", "r")
    fic_out = open("words" + str(n) + ".txt", "w")
    for ligne in fic_in :
        if len(ligne) == n + 1 :
            fic_out.write(ligne)



    fic_in.close()
    fic_out.close()

ecrit_liste_mots(5)
print(nb_lignes("words5.txt"))

