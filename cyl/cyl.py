
from numpy.random import choice
from collections import Counter

def cuantas_vocales(palabra):
    """
    Cuenta la cantidad de vocales en una palabra.

    Parameters
    ----------
    palabra : str
        La palabra de la cual contar las vocales.

    Returns
    -------
    int
        El número de vocales en la palabra.

    Examples
    --------
    >>> cuantas_vocales('murciélago')
    5
    """
    palabra = list(palabra)
    vocales = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']
    nvocales = 0
    
    for c in palabra:
        if c in vocales:
            nvocales += 1
    return nvocales

def cuantas_letras(palabra):
    """
    Devuelve la longitud de la palabra proporcionada.

    Parameters
    ----------
    palabra : str
        La palabra de la cual obtener la longitud.

    Returns
    -------
    int
        La longitud de la palabra.

    Examples
    --------
    >>> cuantas_letras('jugar')
    5
    """
    return len(palabra)

def generar_juego(nvocales = 5):
    """
    Genera una secuencia aleatoria de 10 letras con un número específico de vocales.

    Parameters
    ----------
    nvocales : int, optional
        El número de vocales que debe tener la secuencia. Por defecto es 5.

    Returns
    -------
    list of str
        La lista de 10 letras con el número especificado de vocales.

    Examples
    --------
    >>> generar_juego(3)
    ['a', 'e', 'i', 'b', 'c', 'd', 'f', 'g', 'h', 'j']  # Ejemplo de salida
    """
    
    palabra = ''
    
    letras = list('bcdfghjklmnñpqrstvwxyz')
    vocales = list('aeiou')
    
    palabra = list(choice(vocales, size=nvocales, replace=True)) 
    palabra = palabra + list(choice(letras, size=10 - nvocales, replace=True))
    palabra = list(choice(palabra, size=10, replace=False))
    
    return palabra


def reemplazar_acentos(lista):
    """
    Reemplaza las vocales acentuadas en una lista de caracteres por sus equivalentes sin acento.

    Parameters
    ----------
    lista : list of str
        Lista de caracteres donde cada elemento es una letra que puede tener un acento.

    Returns
    -------
    list of str
        Lista de caracteres con las vocales acentuadas reemplazadas por vocales sin acento.

    Examples
    --------
    >>> reemplazar_acentos(['á', 'é', 'í', 'ó', 'ú'])
    ['a', 'e', 'i', 'o', 'u']
    >>> reemplazar_acentos(['g', 'á', 't', 'ó'])
    ['g', 'a', 't', 'o']

    Notes
    -----
    Esta función utiliza `str.translate` junto con `str.maketrans` para crear un mapeo de caracteres
    y aplicarlo a cada elemento de la lista, sustituyendo las vocales acentuadas por no acentuadas.
    """
    
    # Diccionario de reemplazo con vocales acentuadas y su correspondiente sin acento
    acentos = str.maketrans('áéíóú', 'aeiou')
    
    # Reemplazar los caracteres en cada elemento de la lista
    lista_sin_acentos = [char.translate(acentos) for char in lista]
    
    return lista_sin_acentos

def es_solucion(palabra, diccionario):
    """
    Verifica si una palabra se puede formar con las letras de un diccionario dado.

    Parameters
    ----------
    palabra : list of str
        La lista de letras que componen la palabra a formar.
    diccionario : list of str
        La lista de letras disponibles para formar la palabra.

    Returns
    -------
    bool
        Verdadero si la palabra se puede formar con las letras del diccionario.

    Examples
    --------
    >>> es_solucion(['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])
    True
    """
    
    frecuencia_palabra = Counter(palabra)
    frecuencia_diccionario = Counter(diccionario)
    
    for letra, cantidad in frecuencia_palabra.items():
        if frecuencia_diccionario[letra] < cantidad:
            return False
    return True

def mejor_solucion(propuesta_helena, palabras_candidatas):
    """
    Encuentra la mejor solución de palabra candidata que se puede formar con la propuesta dada.

    Parameters
    ----------
    propuesta_helena : list of str
        La lista de letras propuestas para formar palabras.
    palabras_candidatas : DataFrame
        Un DataFrame con una columna 'Palabra' que contiene las palabras candidatas.

    Returns
    -------
    list
        Una lista con la última palabra que cumple los requisitos, su longitud y la propuesta.

    Examples
    --------
    >>> propuesta = ['a', 'b', 'c']
    >>> candidatas = pd.DataFrame({'Palabra': ['abc', 'abd', 'acd', 'acdb']})
    >>> mejor_solucion(propuesta, candidatas)
    ['abc', 3, 'abc']
    """
    soluciones = []
    
    for palabra in palabras_candidatas['Palabra'].values:
        if es_solucion(reemplazar_acentos(list(palabra)), propuesta_helena):
            soluciones.append([palabra, len(palabra), ''.join(propuesta_helena)])
            
    return soluciones[-1]
