from pizza import Pizza
import ingredientes

print(f"Precio: ${Pizza.precio}")
print(f"Tamaño: {Pizza.tamanio}")

print("Salsa de tomate está en la lista"
      if Pizza.validar_eleccion("salsa de tomate",["salsa de tomate", "salsa bbq"]) 
      else "Salsa de tomate no está en la lista"
    )

p = Pizza()
p.realizar_pedido()


print("Los vegetales escogidos son:")
for ingrediente in p.vegetales:
    if ingrediente in ingredientes.vegetales:
        #se obtiene nombre del ingrediente del diccionario vegetales
        print(">>",ingredientes.vegetales[ingrediente])
    else:
        print(">> Ingrediente no válido")
        
if p.proteina in ingredientes.proteinas:
    #se obtiene nombre del ingrediente del diccionario proteinas
    print("La proteina escogida es:",ingredientes.proteinas[p.proteina])
else:
    print("La proteina escogida es no válida")
    
if p.tipo_masa in ingredientes.tipo_masa:
    #se obtiene nombre del ingrediente del diccionario tipo_masa
    print("El tipo de masa escogido es:",ingredientes.tipo_masa[p.tipo_masa])
else:
    print("El tipo de masa escogido no es válido")

print("La pizza es válida"
      if p.valida
      else "La pizza no es válida"
    )

print(Pizza.valida)