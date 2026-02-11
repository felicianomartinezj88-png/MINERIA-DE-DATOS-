# EJERCICIO 1: PAR O IMPAR
num1 = 10
if num1 % 2 == 0:
    print("Par")
else:
    print("Impar")

#EJERCICIO 2 Determinar si un número es positivo o negativo
num2= -4
if num2>0: 
    print("El numero es positivo")
elif num2<0:
    print("El numero es negativo")
    
else:  
    print("cero")

# 3. Comprobar si una persona es mayor o menor de edad
edad = 20  
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

#4. Evaluar si un estudiante aprueba una materia
Calif = 80
if Calif >= 60:
    print("Aprobado")
else:
    print("Reprobado")

#5. Clasificar una calificacion en letras(A,B,C,D o F)
nota = 85
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")


# 6. Determinar el estado del agua según la temperatura
temperatura = 25  

if temperatura < 0:
    print("Sólido")
elif 0 <= temperatura <= 100:
    print("Líquido")
else:
    print("Vapor")
