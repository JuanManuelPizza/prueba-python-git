nombre = input("Por favor ingrese el nombre del producto: ")
precio = round(float(input("Por favor ingrese el precio del producto: ")), 2)
cantidad = int(input("Por favor ingrese el número de unidades disponibles del producto: "))

total = round((precio*cantidad), 2)

print("El producto " + nombre + " con precio unitario de " + str(precio)+ " cuenta con una cantidad de " + str(cantidad) + " unidades " + " arrojando un costo total de " + str(total))