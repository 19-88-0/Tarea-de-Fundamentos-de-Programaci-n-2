def contar_vocales_en_texto(frase):
    contador_vocales = 0 # Definir la variable dentro de la función
    # Recorrer el texto
    for caracter in frase:
        if caracter in ['a','e','i','o','u','A','E','I','O','U']:
            contador_vocales += 1 # Sumar si es una vocal
    return contador_vocales # Retornar el resultado dentro de la función
# Pedir texto al usuario
texto_usuario = input("Escribe un texto: ")
# Mostrar el resultado
print(f"Cantidad de vocales encontradas: {contar_vocales_en_texto(texto_usuario)}")