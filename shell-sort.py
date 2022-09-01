def shell_sort(items_list):
    gap = len(items_list)//2

    while gap > 0:
        # cada que cambia el gap llamamos a la función gap_insertion_sort que se encargará de ordenar los elementos usando el gap indicado
        for i in range(gap):
            gap_insertion_sort(items_list, i, gap)
        print("Después de los incrementos de tamaño", gap, "La lista es", items_list)
        gap = gap // 2


def gap_insertion_sort(items_list, start, gap):
    # start + gap nos permite movernos a la derecha para hacer la comparación
    for i in range(start+gap, len(items_list), gap):
        current = items_list[i]  # almacenamos el valor temporalmente para guardarlos después en la posición que le corresponde
        position = i  # creamos la variable position y si es necesarios en el siguiente while le restamos el gap para hacer las comparaciones

        # position tiene que ser mayor o igual a gap para poder compararlo con position-gap, si position fuera menor position - gap sería menor a 0 y tendríamos un error
        # si el item en position-gap es mayor al item en la posición i hacemos un swap

        # este while se encarga de comparar un elemento con todos los que tiene a la izquierda (practicamente aquí se realiza el insertion sort, pero sin el swap con el elemento de al lado
        # en lugar de eso se van moviendo los elementos y al final se posiciona current en el lugar que le corresponde)
        while position >= gap and items_list[position-gap] > current:
            items_list[position] = items_list[position-gap] # hacemos el swap
            position = position-gap  # reducimos position para seguir haciendo comparaciones a la izquierda

        # cuando position llega a 0 ya no se pueden hacer comparaciones o cuando current ya no tiene más pequeños a la izquierda
        items_list[position] = current  # almacenamos el valor de la variable que guardamos temporalmente (esto también es parte del swap)


items = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# gaps generados son: 9/2 = 4, 4/2 = 2, 2/2 = 1
shell_sort(items)
print(items)