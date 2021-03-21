def mul():
    x=input("Le premier chiffre svp:")
    while not x.isdigit():
        x=input("La valeur doit etre numerique veuillez entrer votre chiffre svp: ")
    y=input("Le deuxieme chiffre svp:")
    while not y.isdigit():
        y=input("La valeur doit etre numerique veuillez entrer votre chiffre svp: ")
    x = int(x)
    y = int(y)
    z = x*y
    print("Le produit des deux chiffres est" ,z)
    

mul()
