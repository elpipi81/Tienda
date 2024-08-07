from datetime import datetime

print("************************************")
print("****       BIENVENIDOS A       *****")
print("**     LA TIENDA DE MASCOTAS      **")
print("************************************")

inventario = {
    "perro": 10,
    "gato": 8,
    "pajaros": 25,
    "iguana": 2
}

animales_totales = 0
for val in inventario.values():
    animales_totales += val

nombre = input("Por favor ingrese su nombre\n")
apellido = input("Por favor ingrese su apellido\n")


#Concatemnacion

nombre_completo = nombre  + " " + apellido

print ("Gracias por visitarnos,", nombre_completo)

compras = []

def mostrar_menu():
    print ("")
    print ("=========" * 10)
    print ("Seleccione la opcion que deseas: ")
    print ("1. Conocer cuantos animales tiene la tienda")
    print ("2. Comprar un animal")
    print ("3. Mostrar compras")
    print ("4. Salir del programa")
    
    
def mostrar_inventario():
    print ("")
    print ("**** INVENTARIO ****")
    for llave, valor in inventario.items():
        print (f"    {llave}: {valor}")
    print ("En total tenemos", animales_totales, "animales")
    
def comprar_animal():
    carrito = []
    
    while True:
        print ("¿Que animal deseas comprar? Solo puedes elejir 1 de cada especie")
        print ("Escribe 'F' para terminar la lista o V para ver tu carrito")
        animal = input()
        if animal == "F": break
        
        if animal == "V":
            print (f"Tu carrito de compras contiene {carrito}")
            continue
        
        if animal not in inventario:
            print (f"Lo sentimos, no contamos con el animal {animal}")
        elif inventario[animal] == 0:
            print (f"Lo sentimos, no tenemos en existencia el animal {animal}")
        elif animal not in carrito:
            carrito.append(animal)
        else:
            print ("Ese animal ya se encuentra en tu carrito")    
        
        #print ("Has comprado un", animal)
    
    print ("El contenido de tu carrito es")
    for animal in carrito:
        print ("   ", animal)
        inventario[animal] -= 1
    
    #Agregar esta compra al carrito de compras
    fecha = datetime.now()
    compras.append( (nombre, carrito, fecha) )
        
def mostrar_compras():
    print ("")
    print ("**** COMPRAS REALIZADAS ****")
    for compra in compras:   #Compra = es una tupla que tiene nombre, carrito y fecha
        print (f"    {compra[0]}, compro {compra[1]}, en {compra[2]}")
        

while True:
    mostrar_menu()    
    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()
        
    elif respuesta == 2:
        comprar_animal()
    
    elif respuesta == 3:
        mostrar_compras()    
        
    elif respuesta == 4:
        print ("Saliendo del programa")
        break
    
