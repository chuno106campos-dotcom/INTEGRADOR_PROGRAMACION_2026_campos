categorias = ["enlatados", "frutas", "congelados", "panaderia"]
def mostrar_menu():
    print("1. Cargar stock")
    print("2. Mostrar total del stock")
    print("3. Mostrar cantidad de productos")
    print("4. Salir")
    opcion = int(input("Elija una opción\n"))
    return opcion

def pedir_categoria():
    print(categorias)
    categoria = input("Ingrese la categoría\n")
    return categoria


def pedir_datos_carga():
    categoria = pedir_categoria()
    producto = input("Nombre del producto\n")
    cantidad = int(input("Cantidad\n"))
    return categoria, cantidad

