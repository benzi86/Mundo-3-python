from time import sleep
def contagem(Inicio, Fim, Passo):
    if passo > 0:
        Fim+=1
    else:
        Fim-=1   
    for i in range(Inicio,Fim,Passo):        
        print(f"{i}", end=" ")
        sleep(0.5)    
    print("Fim!")
    sleep(0.5)
    print("~"*40)
print("~"*40)   
print("Contagem de 1 até 10 de 1 em 1")    
contagem(1,11,1)
print("Contagem de 10 até 0 de 2 em 2")
contagem(10,-2,-2)
print("Escolha a contagem desejada.")
inicio= int(input("Inicio: "))
fim= int(input("Fim: "))
passo= int(input("Passo: "))
if passo == 0:
    passo= 1
if inicio > fim and passo >0:
    passo*=-1
elif inicio < fim and passo < 0:
    passo*=-1
print("~"*40)
print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
contagem(inicio,fim,passo)

    
