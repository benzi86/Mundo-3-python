import random
from time import sleep
#Função
def maior(*num):
    print("Analisando os valores...")
    if len(num) >0:
        tam=len(num)
        for i in num:
            sleep(0.5)
            print(f"{i}",end=" ") 
            
        maior= max(num)
        print(f"Foram informados {tam} números")
        print(f"O maior valor foi {maior}")
    else:       
        print(f"Não foram informados valores!")
        print(f"O maior valor foi 0")
    print("~"*40)
#Programa principal      
maior(1,5,7,10,2)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
    