# Concurrente - Trabajo Integrador

## Análisis de ADN

Una empresa encargada de hacer análisis de ADN nos contrata para renovar su sistema con el cual examinan las muestras. La principal molestia de los gerentes es que el sistema se demora demasiado tiempo en emitir los resultados de una muestra. Analizar una de estas muestraes un proceso largo y requiere de muchos recursos; un resultado puede llegar a tardar de 1 a 15 días en ser emitido. <br/>

La empresa actualmente cuenta con un `sistema-base` que les permite analizar una muestra por vez de un lote con `n` cantidad de muestras, por lo que no es muy eficiente. Una vez que la unidad emite el resultado, este es almacenado en una base de datos. Cuando se completa el lote de muestras y los resultados fueron totalmente cargados en la base de datos, el sistema informa el `tiempo total` que llevó dicha ejecución. 

Nuestro trabajo es buscar la forma de reducir ese tiempo de análisis para aumentar la cantidad de resultados por día.


## Conclusión

Como se puede observar, el sistema base es muy lento a la hora de analizar una cantidad abundante de muestras. En ambos casos se analizan tan solo 15 muestras; pero en la realidad, esta cantidad es mucho más grandes y analizar cada una puede llegar a tomar meses de procesamiento ya que una sola de éstas puede llegar a pesar más 100 Gigabytes de datos y el tiempo de análisis de una cadena de esa magnitud muy extenso e ineficiente.<br/>
En el ejemplo se puede apreciar cómo utilizar un sistema concurrente reduce el tiempo en hasta más del 50% del total a comparación con un sistema no concurrente. Esto nos permite abarcar una cantidad mucho mayor ADN analizados por tiempo y a su vez analizar cadenas que antes era imposible debido a su tamaño de datos y el tiempo que esto conlleva.

## Source

### Para elegir el problema

- Charla "LOS PROFES NOS CUENTAN: La informática en la biología- Sergio Gonzalez": https://www.youtube.com/watch?v=3nRiaMN6wPY 
  
  **Partes del vídeo destacadas:**
  - Un ADN desde el punto de vista informático: https://youtu.be/3nRiaMN6wPY?t=3139
  - Tamaño de genomas de ADN: https://youtu.be/3nRiaMN6wPY?t=3210
  - Secuenciación: https://youtu.be/3nRiaMN6wPY?t=4058
  - Recursos computacionales: https://youtu.be/3nRiaMN6wPY?t=5004
  
  
### Para armar el código

- Los TPs vistos durante la cursada
