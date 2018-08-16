def escribir(frase, n):
    print(str(n)+" : "+frase+"\n")
    n-=1
    if(n>0):
        escribir(frase,n)
print("Programa para escribir algo el numero de veces que quiera")
frase = raw_input("Escribe una frase")
n = int(input("Numero de veces que se repite"))
escribir(frase,n)

    
