import time
import random
import threading

'''
  Sistema base con el que cuenta la empresa actualmente
  Este sistema no es concurrente
'''

muestras = []
resultados = []
cantidadDeMuestras = 15
tiempoTotal = 0

# Contador de tiempo de analisis

def contador():
  global tiempoTotal, cantidadDeMuestras, resultados

  while len(resultados) < cantidadDeMuestras:
    time.sleep(1)
    tiempoTotal += 1
  print(">>> Se analizaron", cantidadDeMuestras, "muestras en un tiempo total de", tiempoTotal, "dias.")


# Unidad de analisis actual

def unidadDeAnalisis():
  global muestras, resultados
  tiempoDeAnalisis = random.randint(1, 15)

  muestras.pop(0)
  print("> Analizando una muestra. Quedan", len(muestras))
  time.sleep(tiempoDeAnalisis)
  print("> Muestra analizada! Almacenando resultado\n")
  resultados.append(1)

# Agrego las muestras a analizar

for i in range(cantidadDeMuestras):
  muestras.append(1)

# Inicio el contador

contador = threading.Thread(target=contador)
contador.start()

# Examino las muestras

while len(muestras) > 0:
  unidadDeAnalisis()
