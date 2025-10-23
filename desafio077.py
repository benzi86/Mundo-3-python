palavras=("Aprender", "Programar","Linguagem","Python","curso","Estudar","Gratis","praticar","trabalhar","Programador","Futuro")
vogais=("a","e","i","o","u")
for p in palavras:
    print(f"\n A palavra \33[32m{p.upper()}\33[m possui as vogais: ",end="")
    for letra in p:
        if letra.lower() in vogais:
            print(f"{letra.lower()}",end=", ")
           