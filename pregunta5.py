##Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
##último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
##verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.

show = int(input("cuantos shows musicales has vistos en el ultimo año?:"))

if show > 3 : 
    has_visto_mas_de_3_shows = True
else:
    has_visto_mas_de_3_shows = False

print(f"{has_visto_mas_de_3_shows}")