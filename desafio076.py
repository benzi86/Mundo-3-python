print("_"*40)
print(f"{'Tabela de Preços Hortifrutti':^40}")#centralizar texto
print("_"*40)
itens=("Maçã",9.90, "Banana",3.90,"Uva",11.20,"Mamão",12.85,"Limão",2.99,"Melancia",8.75,"Kiwi",16.90)
for prod in range(0,len(itens),2): #prod é o item da tupla dentro do limite 0 até a quantidade de itens da tupla e pulando 2 casas
    print(f"{itens[prod]:.<32}",end="")    #imprime cada item da tupla em duas casas começando da posição 0 ="Maça". O end faz a proxima impressão começar na mesma linha
    print(f"R${itens[prod+1]:>8.2f}")   #imprime cada item da tupla começando da posição 1, equivalente ao preço e continua a partir dai pulando 2 casas, definido no for