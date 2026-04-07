import random
from time import sleep

def sorteia():      
    print(f"Sorteando 5 valores da lista: ",end="")
    numeros=[]
    for i in range(1,6):
        num=random.randint(1,50)
        numeros.append(num)
        sleep(0.5)
        print(f"{num}", end=" ")        
    print("PRONTO!") 
    return numeros    
  
def somaPar(numeros):
    soma=0
    for valor in numeros:
        if valor %2 == 0:
            soma+= valor
    print(f"A soma dos valores pares da lista {numeros} é: {soma}")
n= sorteia()
somaPar(n)