import py_orb
import cy_orb
import time


"""
Programa: planeta en orbita
autor: David Bojacá
Fecha: octubre/27/2022
"""

""" Ejemplo usando datos del planeta TIERRA"""
""" Datos del planeta por wikipedia"""

# Inicializacion planeta para PTYHON
tierraPy = py_orb.Planet()
tierraPy.x=100*10**3
tierraPy.y=300*10**3
tierraPy.z=700*10**3

tierraPy.vx=2000*10**3
tierraPy.vy=29.87*10**3
tierraPy.vz=0.034*10**3

tierraPy.m =5.9741*10*24


""" Ejemplo usando datos del planeta TIERRA"""
""" Datos del planeta por wikipedia"""

# Inicializacion planeta para CTYHON
tierraCy = cy_orb.Planet()
tierraCy.x= 100*10**3
tierraCy.y= 300*10**3
tierraCy.z= 700*10**3

tierraCy.vx= 2.000*10**3
tierraCy.vy= 29.87*10**3
tierraCy.vz= 0.034*10**3

tierraCy.m = 5.9741*10*24

#variables adicionales
time_span =400
n_steps =2000000


#se crea un formato para la impresion sobre el fichero
formato_datos = "{:.5f},{:.5f}\n"

for i in range (2):
	#toma de tiempos para pyhton 
	inicioPy = time.time()
	py_orb.step_time(tierraPy, time_span, n_steps)
	finalPy = time.time() - inicioPy
	
	#toma de tiempos para pyhton 
	inicioCy = time.time()
	cy_orb.step_time(tierraCy, time_span, n_steps)
	finalCy = time.time() - inicioCy
	
	
	
	with open("tierra.cvs","a") as archivo:
		archivo.write(formato_datos.format(finalPy,finalCy))

