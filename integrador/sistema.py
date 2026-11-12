import menu
import gestion_stock
def main():
    gestion_stock.inicializar()
    while True:
        opcion = menu.mostrar_menu()
        if opcion == 1:
            categoria, producto, cantidad = menu.pedir_datos_carga()
            gestion_stock.cargar_stock(categoria, producto, cantidad)
        elif opcion == 2:
            gestion_stock.mostrar_stock()
        elif opcion == 3:
            categoria = menu.pedir_categoria()
            if categoria in gestion_stock.stock_cantidades:
                gestion_stock.contar(gestion_stock.stock_cantidades[categoria])
            else:
                print("La categoría no existe.")
        elif opcion == 4:
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
