lista=[]
for v in range(0,5):
    valor=int(input("Digite um número:"))
    if v == 0 or valor>lista[-1]:
        lista.append(valor)
        print("Número foi inserido na última posição.")
    else:
        pos=0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f"Número foi inserido na posição {pos}.")
                break
            pos+=1
print("*-*"*25)
print(f"Os valores digitados formatados em ordem crescente: {lista}")