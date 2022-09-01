const shell_sort = (list) => {
  let gap = parseInt(list.length / 2);
  while (gap > 0) {
    for (let i = 0; i < list.length; i++) {
      gap_insertion_sort(list, i, gap);
    }
    console.log(
      "Después de los incrementos de tamaño ",
      gap,
      " La lista es ",
      list
    );
    gap = parseInt(gap / 2);
  }
};

function gap_insertion_sort(list, start, gap) {
  // start + gap nos permite movernos a la derecha para hacer la comparación
  let current;
  let position;
  for (let i = start + gap; i < list.length; i += gap) {
    current = list[i]; //almacenamos el valor temporalmente
    position = i; // creamos la variable position y si es necesarios en el siguiente while le restamos el gap para hacer las comparaciones
    while (position >= gap && list[position - gap] > current) {
      list[position] = list[position - gap]; //hacemos el swap
      position = position - gap; //reducimos position para seguir haciendo comparaciones a la izquierda
    }
    // cuando position llega a 0 ya no se pueden hacer comparaciones o cuando current ya no tiene más pequeños a la izquierda
    list[position] = current; // almacenamos el valor de la variable que guardamos temporalmente (esto también es parte del swap)
  }
}

items = [54, 26, 93, 17, 77, 31, 44, 55, 20];
// gaps generados son: 9/2 = 4, 4/2 = 2, 2/2 = 1
shell_sort(items);
console.log(items);
