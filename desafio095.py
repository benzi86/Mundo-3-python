#Ultimo teste Dicionarios
ficha=[]
copia=[]
while True:      
    relatorio={}
    Gol=[]
    relatorio['Nome']= str(input("Nome do jogador: "))
    relatorio['Partidas']=int(input(f"Quantas partidas {relatorio['Nome']} jogo? "))       
    cont=0            
    for  gols in range(relatorio['Partidas']):
        Gol.append(int(input(f"Quantos gols foram marcados na {cont+1}º partida: ")))
        cont+=1            
        relatorio['Gols']=Gol
        total_gols=sum(relatorio['Gols'])
        relatorio['Total']=total_gols
    copia=relatorio.copy()
    ficha.append(copia)                
    conf=str(input("Deseja continuar? [S/N]:")).upper().strip()       
    if conf in 'N':
        break
print("=*="*25)    
print(ficha)
print("-"*30)
print("Cód.", end=" ")
for i in copia.keys():
    print(f"{i:<14}", end=" ")
print()
print("=*="*25)   
for k,v in enumerate(ficha):    
    print(f"{k:>3}",end=" ")
    for d in v.values():
        print(f"{str(d):<15}", end=" ")
    print()   
print("=*="*25)
while True:
    busca=int(input("Selecione o jogador para ver as estatisticas:(999 para encerrar!)"))
    if busca == 999:
        break
    if busca >= len(ficha):
        print(f"ERRO! Jogador {busca} não está na lista!")
    else:
        print(f"=> Estatiscas do Jogador {ficha[busca]['Nome']}:")
        for i, g in enumerate(ficha[busca]['Gols']):
            print(f"- No jogo {i+1} fez {g} gols.")
    print("-"*40)
print(">>Analise Concluida<<")