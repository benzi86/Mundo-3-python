valores= []
num=0
conf=0
num=int(input("Digite um número para a lista:"))
valores.append(num)

while True:    
    conf=str(input("Você deseja continuar? S/N: ")).upper()
    if conf not in "S,N":
        conf=str(input("Digite uma opção válida, S/N: ")).upper()
    if conf == "S":
        num=int(input("Digite um número para a lista:"))                
    elif conf == "N":
        break
    if num not in valores:
        valores.append(num)
    else:
        print("O número já está na lista! Não será inserido..")
valores.sort()
print(valores)