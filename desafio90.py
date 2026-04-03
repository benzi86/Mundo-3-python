print(f"*-*"*25)
print(f"{'Verificador: PASSA ou NÃO PASSA':*^50}")
print('\033[1;32;40m' + 'Atenção: Digite seu nome e sua média para verificar se passou de ano, está de recuperação ou se foi reprovado!' + '\033[m')
aluno= {}
aluno["Nome"]=str(input("Digite o nome: "))
aluno["Nota"]=float(input(f"Digite a nota de {aluno['Nome']}:"))
if aluno["Nota"] < 5:
    aluno["Situação"]="Reprovado"
elif aluno["Nota"] >=7:
    aluno["Situação"]="Aprovado"
else:
    aluno["Situação"]="Recuperação"
print(f"O nome do aluno é {aluno['Nome']}")
print(f"A média de é: {aluno['Nota']}")
print(f"Situção: {aluno['Situação']}")