lista = []

for i in range(0,5):
    lista.append(int(input("Ingrese un número entero cinco veces:")))

print("Su lista está compuesta por estos cinco números:", lista)    

suma = sum(lista)

print("La suma total de todos los elementos es:",suma)

promedio = suma/len(lista)

print ("El promedio de los elementos es:",promedio)

maxnum = max(lista)

print ("El valor máximo de todos los elementos que contiene la lista es:",maxnum)

minnum = min(lista)

print ("El valor mínimo de todos los elementos que contiene la lista es:",minnum)

print("¡Qué tenga un buen día!")