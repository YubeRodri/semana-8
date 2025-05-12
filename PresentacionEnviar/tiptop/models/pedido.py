from datetime import datetime

class Pedido:
    def __init__(self, numero_orden, nombre_cliente, tipo_combo):
        self.numero_orden = numero_orden
        self.nombre_cliente = nombre_cliente
        self.tipo_combo = tipo_combo
        self.hora_pedido = datetime.now().strftime("%H:%M:%S")

    def __str__(self):
        return f"Orden #{self.numero_orden} - Cliente: {self.nombre_cliente}, Combo: {self.tipo_combo}, Hora: {self.hora_pedido}"