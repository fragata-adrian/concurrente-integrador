import time
import random

# Sistema base con el que cuenta la empresa actualmente
# Este sistema no es concurrente

muestras = []
cantidadDeMuestras = 5
tiempoTotal = 0

# Unidad de analisis actual

def unidadDeAnalisis():
  global tiempoTotal
  tiempoDeAnalisis = random.randint(1, 15)
  tiempoTotal += tiempoDeAnalisis

  muestras.pop(0)
  print("> Analizando una muestra...")
  time.sleep(tiempoDeAnalisis)
  print("> Muestra analizada!\n")

# Agrego las muestras a analizar

for i in range(cantidadDeMuestras):
  muestras.append(1)

# Examino las muestras

while len(muestras) > 0:
  unidadDeAnalisis()

# Imprimo el tiempo total para analizar todas las muestras

print("> Se analizaron", cantidadDeMuestras, "muestras en un tiempo total de", tiempoTotal, "dias.")
