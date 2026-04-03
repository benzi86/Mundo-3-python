relatorio={}
Gol=[]
relatorio['Nome']= str(input("Nome do jogador: "))
relatorio['Partidas']=int(input(f"Quantas partidas {relatorio['Nome']} jogo? "))
cont=0
for  gols in range(relatorio['Partidas']):
    Gol.append(int(input(f"Quantos gols foram marcados na {cont+1}º partida: ")))    
    relatorio['Gols']=Gol
    total_gols=sum(relatorio['Gols'])
    relatorio['Total']=total_gols
    cont+=1
print("=*="*25)    
print(relatorio)
print("=*="*25)   
for item, valor in relatorio.items(): 
    if item == 'Partidas':
        continue   
    print(f"O campo {item} tem o valor {valor}")   
print("=*="*25)
print(f"O jogador {relatorio['Nome']} jogou {relatorio['Partidas']} partidas.")
for cont, gols in enumerate(Gol):
    print(f"=> Na partida {cont+1}, fez {gols} gols.")
print(f"Foi um total de {relatorio['Total']} gols até agora.")