import threading
import time
import logging
import random

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

muestras = []
resultados = []
cantidadDeMuestras = 15
cantidadDeUnidades = 5
tiempoTotal = 0
semaforoAnalisis = threading.Semaphore()

# Contador de tiempo de analisis

def contador():
  global tiempoTotal, cantidadDeMuestras, resultados

  while len(resultados) < cantidadDeMuestras:
    time.sleep(1)
    tiempoTotal += 1
  print(">>> Se analizaron", cantidadDeMuestras, "muestras en un tiempo total de", tiempoTotal, "dias.")


class UnidadDeAnalisis(threading.Thread):
  def __init__(self, name):
    super().__init__()
    self.name = name

  def analizarMuestra(self):
    global muestras, resultados
    
    semaforoAnalisis.acquire()

    while len(muestras) > 0:
      tiempoDeAnalisis = random.randint(1, 15)
      muestras.pop(0)
      logging.info("Analizando muestra. Quedan " + str(len(muestras)) + "\n")

      semaforoAnalisis.release()

      time.sleep(tiempoDeAnalisis)
      logging.info("Muestra analizada! Almacenando resultado\n")
      resultados.append(1)
    else:
      semaforoAnalisis.release()

  def run(self):
    self.analizarMuestra()


# Agrego las muestras a analizar

for i in range(cantidadDeMuestras):
  muestras.append(1)

# Inicio el contador

contador = threading.Thread(target=contador)
contador.start()

# Examino las muestras

for i in range(cantidadDeUnidades):
  UnidadDeAnalisis("Unidad " + str(i+1)).start()
