#EJERCICIO 1
N = int(input("Ingresa el valor de N: "))
suma = 0
for i in range(1, N + 1):
    suma += i
print(f"La suma total es: {suma}")


#EJERCICIO 2

num = int(input("Ingresa un número entero positivo: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"El factorial de {num} es: {factorial}")

#EJERCICIO 3

tabla = int(input("¿Qué tabla deseas obtener?: "))
for i in range(1, 11):
    print(f"{tabla} x {i} = {tabla * i}")

#EJERCICIO 4

suma_notas = 0
contador = 0

for _ in range(1000): # El guion bajo indica que no usaremos la variable del ciclo
    nota = float(input("Ingresa una nota (negativa para terminar): "))
    if nota < 0:
        break
    suma_notas += nota
    contador += 1

if contador > 0:
    print(f"El promedio es: {suma_notas / contador}")

#EJERCICIO 5 

base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
resultado = 1

for i in range(exponente):
    resultado *= base
print(f"El resultado de {base}^{exponente} es: {resultado}")


#EJERCICIO 6

A = int(input("Inicio (A): "))
B = int(input("Fin (B): "))
suma_pares = 0

for i in range(A, B + 1):
    if i % 2 == 0:
        suma_pares += i
print(f"La suma total de pares entre {A} y {B} es: {suma_pares}")