from models.cola import Cola
from models.pedido import Pedido

class Clientes:
    def __init__(self):
        self.cola_clientes = Cola()
        self.ultimo_pedido = None
        self.numero_orden = 1
    def llega_cliente(self, nombre, tipo_combo):
        pedido = Pedido(self.numero_orden, nombre, tipo_combo)
        self.cola_clientes.encolar(pedido)
        self.numero_orden += 1

    def atender_cliente(self):
        self.ultimo_pedido = self.cola_clientes.desencolar()
        if self.ultimo_pedido:
            print(f"Atendiendo a: {self.ultimo_pedido}")
        else:
            print("No se han registrado pedidos.")

    def obtener_clientes_en_espera(self):
        return self.cola_clientes.mostrar()

    def obtener_ultimo_atendido(self):
        return self.ultimo_pedido