def verificar_palíndromo(palabra):
    palabra = palabra.replace("","").lower() # Eliminar espacios y convertir a minúsculas
    al_reves = "" # Variable para almacenar la palabra invertida
# Crear la palabra invertida manualmente
    for letra in palabra:
        al_reves = letra + al_reves
# Comparar con la original
    if palabra == al_reves:
        return True
    else:
        return False
# Pedir entrada al usuario
texto_ingresado = input("Escribe una palabra o frase en minúsculas: ")
# Mostrar resultado
if verificar_palíndromo(texto_ingresado):
    print("¡Es un palíndromo!")
else:
    print("¡No es un palíndromo!")