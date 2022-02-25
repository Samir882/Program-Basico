
import numpy as np
import matplotlib.pyplot as plt
#Los import de numpy y matplotlib.pyplot se encuenta la cabecera los cuales nos permiten llamar a librerías 
#En este caso todo lo que venga después de esto es la estructura del código.
print('Programa sobre el tiempo by Samir Moreno')
#Permite mostrar a la persona que ejecute el programa, texto que el programador quiera
Nombre=input("Introduzca su nombre:")
Edad= input("Introduzca su edad:")
#Con input se puede colocar información adicional por parte de la persona que ejecute el programa 
print ('Hola', Nombre, end='.')
print ('Gracias por acceder al web Samir.com, por procesos prácticos va' 
'a ser necesaria su edad para calcular los días de vida, para ello se sabe que tiene', Edad,)


Mes= input('Sabe,¿Cuánto tiempo es en meses?')
Meses=float(input('Entonces, vuelva a colocar su edad, por favor:'))
Mesa=float(input('¿Cuántos meses tiene un año?'))
#Con la herramienta float nos permite hacer una multiplicación entre valores que asigne la persona que ejercute el programa.
p1= Mesa*Meses 
#Realiza una multiplicación entre los valores Mesa y Meses
print ('Entonces tiene', p1 ,'meses')
Dia1= float(input('Copie el numero mostrado anteriormente:'))
Dia2=float(input('Cuanto diria que es el promedio de días en un mes:'))
Dia= Dia1*Dia2
print ('Por lo tanto, usted ha vivido', Dia, 'días')
print("""Entonces con todo ese tiempo vivido, ¿Se encuentra satisfecho?
1)Si    2)No """)
eleccion=input("Coloque 1 o 2, según sea su respuesta")
# La herramienta if nos permite seleccionar entre dos valores para así dar una respuesta u otra.
if eleccion=='1':
    print('Sigua, adelante!!!')
if eleccion=='2':
    print('Levantese y vaya a invertir bien ese tiempo, que todavía hay tiempo')

print('Muchas gracias por su atención' )

#En el caso del print hasta if eleccion se encuentra el cuerpo del programa a ejecutar, por lo tanto en este trabajo al colocar
#numeros solo se utiliza valores de int o enteros para el caso de C++, y dado la multiplicacion nos va a dar valores enteros.


