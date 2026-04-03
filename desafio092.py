from datetime import date
dados={}
dados['Nome']=str(input("Nome: "))
dados['Ano de Nascimento']=int(input("Ano de Nascimento: "))
dados['Carteira']=int(input("Carteira de Trabalho (Digite 0 se não tiver): "))
data_atual=date.today()
ano_atual= data_atual.year
idade= ano_atual-dados['Ano de Nascimento']

print("=*="*25)
if dados['Carteira']!= 0:
    dados['Contratação']=int(input("Ano Contratação "))
    dados['Salário']=float(input("Salário "))
    aposenta=(ano_atual-dados['Contratação'])+35 
else:
    print(f"O nome é {dados['Nome']}")
    print(f"Idade atual {idade}")
    print(f"CTPS nº {dados['Carteira']}")
if dados['Carteira']!= 0:
    print(f"Salário atual {dados['Salário']}")
    print(f"Aposentaria com {aposenta} anos")