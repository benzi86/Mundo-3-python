lista=[]
cont=1
num=int(input("Digite um número:"))
lista.append(num)
while True:
    valor=str(input("Deseja continuar S/N? ")).upper()
    if valor in "S":
        num=int(input("Digite um número:"))
        lista.append(num)
        cont+=1
    else:
        break
pos=1
for pos, item in enumerate(lista):    
    if item == 5 and 5 in lista:
        print("-*-"*25)      
        print(f"Foram digitados {cont} números.")
        print(f"Lista de valores em ordem descrescente:{sorted(lista, reverse=True)}")
        print(f"O número 5 foi digitado na lista na posição {pos}")
        break
    elif 5 not in lista:
        print("-*-"*25)
        print(f"Foram digitados {cont} números.")
        print(f"Lista de valores em ordem descrescente:{sorted(lista, reverse=True)}")
        print("O número 5 não está na lista.")        
        break


