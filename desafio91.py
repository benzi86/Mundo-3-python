import random
import time
from operator import itemgetter
jogo={"jogador1":random.randint(1,6),"jogador2":random.randint(1,6),"jogador3":random.randint(1,6),"jogador4":random.randint(1,6)}
ranking={}
for k,v in jogo.items():
    print(f"O {k} tirou {v} no dado!")    
    time.sleep(1)
print("**Ranking dos jogadores**")
ranking=sorted(jogo.items(), key=itemgetter(1),reverse=True)
cont=0
maior=0
for k,v in ranking:
    print(f"{cont+1}º colocado:{k} com o valor:{v}")    
    cont+=1
    time.sleep(1)
    if v > maior:
        maior=v
        jogador=k
print("=*="*20)
print(f"Parabéns pela vitória *{jogador}* com o maior valor *{maior}*")