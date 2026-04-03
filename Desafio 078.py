valores = []

# Coleta de dados
for v in range(0, 5):
    num = int(input(f"Digite um número na posição {v}: "))
    valores.append(num)

# Identificando maior e menor valores
# Usamos as funções nativas do Python para clareza e eficiência
maior_valor = max(valores)
menor_valor = min(valores)

print("-" * 30)
print(f"A lista completa é: {valores}")

# Exibindo o maior e suas posições (caso haja números repetidos)
print(f"O maior valor digitado foi {maior_valor} nas posições: ", end="")
for i, v in enumerate(valores):
    if v == maior_valor:
        print(f"{i}... ", end="")
print() # Quebra de linha

# Exibindo o menor e suas posições
print(f"O menor valor digitado foi {menor_valor} nas posições: ", end="")
for i, v in enumerate(valores):
    if v == menor_valor:
        print(f"{i}... ", end="")
print()