from .pantallas import *

class PantallaControlador:
    def __init__(self):
        self.menu = Menu()
        self.partida = Partida()
        self.resultado = Resultado()
        self.record = Record()
        self.resultado_final=""

    def start(self):
        while True:
            self.menu.bucle_pantalla()
            self.resultado_final = self.partida.bucle_fotograma()
            self.resultado.cargar_resultado(self.resultado_final)
            self.resultado.bucle_pantalla()

        """
        while True:
            valor = self.menu.bucle_pantalla()

            if valor == "partida":
                self.partida.bucle_fotograma()
                resultado_partida =  self.partida.finalizacion_de_juego()
                if resultado_partida != "":
                    resultado = Resultado(resultado_partida)
                    resultado.bucle_pantalla()  
            elif valor =="record":
                self.record.bucle_pantalla()
        """