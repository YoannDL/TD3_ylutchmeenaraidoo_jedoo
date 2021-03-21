def add():
    a=input("Le premier chiffre svp:")
    while not a.isdigit():
        a=input("La valeur doit etre numerique veuillez entrer votre chiffre svp: ")
    b=input("Le deuxieme chiffre svp:")
    while not b.isdigit():
        b=input("La valeur doit etre numerique veuillez entrer votre chiffre svp: ")
    c=a+b
    print("La somme des deux chiffres est" ,c)
    

add()

