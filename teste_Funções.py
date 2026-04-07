def soma(a,b):# A função soma recebe dois parâmetros, a e b.
    soma = a + b
    print(f"A soma entre {a} e {b} é igual a {soma}")   
    
soma(2,2)
soma(4,5)

def contador(*num):# A função contador recebe um número indeterminado de argumentos, representados por *num.
    print(f"Recebi os valores {num} e são ao todo {len(num)} números.")
    
contador(2,1,7,5,6,10)

def dobra(lst):# A função dobra recebe uma lista(lst) como parâmetro e dobra cada elemento da lista.
    pos=0
    while pos < len(lst):
        lst[pos] *= 2
        pos+=1
    print(f"Lista dobrada: {lst}")
        
valores = [6,3,9,1,0,2]
dobra(valores)
