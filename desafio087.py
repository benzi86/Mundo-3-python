matriz=[[0,0,0],[0,0,0],[0,0,0]]
sumpar=0
terc=0
for i in range(0,3):
    for j in range(0,3):
        matriz[i][j]=int(input(f"Digite o valor para a posição [{i}] [{j}]:"))   
for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}]",end="")
        if matriz[i][j] %2 == 0:
            sumpar+= matriz[i][j]
        if j == 2:
            terc+=matriz[i][j]
        if i == 0 or matriz[1][j]> maior:
            maior=matriz[1][j]            
    print()
print(f"A soma dos valores pares da matriz é: {sumpar}")
print(f"A soma dos valores da terceira coluna é: {terc}")
print(f"O maior valor da segunda linha é: {maior}")