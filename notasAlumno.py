print("***Programa para calcular la nota final de un alumno***")

#Ingrese la información requerida sobre 10 puntos
nombre = input ("Ingrese el nombre del alumno:""\n")
nota_trab = float (input("Ingrese la nota de trabajos:"'\n'))
nota_lecc = float (input("Ingrese la nota de lecciones: "'\n'))
nota_parti = float (input ("Ingrese la nota de participación: ""\n"))
nota_examfi = float(input("Ingrese la nota del examen final: ""\n"))

#Proceso
T = (nota_trab * 20/100)
L = (nota_lecc * 30/100)
P = (nota_parti * 10/100)
E = (nota_examfi * 40/100)

nota_final =(T + L + P + E)

print("La nota de trabajos ponderada al 20 por ciento es: ",T, '\n')
print("La nota de lecciones ponderada al 30 por ciento es: ",L, '\n')
print("La nota de participación ponderada al 10 por ciento es: ",P, 'In')
print("La nota del examen final ponderada al 40 por ciento es: ",E, '\n')
print("La nota final del alumno es: ",nota_final, '\n')