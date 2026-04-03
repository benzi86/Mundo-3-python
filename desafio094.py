cadastro={}
pessoas=[]
media=[]
mulher=[]
lista=[]
while True:   
    cadastro['Nome']=str(input("Nome: "))
    cadastro['Sexo']=str(input("Sexo [M/F]: ")).upper().strip()
    cadastro['Idade']=int(input("Idade: "))
    pessoas.append(cadastro.copy())
    media.append(cadastro["Idade"])
    soma=sum(media)/len(pessoas)
    if cadastro["Sexo"] == "F":
        mulher.append(cadastro["Nome"])         
    conf=str(input("Deseja continuar? [S/N]: ")).upper().strip()
    if conf != "S":
        break            
print("*=*"*25)
print(f"O grupo tem {len(pessoas)} pessoas.")
print(f"A média de idade é de {soma:.1f} anos.")
print(f"As mulheres cadastradas foram {mulher}")
print("A lista de pessoas que estão acima da média são:")
for p in pessoas:
    if p["Idade"] >= soma:
        print(" =>",end=" ")
        for k,v in p.items():
            print(f"{k}: {v},",end=" ")
        print()
print("Programa Encerrado!")        