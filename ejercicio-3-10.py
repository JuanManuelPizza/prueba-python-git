#No se puede hacer uso de bucles, tuplas, listas etc.

eleccion = input("Por favor digite que tipo de pizza quiere, vegetariana o no vegetariana: ").lower().strip()

print(eleccion)

if eleccion == "vegetariana":
    print("Para la pizza vegetariana contamos con pimiento y tofu.")

    veg_eleccion = input("Por favor digite cual de los dos ingredientes desea: ").lower().strip()
    
    if veg_eleccion == "tofu" or veg_eleccion== "pimiento":
        print("Excelente, su pizza vegetariana cuenta con tomate, mozzarella y "+ veg_eleccion + ".")

    else:
        print("No eligio el igrediente correctamente, por favor intente de nuevo.")

elif eleccion == "no vegetariana":
    print("Para la pizza no vegetariana contamos con peperoni, jamon y salmon.")

    nonveg_eleccion = input("Por favor ingrese cual de los tres ingredientes desea: ").lower().strip()

    if nonveg_eleccion == "jamon" or nonveg_eleccion == "salmon" or nonveg_eleccion == "peperoni":
        print("Excelente, su pizza no vegetariana cuenta con tomate, mozzarella y " + nonveg_eleccion + ".")

    else: 
        print("No eligio el ingrediente correctamente, por favor intente de nuevo.")
else:
    print("No selecciono el tipo de pizza correctamente, por favor intente de nuevo.")