# Funciones entrada/salida

'''nombre =input("Ingrese su nombre:")
print("su nombre es:", nombre)'''

#Solicite la edad y muestre por pantalla "si es o no mayor de edad"

'''edad=input("ingrese su edad:")
edad=int(edad)
print( edad >= 18 and "Es mayor de edad" or "no es mayor de edad")'''

#SOLICITAR UNA CLAVE Y DECIR SIE S CORRECTA O INCONRRECTA

'''clave_original= 2014
clave_entrada=input("Ingrese la clave:")
if clave_entrada == clave_original:
    print("correcto")
else:
    print("Incorrecto")'''

### Función format##3

'''numero= 192.55
formato_cientifico=format(numero, "e")
print("formato_cientifico" , formato_cientifico)
formato_cientifico= format (numero, ".2e")
print(" formato cientifico con dos decimales", formato_cientifico)
formato_cientifico= format (numero, ".0e")
print(" formato cientifico sin decimales", formato_cientifico)'''

'''numero = 12.5958
formato_flotante= format(numero,".2f")
print("formato flotante:", formato_flotante) '''

#Pasar de formato los siguientes numeros


num1= 0.52941
num2= 2.389

#entero, flotante 2 decimales y 5 decimales, notacion cientifica un decimal y dos decimales

'''formato_entero =  (format(num2, ".0f"))
print(formato_entero)
formato_
'''


'''cadena= "hola mundo"
formato_centrado= format(cadena, "^100")
formato_derecha= format(cadena, ">100")
formato_izquierda= format(cadena, "<100")

print("formato  con ===> \n", formato_centrado)
print("formato  con ===> \n", formato_derecha)
print("formato  con ===> \n", formato_izquierda)'''

#---------- Funciones de conversion-------------


#convertir a binario, octal, hexadecimal

'''decimal=9.23298
conversion_binario= bin()
conversion_octal=oct()
conversion_hex= hex()
print ("===  Decimal   ===>", decimal)
print(" bin, oct, hex ===>", conversion_binario, conversion_octal, conversion_hex)'''

#¿ como hacer lo contario?
 #bin===> decimal
 #oct===> decimal
 #hex===> decimal

'''bin,oct,hex= "1100110", "146", "66"
print("bin a decimal===>", int(bin,2))
print("oct a decimal===>", int(oct,8))
print("hex a decimal===>", int(hex,16))'''

#------------ funcion de ayuda(dir)------------
# Permite ver la funcionalidad
'''cadena="hola mundo"
lista= [1,2,3]
entero =10

print("funcioanlidades para cadena ====> \n", dir(cadena))
print("funcioanlidades para lista ====> \n", dir(lista))
print("funcioanlidades para entero ====> \n", dir(entero))'''

#--------------- Funciones para secuencias------------------

'''print("\n\n Funciones para secuencias ======>")
secuencia=range(1,11,1)
print(list(secuencia))'''

#en range no toma el valor de la derecha y si el salto es 1 no es necesario

# numeros del -10 al 10 con salto 2

'''secuencia=range(-10,11,2)
print(list(secuencia))
#numeros multiplos de 3 desde el -10 al 5
secuencia2=range(-9,6,3)
print(list(secuencia2))
#numeros del 10 al 0
secuencia3=(range(10,-1,-1))
print(list(secuencia3))
#numeros multiplos de 3 y 5 del 1 al 1000, al revés ( o sea multiplos de 15)

secuencia4=(range(990,0,-15))
print(list(secuencia4))'''

#------------------------
# Tamaño: len()
# Suma= sum()
# Min= min()
# Max= max()
# Reversa= reversed()

secuencia= range(1,10000,3)
lista=[1, 2, 3, 4, 5, 6]
print("tamaño secuencia ===> ", len(secuencia))
print("tamaño lista ===> ", len(lista))
print("minimo de secuencia ===>", min(secuencia))
print("Máximo de lista ===>", max(lista))
print("revertir secuencia ===>", list(reversed(secuencia)))
print("revertir lista ===>", list(reversed(lista)))






















