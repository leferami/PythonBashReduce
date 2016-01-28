#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from datetime import datetime

inc = 0
fecha=datetime.now()
tiempo_operacion_inicial = fecha -fecha
tiempo_operacion_final = datetime.now() - datetime.now()
tiempo_operacion_total = datetime.now() - datetime.now()

tiempo_inicial = fecha -fecha
tiempo_final = datetime.now() - datetime.now()
tiempo_total = datetime.now() - datetime.now()

for line in sys.stdin:
	tiempo_inicial = datetime.now()
	delimiters = [","," ",";","\"","-","_","\n"]
	##inicio = datetime.now()
	for delim in delimiters:
		split_result = []
		
		for chain in line:
			if(chain != ""):
				split_result += chain.split(delim)
		line = split_result

	for char in line:
		if(chain != ""):
			if len(char) != 0 :
				number = (ord(char))
			tiempo_operacion_inicial = datetime.now()
			#Desplazar letra
			desplazo = (int(number) + 100)
			#Alragamiento de letra
			alargado = desplazo * 250
			#Resto a la letra original
			resto = alargado - number
			#Hallo su raiz cuadrada
			raiz = pow(resto, 0.5)
			#print raiz
			#Incremento
			inc = inc + raiz
			tiempo_operacion_final = datetime.now()

			tiempo_operacion_total = tiempo_operacion_total +(tiempo_operacion_final - tiempo_operacion_inicial)
	tiempo_final = datetime.now()
	tiempo_total = tiempo_total + (tiempo_final -tiempo_inicial)

#print inc

	#fin = datetime.now()
	#tiempo_linea = fin - inicio 
	#tiempo_total_procesar = tiempo_total_procesar + tiempo_linea
	#print "Linea: ",i,"\tContador de letras: ",len(line) ,"TIempo de procesar por linea {}".format(tiempo_linea..microsecond)
	#print "",i,"{}".format(tiempo_linea)

print "Tiempo de operaciones: {}".format(tiempo_operacion_total)
print "Tiempo Total: {}".format(tiempo_total)
#print "Tiempo Total: {}".format(tiempo_total_procesar)