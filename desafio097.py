def escreva(palavra):
    tam= len(palavra)+4
    print("~"*tam)
    print(f"{palavra:^{tam}}")
    print("~"*tam)
       
    
escreva("palavra")
escreva("Curso de Python")
escreva("Olá")