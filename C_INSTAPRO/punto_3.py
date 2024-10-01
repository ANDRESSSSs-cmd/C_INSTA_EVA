def invertir_lista(lista):
    lista_invertida = []  # Lista para almacenar los elementos en orden inverso

    for elemento in reversed(lista):  # Recorre la lista en orden inverso
        lista_invertida.append(elemento)  # Agrega cada elemento a la nueva lista

    return lista_invertida


# Ejemplo de uso
lista_original = [1, 2, 3, 4, 5]
nueva_lista = invertir_lista(lista_original)
print(nueva_lista)  # Esto imprimirá [5, 4, 3, 2, 1]
