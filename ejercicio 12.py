print("") 
print("Complemento: DETERMINAR EL MAYOR Y MENOR.") 
print("")
print ("Ingrese la cantidad de numeros a comparar:") 
lim = int( input())
print ("Ingrese los numeros: ")
n = int( input("Ingrese numero: "))
men = n
may = n
for i in range(1, lim):
    n = int( input("Ingrese numero: "))
    if n < men : men = n
    else:
        if n > may :
            may = n
#Salida
print("\nSALIDA: ") 
print("") 
print ("El numero menor es :" ,men)
print ("El numero mayor es :", may)