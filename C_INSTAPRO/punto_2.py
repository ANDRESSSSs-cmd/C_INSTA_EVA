def eliminar_duplicados(lista):
    vista = set()  # Conjunto para rastrear los elementos vistos
    resultado = []  # Lista para almacenar el resultado sin duplicados

    for elemento in lista:
        if elemento not in vista:  # Verifica si el elemento ya fue visto
            vista.add(elemento)  # Agrega el elemento al conjunto
            resultado.append(elemento)  # Agrega el elemento a la lista de resultados

    return resultado


# Ejemplo de uso
lista_original = [1, 2, 2, 3, 4, 4, 5, 5, 6]
nueva_lista = eliminar_duplicados(lista_original)
print(nueva_lista)  # Esto imprimirá [1, 2, 3, 4, 5, 6]

