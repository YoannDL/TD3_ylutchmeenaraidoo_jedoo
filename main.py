#!/usr/bin/env python3


#!/usr/bin/env python3


def main():
        
    question = str(input("Voulez vous ajouter(+) ou multiplier(*) deux chiffres? "))

    if question == "+":
        from addTwoInt import add
        add()

    elif question == "*":
        from mulTwoInt import mul
        mul()

    else :
        print("Choisissez une operation entre (*) et (+) svp.")
        main()



main()
