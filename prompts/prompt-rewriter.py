import sys
from nltk.corpus import wordnet
import random

def reescribir_texto(texto):
    palabras = texto.split()
    reescrito = []

    for palabra in palabras:
        # Obtenemos los sinónimos de la palabra actual
        sinonimos = []
        for synset in wordnet.synsets(palabra):
            for lemma in synset.lemmas():
                sinonimos.append(lemma.name())

        if sinonimos:
            # Reemplazamos la palabra con un sinónimo aleatorio
            sinonimo = random.choice(sinonimos)
            reescrito.append(sinonimo)
        else:
            # Si no se encuentran sinónimos, mantenemos la palabra original
            reescrito.append(palabra)

    # Convertimos la lista de palabras reescritas en un texto nuevamente
    resultado = ' '.join(reescrito)
    return resultado

# Verificar si se proporcionó el texto de entrada como argumento
if len(sys.argv) > 1:
    texto_original = ' '.join(sys.argv[1:])  # Unimos todos los argumentos en un solo texto
else:
    texto_original = input("Ingrese el texto que desea reescribir: ")

texto_reescrito = reescribir_texto(texto_original)

print("Texto original:")
print(texto_original)
print()
print("Texto reescrito:")
print(texto_reescrito)
