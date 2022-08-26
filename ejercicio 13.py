#Decoracion: Nombre del Algoritmo
print("") 
print("Complemento11: CONTAR CUANTOS SON PARES.") 
print("")
#Inicializar
i=1
c=0 
numEntradas = 10
 #proceso
print("Ingrese", numEntradas, "Numeros:") 
while i <= numEntradas:
    n = int( input("Ingrese numero: ")) 
    if n%2 == 0 :
        c=c+1 
    i=i+1
#Salida
print("\nSALIDA: ") 
print("")
print ("En", numEntradas, "numeros enteros hay", c, "numeros pares")