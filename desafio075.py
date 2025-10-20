print("Verificação de Dados")
num1=int(input("Digite o primeiro número:"))
num2=int(input("Digite o segundo número:"))
num3=int(input("Digite o terceiro número:"))
num4=int(input("Digite o quarto e último número:"))
dados=(num1,num2,num3,num4)
cont=0
print(f"Você digitou os valores: {dados}")
print(f"O valor 9 apareceu {dados.count(9)} vezes!")
if 3 in dados:
    print(f"O número 3 apareceu na {dados.index(3)+1}º posição.")
else:
   print("O valor 3 não foi encontrado nessa sequência!")
print(f"Os valores pares digitados foram:",end="")
for num in dados:
   if num %2 == 0:    
    print(num,end=",")