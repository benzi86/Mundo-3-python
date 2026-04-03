import random
import time
print("*"*40)
print("Mega Sena".center(40,"*"))
print("*"*40)
jogo=[]
opc=int(input("Quantos jogos quer sortear?: "))
for i in range(1,opc+1):
    jogo= random.sample(range(1,61),6)
    jogo.sort()
    print(f"Jogo {i}: {jogo}")
    time.sleep(1)
print("<Boa Sorte>!!!".center(40,"*"))