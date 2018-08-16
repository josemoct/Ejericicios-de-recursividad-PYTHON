def multiplicar(a,b):
    #print("a= "+str(a)+" b= "+str(b))
    if(b==0):
        return 0
    else:
        return a+multiplicar(a,b-1)
print("Programa para multiplicar dos numeros con sumas")
a = int(input("Escribe el primer numero"))
b = int(input("Escribe el primer numero"))
print(multiplicar(a,b))

    
    
