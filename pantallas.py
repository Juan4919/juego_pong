import pygame as pg
from pongapp.figura_class import Pelota,Raqueta
from pongapp.utils import*


class Partida:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Pong")
        self.tasa_refresco= pg.time.Clock()

        self.pelota = Pelota(ANCHO//2,ALTO//2,COLOR_PELOTA)
        self.raqueta1 = Raqueta(10 ,ALTO//2 )#raqueta izquierda
        self.raqueta2 = Raqueta(ANCHO-10,ALTO//2 )#raqueta derecha

    def bucle_fotograma(self):
        game_over = True
        while game_over:
            self.valor_tasa = self.tasa_refresco.tick(350)
   
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False

            self.pantalla_principal.fill( COLOR_CANCHA )
            pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (ANCHO//2,0), (ANCHO//2,ALTO), width=10)
           
            self.raqueta1.dibujar(self.pantalla_principal) 
            self.raqueta2.dibujar(self.pantalla_principal)
            self.pelota.dibujar(self.pantalla_principal)
            
            self.raqueta1.mover(pg.K_w,pg.K_s)
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)
            self.pelota.mover()

            #logica de choque
            #raqueta derecha
            self.pelota.comprobar_choqueV2(self.raqueta1,self.raqueta2)
            self.pelota.mostrar_marcador(self.pantalla_principal)

            pg.display.flip()

        pg.quit()        