stock_productos = {'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': []}
stock_cantidades = {'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': []}

def inicializar():
    for categoria in stock_productos:
        stock_productos[categoria] = []
    for categoria in stock_cantidades:
        stock_cantidades[categoria] = []


def cargar_stock(categoria, producto, cantidad):
    categoria=input("Elige la categoría\n")
    if categoria in stock_productos:
        productos=input("Escriba los productos para agregar\n")
        cantidad=input("Escriba la cantidad que quiere agregar\n")
    stock_productos[categoria].append(producto)
    stock_cantidades[categoria].append(cantidad)

def mostrar_stock():
    for cat, pro in stock_productos.items():
        print(f"{cat}:{pro}")
    for cat, pro in stock_cantidades.items():
        print(f"{cat}:{pro}")

def contar(lista_productos):
    cantidad_productos = len(lista_productos)
    suma_cantidades = sum(lista_productos)
    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Suma de las cantidades: {suma_cantidades}")
