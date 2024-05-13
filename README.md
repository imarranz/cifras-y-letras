
# Cifras y Letras


<p align="center">
  <img src="https://repository-images.githubusercontent.com/794474602/0a00e1e9-4f4f-40ed-9673-31d20c16ae56" alt="Data Science Book Hub">
</p>

<p align="center">
  <a href="https://github.com/imarranz/cifras-y-letras/pulls">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?longCache=true" alt="Pull Requests">
  </a>
  <a href="LICENSE.md">
    <img src="https://img.shields.io/badge/License-MIT-red.svg?longCache=true" alt="MIT License">
  </a>
   <a href="https://github.com/imarranz/cifras-y-letras"><img src="https://img.shields.io/github/stars/imarranz/cifras-y-letras" alt="Stars"/></a>
  </a>
</p>

<p align="center">
  <a href="https://twitter.com/imarranz" target="_blank">
    <img src="https://img.shields.io/twitter/follow/imarranz.svg?logo=twitter">
  </a>
</p>


**Desafío de la Palabra Más Larga**

De lunes a jueves, a las 9:30, todos en mi familia tenemos una cita con el concurso **Cifras y Letras**. Podéis saber más sobre este programa en la web de [RTVE](https://www.rtve.es/play/videos/cifras-y-letras/?media=tve) y en [wikipedia](https://es.wikipedia.org/wiki/Cifras_y_letras). El programa tiene varias pruebas de cálculo y vocabulario. Una de ellas, la prueba de la palabra más larga, es una de la que más nos gusta. En esta prueba a los concursantes se les dará 10 letras al azar, de las cuales uno de los concursantes podrá decidir cuántas serán vocales y con estas 10 letras los concursantes deben construir la palabra más larga.

Este repositorio contiene una librería en Python que he diseñado y desarrollado junto a mis hijos para encontrar la palabra más larga posible a partir de un conjunto de letras proporcionadas en el concurso de **Cifras y Letras**. A mis hijos les encanta ver cómo nuestro propio programa compite contra los concursantes, dándonos una "ventaja" divertida y educativa. Utilizamos un diccionario de la lengua española como base para el análisis y la búsqueda de palabras, lo que hace de este proyecto una gran herramienta tanto para el aprendizaje como para el entretenimiento familiar.

## Objetivos

El principal objetivo de este proyecto es desarrollar una herramienta que pueda analizar rápidamente un conjunto aleatorio de letras y determinar la palabra más larga que se puede formar con ellas, según el [Diccionario de la Lengua Española](https://www.rae.es/).

Otro objetivo que hemos alcanzado con este programa es resolver la siguiente pregunta ¿Cuál es la estrategia óptima a la hora de decidir el número de vocales? ¿4, 5 o 6 vocales?

## Cómo funciona

El programa toma un conjunto de letras como entrada y busca en el diccionario todas las combinaciones posibles para formar palabras. Luego, selecciona la palabra más larga que se ajusta a las letras disponibles.

## Uso

Para usar este programa, simplemente puedes clonar el repositorio y seguir las instrucciones de configuración y ejecución detalladas a continuación:

```bash
git clone https://github.com/imarranz/cifras-y-letras.git
cd cifras-y-letras
```

En nuestro código en Python, podemos cargar la librería _cyl_ y poder trabajar con las diferentes funciones que hemos desarrollado para resolver el reto de la palabra más larga.

```bash
from cyl import cuantas_vocales, cuantas_letras, generar_juego, es_solucion, mejor_solucion, reemplazar_acentos
```

## Configuración

Asegúrate de tener Python instalado en tu sistema. Puedes descargar Python desde [aquí](https://www.python.org/downloads/). Además, necesitarás instalar algunas dependencias. Puedes hacerlo usando [conda](https://docs.conda.io/en/latest/):

```bash
conda env create -f environment.yml
conda activate cifrasyletras
```

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Si tienes sugerencias para mejorar el algoritmo o añadir nuevas funcionalidades, no dudes en hacer un _fork_ del repositorio y enviar un [pull request](https://github.com/imarranz/cifras-y-letras/pulls).

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Source

De este [repositorio](https://github.com/JorgeDuenasLerin/diccionario-espanol-txt) hemos aprendido a descargar el Diccionario de la RAE en [texto](/data/rae.txt), algo fundamental para que funcione este proyecto.



