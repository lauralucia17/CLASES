# Crear variables y asignarles los siguientes tipos de datos:

# Enteros: 1,2,3 999
# Luego reste sucesivamente del ultimo al primero y almacenelo
# en una variable llamada resultado1 

a = 1
b = 2
c = 3
d = 999
resultado1 = d-c-b-a
print("Resultado1 = ", resultado1)

# Flotantes: 15.2, 29.5, 18.28
# Luego divida sucesivamente del primero al ultimo
# y almacenelo en una variable llamada resultado2

f1= 15.2
f2=29.5
f3=18.28

resultado2= (f1/f2)/f3
print("resultado2: ", resultado2)


# Strings: "123", "Cristian" 
# Luego sume ambas variables y determine si la 
# operacion es posible, si asi es almacenelo en una variable
# de su eleccion

numero="123"
nombre="Cristian"

suma=numero+nombre
print("el resultado es:", suma)


######## Para pensar ######

# Busque una manera de convertir:
# un entero a un flotante

numt=12
print(float(numt))

# un flotante a un entero
numf=12.1
print(int(numf))
# un string a un entero y flotante
String= "hola"
print(int(String))
print(float(String))

# un numero a un string