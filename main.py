# Manejo de fechas en Python
print("Manejo de fechas y horas en Python")

from datetime import datetime, date, timedelta, time
# Creación del primer archivo de texto en replit, que contendrá los ejercicios de manejo de fechas del archivo 'fechasyhoras_1.txt'
file_fechayhora1 = open('fechasyhoras_1.txt', 'w')

# Primera frase del archivo nuevo
file_fechayhora1.write("Ejercicios de manejo de fechas y horas del texto 'fecha_hora1.txt'\n")
file_fechayhora1.write("\n")

# Para acceder al archivo de texto de 'fecha_hora1.txt' debemos abrir el texto en forma de lectura y utilizar el método read()
fechas_horas1 = open('fecha_hora1.txt','r') # E: debo cambiar este texto según el que cree
texto1 = fechas_horas1.read()
# Es importante cerrar este archivo antes de proseguir con el código
fechas_horas1.close()

# Ahora, con el método write, plasmaremos las fechas del archivo subido, en el archivo de texto creado desde acá, y ejecutaremos algunas funciones de fechas
file_fechayhora1.write("- Las fechas del primer texto de la 1 a la 6 en orden: \n")
# Forma de mostrar el texto tomado del archivo subido 'fecha_hora1.txt'
file_fechayhora1.write(texto1)
file_fechayhora1.write("\n")

# Para acceder al archivo de texto de 'fecha_hora1.txt' debemos abrir el texto en forma de lectura y utilizar el método readlines() para que salgan en forma de lista
fechas_horas1 = open('fecha_hora1.txt','r')
texto1lista = fechas_horas1.readlines()
# Es importante cerrar este archivo antes de proseguir con el código
fechas_horas1.close()

# De la manera como está escrito el archivo, cada fecha va acompaña de un '\n', esto debe eliminarse para que las fechas puedan entrar en el formato date. En este paso eliminaremos estos '\n' de cada fecha
print()
print(texto1lista)
print()
fe1 = (texto1lista[1].rstrip('\n'))
fe2 = (texto1lista[2].rstrip('\n'))
fe3 = (texto1lista[3].rstrip('\n'))
fe4 = (texto1lista[4].rstrip('\n'))
fe5 = (texto1lista[5].rstrip('\n'))
fe6 = (texto1lista[6].rstrip('\n'))

# Operaciones entre fechas
file_fechayhora1.write("- Operaciones entre fechas: \n")
file_fechayhora1.write("\n")

# Ejercicio aumentar horas, minutos y segundos
file_fechayhora1.write("- Aumentar horas: \n")
file_fechayhora1.write("\n")

# usamos strptime para convertir el string al formato date
date1 = datetime.strptime(fe1,'%d/%m/%Y %H:%M:%S')
file_fechayhora1.write("Fecha 1: ")
file_fechayhora1.write(str(date1))
print(date1)

# Aumentamos 9 horas la fecha 1 almacenada como date1 y ponemos la respuesta en el archivo 'fechasyhoras_1.txt'
sumar9hours = (date1 + timedelta(hours=9))
file_fechayhora1.write("\nAumentar 9 horas a la fecha 1: ")
file_fechayhora1.write(str(sumar9hours))
print(sumar9hours)

# Aumentamos 18 horas la fecha 1 almacenada como date1 y ponemos la respuesta en el archivo 'fechasyhoras_1.txt'
sumar18hours = (date1 + timedelta(hours=18))
file_fechayhora1.write("\nAumentar 18 horas a la fecha 1: ")
file_fechayhora1.write(str(sumar18hours))
print(sumar18hours)

# Aumentamos 10 seconds la fecha 1 almacenada como date1 y ponemos la respuesta en el archivo 'fechasyhoras_1.txt'
sumar10sec = (date1 + timedelta(seconds=10))
file_fechayhora1.write("\nAumentar 10 segundos a la fecha 1: ")
file_fechayhora1.write(str(sumar10sec))
print(sumar10sec)

# Aumentamos 25 min la fecha 1 almacenada como date1 y ponemos la respuesta en el archivo 'fechasyhoras_1.txt'
sumar25min = (date1 + timedelta(minutes=25))
file_fechayhora1.write("\nAumentar 25 minutos a la fecha 1: ")
file_fechayhora1.write(str(sumar25min))
print(sumar25min)

file_fechayhora1.write("\n")

# Comparararemos 4 fechas, si la comparación es verdadera saldrá True, de otro modo, saldrá False
file_fechayhora1.write("\n- Comparación fecha 2 y fecha 3: \n")

# Verificar si la fecha 2 es menor a la fecha 3
comp1 = fe2 > fe3
file_fechayhora1.write("\nEs la fecha 2 mayor que la fecha 3?: ")

file_fechayhora1.write("\n")

# Escribir la respuesta de la comparación anterior en 'operaciones_fechas_1.txt'
file_fechayhora1.write(str(comp1))
print(comp1)
file_fechayhora1.write("\n")

# Salto de línea
file_fechayhora1.write("\n")

# Restar 2 fechas
file_fechayhora1.write("- Restar 2 fechas: \n")
file_fechayhora1.write("\n")
# usamos strptime para convertir el string al formato date
date4 = datetime.strptime(fe4,'%d/%m/%Y %H:%M:%S')
file_fechayhora1.write("Fecha 4: ")
file_fechayhora1.write(str(date4))
print(date4)

file_fechayhora1.write("\n")
# usamos strptime para convertir el string al formato date
date5 = datetime.strptime(fe5,'%d/%m/%Y %H:%M:%S')
file_fechayhora1.write("Fecha 5: ")
file_fechayhora1.write(str(date5))
print(date5)

file_fechayhora1.write("\n")
# Restar las fechas y mostrar la respuesta en el archivo 'fechasyhoras_2'
file_fechayhora1.write("Resta de la fecha 5 - fecha 4: ")
resta = date5-date4
file_fechayhora1.write(str(resta))
print(resta)

file_fechayhora1.write("\n")
file_fechayhora1.write("\n")
# Disminuir horas
file_fechayhora1.write("- Disminuir horas: \n")
file_fechayhora1.write("\n")
# usamos strptime para convertir el string al formato date
date6 = datetime.strptime(fe6,'%d/%m/%Y %H:%M:%S')
file_fechayhora1.write("Fecha 6: ")
file_fechayhora1.write(str(date6))
print(date6)

# Disminuiremos 5 horas la fecha 6 almacenada como date 6 y ponemos la respuesta en el archivo 'fechasyhoras_1.txt'
restar5hours = (date6 - timedelta(hours=5))
file_fechayhora1.write("\nDisminuir 5 horas a la fecha 6: ")
file_fechayhora1.write(str(restar5hours))
print(restar5hours)

# Disminuimos 16 horas la fecha 6 almacenada como date 6 y ponemos la respuesta en el archivo 'fechasyhoras_1.txt'
restar16hours = (date6 - timedelta(hours=16))
file_fechayhora1.write("\nDisminuir 16 horas a la fecha 6: ")
file_fechayhora1.write(str(restar16hours))
print(restar16hours)

# Disminuir 15 segundos la fecha 6 almacenada como date 6 y ponemos la respuesta en el archivo 'fechasyhoras_1.txt'
restar15sec = (date6 - timedelta(seconds=15))
file_fechayhora1.write("\nDisminuir 15 segundos a la fecha 6: ")
file_fechayhora1.write(str(restar15sec))
print(restar15sec)

# Disminuir 40 minutos la fecha 6 almacenada como date 6 y ponemos la respuesta en el archivo 'fechasyhoras_1.txt'
restar40min = (date6 - timedelta(minutes=40))
file_fechayhora1.write("\nDisminuir 40 minutos a la fecha 6: ")
file_fechayhora1.write(str(restar40min))
print(restar40min)

# Cerrar el archivo 'fechas_horas1.txt'
file_fechayhora1.close()

print("--------"*8)


# Crear y abrir el archivo 'operaciones_fechas_2.txt'
file_fechayhora2 = open('fechasyhoras_2.txt', 'w')

# Primera frase del archivo nuevo
file_fechayhora2.write("Ejercicios de manejo de fechas del texto 'fecha_hora2.txt'\n")
file_fechayhora2.write("\n")

# Para acceder al archivo de texto de 'fechas_2.txt' debemos abrir el texto en forma de lectura y utilizar el método read()
fechas_horas2 = open('fecha_hora2.txt','r')
texto2 = fechas_horas2.read()
# Es importante cerrar este archivo antes de proseguir con el código
fechas_horas2.close()

# Ahora, con el método write, plasmaremos las fechas del archivo subido, en el archivo de texto creado desde acá, y ejecutaremos algunas funciones de fechas
file_fechayhora2.write("- Las fechas del segundo texto de la 1 a la 4 en orden: \n")
# Forma de mostrar el texto tomado del archivo subido 'fechas_2.txt'
file_fechayhora2.write(texto2)
file_fechayhora2.write("\n")

# Para acceder al archivo de texto de 'fechas_2.txt' debemos abrir el texto en forma de lectura y utilizar el método readlines() para que salgan en forma de lista
fechas_horas2 = open('fecha_hora2.txt','r')
texto2lista = fechas_horas2.readlines()
# Es importante cerrar este archivo antes de proseguir con el código
fechas_horas2.close() 

print((texto2lista))
print()

# De la manera como está escrito el archivo, cada fecha va acompaña de un '\n', esto debe eliminarse para que las fechas puedan entrar en el formato date. En este paso eliminaremos estos '\n' de cada fecha
day1 = (texto2lista[1].rstrip('\n'))
day2 = (texto2lista[2].rstrip('\n'))
day3 = (texto2lista[3].rstrip('\n'))
day4 = (texto2lista[4].rstrip('\n'))

print()

# De esta manera, cada fecha queda en modo string, pero para las funciones que usaremos ahora, se requiere que los números de la fecha sean de tipo int, para eso haremos la conversión de manera individual para cada número que está separado por comas

# Cambiar cada número de string a int para la fecha 1 del texto 2, day1 
day1_hour = int(day1[12:14])
print(day1_hour)
day1_min = int(day1[15:17])
print(day1_min)
day1_sec = int(day1[18:20])
print(day1_sec)

# Cambiar cada número de string a int para la fecha 2 del texto 2, day2
day2_hour = int(day2[12:14])
print(day2_hour)
day2_min = int(day2[15:17])
print(day2_min)
day2_sec = int(day2[18:20])
print(day2_sec)

# Cambiar cada número de string a int para la fecha 3 del texto 2, day3 
day3_hour = int(day3[12:14])
print(day3_hour)
day3_min = int(day3[15:17])
print(day3_min)
day3_sec = int(day3[18:20])
print(day3_sec)

# Cambiar cada número de string a int para la fecha 4 del texto 2, day4
day4_hour = int(day4[12:14])
print(day4_hour)
day4_min = int(day4[15:17])
print(day4_min)
day4_sec = int(day4[18:20])
print(day4_sec)

# Empezaremos con los ejercicios
file_fechayhora2.write("\n- Ejercicios con funciones: \n")

# time(): forma de mostrar la hora
file_fechayhora2.write("\n- time(): \n")

# Usar time() colocando los argumentos ya transformados en int 
fech1 = time(day1_hour,day1_min,day1_sec)
file_fechayhora2.write("\nLa hora 1 representada de la manera 1: ")
file_fechayhora2.write(str(fech1))
print(fech1)

# Otra forma de representar esta fecha. Mostrar el resultado en 'fechasyhoras_2.txt'
format2 = ( "{:%H y %M del día}".format(fech1))
file_fechayhora2.write("\nHora 1 representada de la manera 2: ")
file_fechayhora2.write(str(format2))

file_fechayhora2.write("\n")

# time(): forma de mostrar la hora de una manera, y uso de .hour(), .minute(), .second() para ver específicamente cada valor
file_fechayhora2.write("\n- time(), .hour(), .minute(), .second(): \n")

# Usar date colocando los argumentos ya transformados en int 
fech2 = time(day2_hour,day2_min,day2_sec)
# Mostrar la fecha como sale con date
file_fechayhora2.write("\nHora 2: ")
file_fechayhora2.write(str(fech2))
# Mostrar la hora de la hora 2
file_fechayhora2.write("\nHoras de la hora 2: ")
file_fechayhora2.write(str(fech2.hour))
# Mostrar los minutos de hora 2
file_fechayhora2.write("\nMinutos de la hora 2: ")
file_fechayhora2.write(str(fech2.minute))
# Mostrar los segundos de la hora 2
file_fechayhora2.write("\nSegundos de la hora 2: ")
file_fechayhora2.write(str(fech2.second))

print(fech2)

file_fechayhora2.write("\n")

# Comparararemos 4 horas, si la comparación es verdadera saldrá True, de otro modo, saldrá False
file_fechayhora2.write("\n- Comparación fecha 1 y fecha 2: \n")

# Verificar si la hora 1 es mayor que la hora 2
comp = fech1 > fech2
file_fechayhora2.write("\nEs la hora 1 mayor que la hora 2?: ")

file_fechayhora2.write("\n")

# Escribir la respuesta de la comparación anterior en 'fechasyhoras_2.txt'
file_fechayhora2.write(str(comp))
print(comp)
file_fechayhora2.write("\n")

# Creación de las variables fech3 y fech4 donde se almacenarán las horas 3 y 4, respectivamente, en formato time
fech3 = time(day3_hour,day3_min,day3_sec)
fech4 = time(day4_hour,day4_min,day4_sec)

# Verificar si la hora 3 es menor que la hora 4
comp3 = fech3 < fech4
file_fechayhora2.write("\nEs la hora 3 menor que la hora 4?: ")

file_fechayhora2.write("\n")

# Escribir la respuesta de la comparación anterior en 'fechasyhoras_2.txt'
file_fechayhora2.write(str(comp3))
print(comp3)
file_fechayhora2.write("\n")


# Cerramos el archivo 'operaciones_fechas_2.txt'
file_fechayhora2.close()