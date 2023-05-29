from collections import Counter
from scipy.stats import chi2
from datetime import datetime

class GeneradorCongruencialLineal:
    def __init__(self, semilla, a, c, m):
        self.semilla = semilla
        self.a = a
        self.c = c
        self.m = m
    
    def generar_numeros(self, cantidad):
        numeros = []
        for _ in range(cantidad):
            self.semilla = (self.a * self.semilla + self.c) % self.m
            numeros.append(self.semilla / self.m)
        #print(numeros)
        return numeros
        

def poker_test(arr):

    # Verificar que se tengan al menos 5 números
    if len(arr) < 5:
        return False
    
    # Convertir los números generados en una lista de cadenas de 2 dígitos
    num_strings = [str(num).zfill(3) for num in arr]
    
    # Contar la frecuencia de cada combinación de 2 dígitos
    freq = Counter(num_strings)
    
    # Verificar si hay alguna combinación repetida
    if any(count > 1 for count in freq.values()):
        return False
    
    return True
def get_numbers(cantidad):

    now = datetime.now()
    milisegundos = int(now.timestamp() * 1000)
    semilla = milisegundos  # Valor inicial
    a = 1103515245    # Multiplicador 333322
    c = 12345    # Incremento
    m = 2 ** 32  # Módulo
    generador = GeneradorCongruencialLineal(semilla, a, c, m) 
    # Generar un array de 50 números pseudoaleatorios
    numeros_aleatorios = generador.generar_numeros(cantidad)

    # Prueba de poker
    es_viable = poker_test(numeros_aleatorios)
    
    if es_viable:
      print("El conjunto de números es viable como números pseudoaleatorios.")
      return numeros_aleatorios
    else:
      print("El conjunto de números no es viable como números pseudoaleatorios.") 
      #print(numeros_aleatorios)

