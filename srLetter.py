#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from datetime import datetime

i = 0
fecha=datetime.now()
tiempo_total_procesar = fecha -fecha
tiempo_total_contar = datetime.now() - datetime.now()
tiempo_total = datetime.now() - datetime.now()

for line in sys.stdin:
	delimiters = [","," ",";","\"","-","_","\n"]
	inicio = datetime.now()
	for delim in delimiters:
		split_result = []
		
		for chain in line:
			if(chain != ""):
				split_result += chain.split(delim)
		line = split_result
	i = i + 1
	fin = datetime.now()
	tiempo_linea = fin - inicio 
	tiempo_total_procesar = tiempo_total_procesar + tiempo_linea
	#print "Linea: ",i,"\tContador de letras: ",len(line) ,"TIempo de procesar por linea {}".format(tiempo_linea..microsecond)
	print "",i,"{}".format(tiempo_linea)


print "Tiempo Total: {}".format(tiempo_total_procesar)