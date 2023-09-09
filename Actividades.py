#TAREA 1
#Haz un programa que lea 2 números e imprima True si el primero es 20 veces el valor del segundo. Si no, imprime False.
num1=0
num2=0

num1 = int(input ("1:"))
num2 = int(input ("2:"))

if num1 == 20 * num2:
        print(True)

else:
   print (False)


#Haz un programa que lea tres números e imprima el producto de los tres dividido entre la suma de los tres.
num1 = int(input ("1:"))
num2 = int(input ("2:"))
num3 = int(input ("3:"))

multiplicacion= num1 * num2 * num3
suma= num1 + num2 + num3

Resultado= multiplicacion/suma

print (Resultado)




# Haz un programa que lea 3 números e imprima True si están en orden ascendiente. Si no, imprime False.
num1 = int(input ("1:"))
num2 = int(input ("2:"))
num3 = int(input ("3:"))

if num1 < num2 and num2 < num3:
    print(True)
else:
    print(False)



 #Haz un programa lea 4 números e imprima True si todos son negativos. Si alguno es positivo, imprime False.
num1 = int(input ("1:"))
num2 = int(input ("2:"))
num3 = int(input ("3:"))
num4 = int(input ("4:"))

if num1 < 0 and num2 < 0 and num3 < 0 and num4 < 0:
    print(True)
else:
    print(False)



# Haz un programa que lea un número e imprima True si es un número par e imprima False si es un número impar.
num1 = int(input ("Ingrese el numero:"))

if num1 % 2 == 0:
    print(True)
else:
    print(False)



#Haz un programa que lea 3 números e imprima True si el primero es menor que el segundo y si el segundo no es igual al tercero. Si no, imprime false.
num1 = int(input ("1:"))
num2 = int(input ("2:"))
num3 = int(input ("3:"))

if num1 > num2 and num2 != num3:
    print(True)
else:
    print(False)



# Haz un programa que lea 3 números e imprima True si el primero y el segundo son iguales o si el primero es al menos 3 unidades más grande que el segundo. Si no, imprime False.
num1 = int(input ("1:"))
num2 = int(input ("2:"))
num3 = int(input ("3:"))

if num1 == num2 or num1 - num2 >= 3:
    print(True)
else:
    print(False)



#Haz un programa que lea 8 números e imprima el promedio
num1 = int(input ("1:"))
num2 = int(input ("2:"))
num3 = int(input ("3:"))
num4 = int(input ("4:"))
num5 = int(input ("5:"))
num6 = int(input ("6:"))
num7 = int(input ("7:"))
num8 = int(input ("8:"))

print (num1+num2+num3+num4+num5+num6+num7+num8 / 8)









#TAREA 2
#Ej1
Mes = input("ingresa el mes: ").lower()

diasdelmes = {
    "enero": 31,
    "febrero": 28,
    "marzo": 31,
    "abril": 30,
    "mayo": 31,
    "junio": 30,
    "julio": 31,
    "agosto": 31,
    "septiembre": 30,
    "octubre": 31,
    "noviembre": 30,
    "diciembre": 31
}

if Mes in diasdelmes:
    numero_de_dias = diasdelmes[Mes]
    print(f"El mes de {Mes.capitalize()} tiene {numero_de_dias} días.")


#Ej2
dia_semana = input("Día: ")

dia_semana = dia_semana.lower()

dias_semana = {
    "lunes": 1,
    "martes": 2,
    "miércoles": 3,
    "miercoles": 3, 
    "jueves": 4,
    "viernes": 5,
    "sábado": 6,
    "sabado": 6,  
    "domingo": 7
}

if dia_semana in dias_semana:
    posicion = dias_semana[dia_semana]
    print(f"{dia_semana.capitalize()} es el día {posicion} de la semana.")
else:
    print("Dia no valido")

#Ej3
año = int(input("año:"))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("bisiesto.")
else:
    print("No bisiesto")

#Ej4
numero = int(input("Por favor, ingresa un número entero: "))

es_positivo = False
es_par = False
es_menor_que_100 = False

if numero > 0:
    es_positivo = True

if numero % 2 == 0:
    es_par = True

if numero < 100:
    es_menor_que_100 = True

clasificacion = []

if es_positivo:
    clasificacion.append("positivo")
else:
    clasificacion.append("negativo")

if es_par:
    clasificacion.append("par")
else:
    clasificacion.append("impar")

if es_menor_que_100:
    clasificacion.append("menor que 100")
else:
    clasificacion.append("mayor o igual a 100")

print(f"Es un número {', '.join(clasificacion)}.")


#ej5
arreglo = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si']
secuencia = []

indices = [6, 6, 0, 1, 1, 0, 6, 5, 4, 4, 5, 6, 6, 5, 5]

for indice in indices:
    secuencia.append(arreglo[indice])

print(" ".join(secuencia))


#ej6
arreglo = ["Jose Miguel", "Carlos", "Manuel", "Memo"]


cadena_usuario = input("Ingresa una cadena: ")

if cadena_usuario in arreglo:
    resultado = True
else:
    resultado = False

print(resultado)


#Ej7

arreglo = [12, 456, 2, 123]


arreglo_ordenado = sorted(arreglo)


print(arreglo_ordenado)


#Ej8
numeros = []

for i in range(6):
    numero = float(input(f"Ingrese el número {i + 1}: "))  # Convertimos la entrada a tipo float
    numeros.append(numero)

suma_indices_pares = 0
suma_indices_impares = 0

for i in range(len(numeros)):
    if i % 2 == 0:  # Índices pares
        suma_indices_pares += numeros[i]
    else:  # Índices impares
        suma_indices_impares += numeros[i]

resta = suma_indices_pares - suma_indices_impares

print(f"La resta de la suma de los índices pares con la suma de los índices impares es: {resta}")


#Challenge 2
lado = float(input("Lado:"))
diagonal = float(input("Diagonal: "))

if lado == diagonal:
    print("es un cuadrado.")
else:
    print("es un rectángulo.")









#TAREA 3 (EXAMEN)
#Escribe un programa en phyton que sirve para calcular el voltaje en un circuito lineal con corriente y resistencia contrarias. 
#la corriente y resistencia se deben pedir al usuario.
#El voltaje se define por la siguiente formula (ley de ohm) (voltaje x resistencia)

Voltaje= int(input ("Ingrese el voltaje:"))
Corriente= int  (input ("ingrese la corriente:"))
Resistencia= int(input ("ingrese la resistencia:"))

print( Voltaje*Resistencia)

#ejercicio 2:
Precioantiguo= int(input ("Precio antiguo:"))

print(Precioantiguo * 8000 / 100)

#Ejercicio 3:
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")

#Ejercicio 4
#una biblioteca tiene un catalogo de libros (la biblia, el coran, el principito, el diario de grefg, programación en phyton, algoritmos avanzados, quimica, matematicas.)
#ejecuta operaciones sobre la lista y agrega cuatro libros, elimina dos y cambia dos de lugar.
catalogo_libros = ["La Biblia", "El Corán", "El Principito", "El Diario de Grefg", "Programación en Python", "Algoritmos Avanzados", "Química", "Matemáticas"]

libros_nuevos = ["Artes", "Algebra", "Clase tec mty", "Bioingenieria"]
catalogo_libros.extend(libros_nuevos)

catalogo_libros.remove("El Corán")
catalogo_libros.remove("Química")

catalogo_libros[catalogo_libros.index("Programación en Python")] = "Biología"
catalogo_libros[catalogo_libros.index("Matemáticas")] = "Geografía"

for indice, libro in enumerate(catalogo_libros, start=1):
    print(f"{indice}. {libro}")

#Reto 1:
#Calcular area de un triangulo con solo lado del triangulo.
Lado=float(input("Determine una medida:"))
altura = float(input("Ingresa la altura del triángulo: "))

area = (Lado * altura) / 2

print(area)









#TAREA 4
#P1
numero = int(input("ingresa un número: "))
suma = 0
for i in range(0, numero):

    suma = numero + i
    i = i + 1
print(suma)






#P2
total = 0
contador = 0

while True:
    try:
        numero = float(input("Ingresa un número (0 para finalizar): "))
        total += numero
        contador += 1
        
        if numero == 0:
            break  
    except ValueError:
        print("Por favor, ingresa un número válido.")

if contador == 0:
    print("No se ingresaron números.")
else:
    promedio = total / contador
    print(f"El promedio de los números ingresados es: {promedio:.2f}")






#P6
def es_divisible_por_243(numero):
    
    return numero % 243 == 0


numero = int(input("Ingresa un número: "))

if es_divisible_por_243(numero):
    print(f"{numero} es divisible por 243.")
else:
    print(f"{numero} no es divisible por 243.")







#P3
n = int(input("Ingrese la cantidad de artículos en su lista de compras: "))


lista_de_compras = []


for i in range(n):
    articulo = input(f"Ingrese el artículo #{i + 1}: ")
    lista_de_compras.append(articulo)


lista_de_compras.sort()


print("\nLista de compras en orden alfabético:")
for articulo in lista_de_compras:
    print(articulo)








#P4
n = int(input("Ingrese la cantidad de números en la lista: "))


lista_de_numeros = []


for i in range(n):
    numero = int(input(f"Ingrese el número #{i + 1}: "))
    lista_de_numeros.append(numero)


numeros_pares = [num for num in lista_de_numeros if num % 2 == 0]


print("\nNúmeros pares en la lista:")
for numero in numeros_pares:
    print(numero)







#P5
def imprimir_vocales(cadena):
    vocales = "aeiouAEIOU"  
    resultado = ""

    for caracter in cadena:
        if caracter in vocales:
            resultado += caracter

    print(resultado)


entrada = input("Ingresa una cadena de texto: ")


print("\nVocales en la cadena:")
imprimir_vocales(entrada)






#P7
def multiplicarString(cadena, n):
    if n <= 0:
        return ""  
    else:
        resultado = cadena * n
        return resultado


cadena1 = "Hola"
n1 = 3
resultado1 = multiplicarString(cadena1, n1)
print(resultado1)  

cadena2 = "Adios"
n2 = 5
resultado2 = multiplicarString(cadena2, n2)
print(resultado2)  

