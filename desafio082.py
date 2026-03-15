lista=[]
pares=[]
impares=[]

while True:
    num=int(input("Digite um número:"))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    item=" "     
    while item not in "SN":
        item=str(input("Dese continuar? [S/N] ")).upper().strip()[0]
    if item == "N":      
        break
        
print(f"Lista completa: {lista}")
print(f"Lista de Pares: {pares}")
print(f"Lista de Impares: {impares}")