from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()
    
    def encolar(self, elemento):
        self.items.append(elemento)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()
        return None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def mostrar(self):
        return list(self.items)
