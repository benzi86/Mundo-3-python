print("=*="*10)
print("Verificação de Dados")
print("=*="*10)
num1=int(input("Digite o primeiro número:"))
num2=int(input("Digite o segundo número:"))
num3=int(input("Digite o terceiro número:"))
num4=int(input("Digite o quarto e último número:"))
dados=(num1,num2,num3,num4)
cont=0
print(f"Você digitou os valores: {dados}")
print(f"O valor 9 apareceu \33[32m{dados.count(9)} \33[mvezes!")
if 3 in dados:
    print(f"O número 3 apareceu na \33[35m{dados.index(3)+1}º\33[m posição.")
else:
   print("O valor 3 não foi encontrado nessa sequência!")
print("Os valores pares digitados foram:",end="")
for num in dados:
   if num %2 == 0:    
    print(num,end=",")