lista=[]
pessoas=[]
pmaior=[]
pmenor=[]
cont=0
pm=0
pmin=0
while True:
    lista.append(str(input("Digite seu nome:")))
    lista.append(int(input("Digite seu peso:")))
    if len(pessoas) == 0:
        pm=pmin= lista[1]
    else:
        if lista[1] > pm:
            pm= lista[1]
        if lista[1] < pmin:
            pmin= lista[1]
    pessoas.append(lista[:])
    lista.clear()
    conf=str(input("Deseja continuar? [S/N]: ")).upper().strip()
    if conf in "Nn":
        break    
#for person in pessoas: ->Contagem de pessoas com laço for, mais otimizado fazer com len(pessoas)<-
   # if person[1] > 0:
     #   cont+=1
for peso in pessoas:
    if peso[1] > 90:
        pmaior.append(peso[0])       
    elif peso[1] <=89:
       pmenor.append(peso[0]) 
      
print(f"Foram cadastradas {len(pessoas)} pessoas.")
print(f"O maior peso é {pm:.2f} KG  e as pessoas mais pesadas: {pmaior}")
print(f"O menor peso é {pmin:.2f} KG  e as pessoas mais leves: {pmenor}")
