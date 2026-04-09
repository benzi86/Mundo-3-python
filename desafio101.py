
def voto(ano):
    from datetime import date
    ano_atual=date.today().year    
    conf= ano_atual- ano
    if conf >=16 and conf < 18:
        print(f"Com {conf} anos o voto é FACULTATIVO.")
    elif conf >=18 and conf < 70:
        print(f"Com {conf} anos o voto é OBRIGATÓRIO.")
    elif conf >= 70:
        print(f"Com {conf} anos o voto é NEGADO.")
    else:
        print(f"Com {conf} anos é proibido votar.")
    
    
ano=int(input("Digite o ano de nascimento:"))
voto(ano)