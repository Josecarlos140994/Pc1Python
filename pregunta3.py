##Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
##por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
##peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
##cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
##último pedido y calcule el peso total del paquete que será enviado.

##la jugueteria vende dos productos : payasos y muñecas

p = float(input("payasos vendidos:"))
m = float (input("muñecas vendidas:"))

total_de_juguetes_vendidos = p + m

pt_payasos = p * 112
pt_muñecas = m * 75

peso_total = pt_payasos + pt_muñecas

print(f"El numero de payosos y muñecas vendidas son: {total_de_juguetes_vendidos}")
print(f"El peso total del paquete enviado es: {peso_total}")
