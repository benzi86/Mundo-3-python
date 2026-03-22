matriz=[[],[],[]]
valor=0
for i in range(0,3):
    for j in range(0,3):
        valor=int(input(f"Digite o valor para [{i}, {j}]: "))
        if i == 0 and j<=2:
            matriz[0].append(valor)
        elif i == 1 and j<=2:
            matriz[1].append(valor)
        elif i == 2 and j<=2:
            matriz[2].append(valor)
for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}]",end=" ")
    print()
        
