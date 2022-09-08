#====================== EJERCICIOS INTRODUCTORIOS ====================
#==>  EJERCICIO 1 
""" Dada una cantidad de segundos, realice un algoritmo que los convierta a unidades horas,minutos
mostrando en pantalla en formato "horas:minutos"  
"""

'''Seg = int(input("Ingrese una cantidad de segundos : "))
hor = Seg/3600
min= ((hor-int(hor))*60)

print(int(hor)," : ", int(min ))'''


#==>  EJERCICIO 2 
""" ¿Qué radio debe tener una esfera, para que su volumen sea el mismo al de un cubo de lado 5 cm? """

'''from math import pi

radio = ((125*3)/(4*pi))**(1/3)

formato_flotante= format(radio,".2f")

print("El radio que debe tener la esfera para que su volumen sea el mismo que el de un cubo de lado 5cm es: ", formato_flotante, "cm")'''

#==>  EJERCICIO 3 
""" ¿Cuantas veces supera, el area de un cubo, al area de una esfera, si el lado del
cubo es 10 cm. Y el radio de la esfera 2 cm ? """

'''Ac = 100
ra = 2
Ae = (4*pi*(ra**2))
relacion= Ac/Ae
form_flotante= format(relacion,".2f")
print("llas veces que el area del cubo supera el de la esfera es de aproximadamente: ", form_flotante)'''

#==>  EJERCICIO 4 
""" Realice un código, que permita la conversión de millas a km y km a millas """

'''vel= float(input("Ingrese un valor de velocidad:"))

opcion= int(input("digite ""1"" si es en kilometros, digite ""0"" si es en millas:"))

if opcion == 1:

   velf= vel*0.621371
   print("la velocidad es :", velf,"Millas")
else:
   velf1= vel*1.60934
   print("la velocidad es:", velf1, "kilometros")'''


#==>  EJERCICIO 5 
""" Dadas las coordenadas P1(5,4,5) y P2(0,10,9).
Realice un codigo que determine la distancia entre ambos puntos """

'''P1x=5
P1y=4
P1z=5
P2x=0
P2y=10
P2z=9

d = ((P2x-P1x)**2+(P2y-P1y)**2+(P2z-P1z)**2)**(1/2)

print("La distancia entre los dos punto es de :", d )'''


#==>  EJERCICIO 6 
""" La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas, 
con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 3 calificaciones definidas.
Realice un algoritmo que calcule la nota necesaria de la última nota para pasar la materia. """

'''nota1= float(input("ingrese la primera nota:"))
nota2= float(input("ingrese la segunda nota:"))
nota3= float(input("ingrese la tercera nota:"))

prom = nota1*0.15 + nota2*0.25 + nota3*0.20

nota4= ((prom-3)/0.4)*(-1)

print("Para pasar la materia necesita una nota de: ", nota4 ) #Teniendo en cuenta que la nota se pasa en tres.'''
 
#==>  EJERCICIO 7 
""" La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 4 notas,
 con porcentajes de 15%, 25%, 20% y 40%. Si un estudiante tiene las primeras 2 calificaciones definidas.
Realice un algoritmo que calcule la nota necesaria de las dos últimas notas para pasar la materia. """




#==>  EJERCICIO 8 
""" Cuatro compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. El servicio se
prestará solo de ida.
Sin embargo, los cuatro no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre los cuatro.
A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:
            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
JUAN          Si        Si        No        Si    No
CAMILA        Si        Si        No        No    No
JOSE          Si        No        Si        No    No
MARIA         Si        Si        Si        No    No      
¿Cuanto debe pagar cada estudiante? """

'''Juan = 15000*3+10000*2
Camila = 15000*2+10000*3
Jose= 15000*2+10000*3
Maria= 15000*3+10000*2

print("Juan debe pagar:", Juan, "\n Camila debe pagar:", Camila, "\n Jose debe pagar:", Jose, "\n Maria debe pagar:" , Maria)'''

#==>  EJERCICIO 9 
""" El salario mensual de un empleado se calcula teniendo en cuenta el numero de seguros vendidos,
    en donde el precio de cada seguro es de $120000. 
    Para los primeros 20 seguros, la comisión es del 20%.
    Para los siguientes 100 seguros las comisión es del 30%.
    Para los siguientes seguros vendidos. La comisión es de 10%.
    a) Si un empleado vende 435 seguros, ¿cual será su salario?
    b) Para un salario de $10'000.000. ¿Cuántos seguros debe vender?
    c) Si un empleado devenga $15'000.000. ¿Cuantos salarios vendió en promedio al dia? 
       Teniendo en cuenta que solo trabajaba de lunes a jueves """

com = (120000*0.2)*20+(120000*0.3)*100+(120000*0.1)*315
print("El salario para el vendedor 1 es de: ", com)

ventas= ((4080000-10000000)/(120000*0.1))*(-1)

print("el vendedor debe vender ", int(ventas), "seguros para ganarse  10000000")



#==>  EJERCICIO 10 
""" El salario de un empleado de una empresa se calcula, utilizando como base el 
salario minimo, más un apoyo del 10% en transporte, y uno de 5% por gastos varios.
Además se paga una comisión de acuerdo al numero de ventas de los siguientes productos:
           
            precio_unidad  comisión
* Zapatos:    $ 50 000        5%
* Tenis:      $ 70 000        4%  
* Camizas:    $ 40 000        6%
* Corbatas:   $ 25 000        7%
* Pantalon:   $ 35 000        5%
* Blusas:     $ 80 000        3%
* Vestidos:   $ 95 000        2%
* Medias:     $ 10 000        8%
a) Realice un algoritmo que calcule el salario del empleado teniendo en cuenta el numero de ventas realizadas 
b) Uno de los directivos, quiere que la comisión de cada uno de los productos no supere los $2000
   ¿Qué productos deben cambiar en su porcentaje de comision?
c) Otro directivo desea que la comisión de cada producto se fije en $1900, 
   ¿en cuanto se deben fijar las comisiones de los productos"""

#==>  EJERCICIO 11 
""" Un auto acelera de manera uniforme 0.5 km/s², 
a) ¿cuantas horas deben pasar para alcanzar la velocidad de la luz?
b) ¿qué distancia se habrá recorrido? (suponga que es posible alcanzar la velocidad de la luz) """

#==>  EJERCICIO 12 
""" Un proyectil es lanzado verticalmente hacia arriba, calcule la velocidad inicial que debe tener para 
alcanzar una altura dada. """

#==>  EJERCICIO 13 
""" Un proyectil es lanzado siguiendo una trayectoria parabólica, calcule el ángulo y la velocidad inicial
que debe tener para alcanzar una distancia horizontal y vertical dada. """

#==>  EJERCICIO 14 
""" Un atleta inicia su entrenamiento, desde el punto de partida de una pista, a una velocidad constante de 3m/s. 
Diez segundos después otro atleta empieza su recorrido a una velocidad constante de 5m/s. ¿Cuánto tiempo 
habrá pasado para que el segundo atleta alcance al primero? """

#==>  EJERCICIO 15 
""" Dos automoviles realizan una carrera. El primero de ellos acelera a razón constante de 3m/s², el segundo 
a razón de 5m/s². Si el segundo de ellos empieza su recorrido 10 segundos después que el primero ha empezado.
¿Cuanto tiempo habrá transcurrido cuando ambos se encuentran? """
