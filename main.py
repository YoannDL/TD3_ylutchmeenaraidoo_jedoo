#!/usr/bin/env python3


#!/usr/bin/env python3


def add():
    a=input("Le premier chiffre svp:")
    while not a.isdigit():
        a=input("La valeur doit etre numerique veuillez entrer votre chiffre svp")
    b=input("Le deuxieme chiffre svp:")
    while not b.isdigit():
        b=input("La valeur doit etre numerique veuillez entrer votre chiffre svp")
    c=int(a)+int(b)
    print("La somme des deux chiffres est" ,c)
    return 

question=str(input("Voulez vous additioner deux entier?(oui ou non)"))
if question=="oui":
        add()
else :
    print("ok")
