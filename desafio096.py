print("-"*25)
print("Área de Terrenos")
print("-" * 25)

def area(larg, comp):
    area= larg * comp
    print(f"A área de um terreno {larg} x {comp} é de {area}m².")
    
    
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura, comprimento)