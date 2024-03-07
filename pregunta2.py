

c_restaurante = float(input("cuanto fue tu consumo en el restaurante:"))

p_propina = float(input("Que porcentaje de propina desea dejar:"))

total_de_propina = c_restaurante * (p_propina/100)

print(f"El dinero de la propina fue: {total_de_propina}")