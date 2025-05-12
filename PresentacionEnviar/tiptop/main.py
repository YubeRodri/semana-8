from controllers.fila_clientes import Clientes

def mostrar_menu():
    print("\n-- Pollo Tip-Top Metrocentro --")
    print("1. Hacer un pedido")
    print("2. Atender el siguiente pedido")
    print("3. Mostrar pedidos en espera")
    print("4. Salir")
    print("-------------------")

def main():
    clientes = Clientes()
    while True:
        mostrar_menu()
        opcion = input("Digite su accion a realizar: ")
        
        if opcion == "1":
            nombre_cliente = input("Porfavor ingrese su nombre: ")
            print("Combos disponibles: 1. Clasico, 2. Familiar, 3. Sandwich")
            tipo_combo = input("Seleccione el combo a llevar: ")
            tipo_combo = {"1": "Clasico", "2": "Familiar", "3": "Sandwich"}.get(tipo_combo, "Clasico")
            clientes.llega_cliente(nombre_cliente, tipo_combo)
            print(f"Pedido registrado para {nombre_cliente} con combo {tipo_combo}.")
        
        elif opcion == "2":
            clientes.atender_cliente()
        
        elif opcion == "3":
            pedidos = clientes.obtener_clientes_en_espera()
            if pedidos:
                print("\nPedidos pendientes: ")
                for pedido in pedidos:
                    print(pedido)
            else:
                print("Ya se han atendido a todos los clientes!")
        
        elif opcion == "4":
            print("Muchas gracias por comprar en Pollo Tip-Top Metrocentro!")
            break
        
        else:
            print("Porfavor ingrese una opcion valida.")

if __name__ == "__main__":
    main()