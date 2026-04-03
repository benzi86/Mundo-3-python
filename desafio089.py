print(f"{'BOLETIM ONLINE':*^25}")
alunos=[]
while True:
    nome=str(input("Digite o Nome do Aluno(a): "))
    n1=float(input("Digite a Nota 1: "))
    n2=float(input("Digite a Nota 2: "))
    media= (n1+n2)/2
    alunos.append([nome,[n1,n2],media])    
    val=str(input("Deseja continuar [S/N]: ")).upper().strip()
    if val in ("N,n"):
        break
print(f"{'Posição':^1}{'Nome':^10}{'Nota':>12}")
print("-"*35)  
for pos, i in enumerate(alunos):     
    print(f"{pos}", end=" ")
    print(f"{i[0]:^22}",end=" ")
    print(f"{i[2]}")       
while True:
    conf=int(input("Consultar a nota de qual aluno? (999 finaliza!)"))
    if conf <= len(alunos)-1:
        print(f" A nota de {alunos[conf][0]} é: {alunos[conf][1]}")
    if conf == 999:
        print("-"*35)
        print("Obrigado por usar o Boletim online!")
        break
print("-"*35)