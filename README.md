# PythonBashReduce
Proyecto Sistema Operativo 

##############		Proceso I/O-BOUND  (archivo pequeño)		##############
time ./br -m "localhost" -r /home/hjupiter/bashreduce/srStem.py -i /home/hjupiter/bashreduce/archivoPequeño.txt -o /home/hjupiter/bashreduce/salida.cvs

"localhost"    	== >> Indica cuantos core se ejecutan
-i  			== >> Indica que es un archivo de entrada.
-o  			== >> Indica que es un archivo de salida.


##############		Proceso I/O-BOUND  (archivo grande)		##############
time ./br -r /home/kl/Documents/SistemasOperativos/proyecto2doParcial/bashreduce/srStop.py -m "localhost localhost localhost localhost" -i /home/kl/Documents/SistemasOperativos/proyecto2doParcial/bashreduce/archivoGrande.txt -o /home/kl/Documents/SistemasOperativos/proyecto2doParcial/bashreduce/salida.csv
"localhost"    	== >> Indica cuantos core se ejecutan
-i  			== >> Indica que es un archivo de entrada.
-o  			== >> Indica que es un archivo de salida.

##############		Proceso CPU-BOUND		##############

time ./br -m "localhost" -r /home/josanvel/Escritorio/ProSO/srCPU.py -i /home/josanvel/Escritorio/ProSO/prueba2.txt

time			== >> Indica el tiempo en modo kernel, tiempo modo usuario y tiempo real en ejecutar el script con bashreduce

"localhost"    	== >> Indica cuanto core se ejecuta
-i  			== >> Indica que es un archivo de entrada.
-o  			== >> Indica que es un archivo de salida.

/home/josanvel/Escritorio/ProSO/srCPU.py           	==== >>>   Script en python  con su ruta respectiva.
/home/josanvel/Escritorio/ProSO/prueba2.txt        	==== >>>   Dataset con su ruta respectiva.
