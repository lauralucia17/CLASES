#06-09-2022

'''Pida a un usuario su nombre y su edad. Determine si es mayor de edad 
y muestre un mensaje en pantalla diciendo:
<NOMBRE>, usted es mayor/menor de edad. '''

'''nombre = input("Ingrese su nombre:")
edad= int(input("Ingrese su edad:"))

if edad >=18:
    print(nombre,"usted es mayor de edad")
else:
    print("Uste es menor de edad")

# o tambien

nombre = input("Ingrese su nombre:")
edad= int(input("Ingrese su edad:"))

if edad >=18:
    print("{},usted es mayor de edad".format(nombre))
else:
    print("{},Usted es menor de edad".format(nombre))'''

''' Realice un programa que calcule el mayor de tres numeros'''

'''num1= int(input(" Ingrese un numero"))
num2= int(input(" Ingrese un numero"))
num3= int(input(" Ingrese un numero"))

if (num1>num2>=num3) or (num1>num3>=num2):
    print("el numero mayor es", num1)
elif (num2>num3>=num1) or (num2>num1>=num3):
    print("el numero mayor es", num2)
else:
    print("el numero mayor es:", num3)'''

''' Salario base 1 000 000
Realice un programa que calcule el salario de un 
vendedor de seguros, teniendo en cuenta las siguientes
condiciones'''

'''Ventas => entre [5, 20] seguros ==> aumenyo del 20% sobr ela base

Ventas => entre [21,50] seguros=> aumento del 30% sobre la base

Ventas => entre [51, infinito] seguros => aumento del 35%'''

'''salario_base = 1_000_000
ventas = int(input("Numero de ventas: "))
salario_total = 0
condicion1 = (5 <= ventas <= 20)
condicion2 = (21 <= ventas <= 50)
condicion3 = (ventas >= 51)

if condicion1:
    salario_total = salario_base + 0.2 * salario_base 
elif condicion2:
    salario_total = salario_base + 0.3 * salario_base 
elif condicion3:
    salario_total = salario_base + 0.35 * salario_base 
print("El salario total es {}".format(salario_total))'''


#########################################################################

'''Una contraseña de un programa, debe incluir:
*Contresaña contenga mayusculas
*Congtreseña contenga minusculas
*contenga números
*Por lo menos 8 caracteres en total

Determine si al ingresar una contraseña, esta cumple con todas las 
anteriores condiciones.'''

'''Una contraseña de un programa, debe incluir:
* Contenga mayusculas
* Contenga minusculas
* Contenga números
* Caracteres especiales
* Por lo menos 8 caracteres en total
Determine si al ingresar una contraseña, esta cumple con todas las 
anteriores condiciones.'''



'''contrasena = str(input("Ingrese una contraseña:"))
validez = False

condicion1 = <Contenga mayusculas>
condicion2 = <Contenga minusculas>
condicion3 = <Contenga números>
condicion4 = <Caracteres especiales>
condicion5 = <Por lo menos 8 caracteres en total>

if (condicion1 and condicion2 and condicion3 and condicion4 and condicion5):
    validez = True
    print("La contraseña es valida")
else:
    validez = False
    print("La contraseña no es valida")'''






    


