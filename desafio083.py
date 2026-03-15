pilha=[]
conta=str(input("Digite uma expressão mátematica: "))
for v in conta:
    if v == "(":
        pilha.append("(")
    elif v == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressão está correta.")
else:
    print("Sua expressão está incorreta.")
