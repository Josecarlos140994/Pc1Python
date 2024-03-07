##Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
##encuentran en la posición 0, 4 y 5.
##lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
##Resultado esperado: ['Verde', 'Blanco', 'Negro']


Lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

Lista.remove ('Rojo')
Lista.remove ('Rosa')
Lista.remove ('Amarillo')

Lista

print(f" La lista final es: {Lista}" )