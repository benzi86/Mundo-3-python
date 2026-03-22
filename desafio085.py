#Lista com 7 números para separar os pares e impares
num=[[], []]
valor= 0
for n in range(0,7):
    valor=(int(input(f"Digite o {n+1}º valor: ")))      
    
    if valor %2 == 0:                
        num[0].append(valor) 
               
    else:
        num[1].append(valor)
            
print(f"Os números pares digitados foram: {sorted(num[0])}")
print(f"Os números ímpares digitados foram: {sorted(num[1])}") 