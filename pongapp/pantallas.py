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

        self.fuente = pg.font.Font(FUENTE1,20)  
        self.fuenteTwo = pg.font.Font(FUENTE2,15)
        
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0
        self.quienMarco=""
        self.temporizador = TIEMPO_JUEGO
        self.game_over = True
        self.contadorFotograma=0
        self.colorFondo=COLOR_CANCHA

    def bucle_fotograma(self):
        
        
        while self.game_over:
            self.valor_tasa = self.tasa_refresco.tick(300)
            self.temporizador = self.temporizador -  self.valor_tasa

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    self.game_over = False
            
            
            color = self.fijar_fondo() 
            self.pantalla_principal.fill(color)

            self.mostrar_linea_central()
            
            self.raqueta1.dibujar(self.pantalla_principal) 
            self.raqueta2.dibujar(self.pantalla_principal)
            self.pelota.dibujar(self.pantalla_principal)
            self.mostrar_jugadores()
            
            self.raqueta1.mover(pg.K_w,pg.K_s)
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)
            self.quienMarco = self.pelota.mover()

            self.pelota.comprobar_choqueV2(self.raqueta1,self.raqueta2)
            self.mostrar_marcador()
            self.mostrar_temporizador()
            self.finalizacion_de_juego()

            pg.display.flip()

        pg.quit()

    def mostrar_linea_central(self):
            """
            cont_linea = 0
            while cont_linea <= 600:
                pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (400,cont_linea), (400,cont_linea+50), width=10)
                cont_linea += 70
            """
            
            for cont_linea in range(0,601,70):    
                pg.draw.line(self.pantalla_principal,COLOR_BLANCO,(ANCHO//2,cont_linea),(ANCHO//2,cont_linea+50),width=10) 


    def mostrar_jugadores(self):
        jugador1 = self.fuenteTwo.render("Jugador 1",True,COLOR_AZUL)
        jugador2 = self.fuenteTwo.render("Jugador 2",True,COLOR_AZUL)
        self.pantalla_principal.blit(jugador1,(210,20))
        self.pantalla_principal.blit(jugador2,(510,20))

    def mostrar_marcador(self):
        if self.quienMarco == "right":
            self.contadorDerecho +=1
        elif self.quienMarco ==  "left":
            self.contadorIzquierdo +=1  
        marcador1 = self.fuente.render(str(self.contadorDerecho),True,COLOR_NARANJA)
        marcador2 = self.fuente.render(str(self.contadorIzquierdo),True,COLOR_NARANJA)
        self.pantalla_principal.blit(marcador1,(250,50))
        self.pantalla_principal.blit(marcador2,(550,50))

    def finalizacion_de_juego(self):
            #finalizacion del juego por tiempo
            if self.temporizador <= 0:
                print("fin del juego")
                self.game_over = False          

            #finalizacion de juego por puntos
            if self.contadorDerecho == 7:
                self.game_over = False
                print("El ganador es el Jugador 1")

            if self.contadorIzquierdo ==7:
                self.game_over = False
                print("El ganador es el Jugador 2")

    def mostrar_temporizador(self):
        tiempo_juego = self.fuente.render(str( int( self.temporizador/1000) ),True,COLOR_ROJO)
        self.pantalla_principal.blit(tiempo_juego,(400,20))

    def fijar_fondo(self):
        self.contadorFotograma +=1
        if self.temporizador > 10000:
            self.contadorFotograma=0
        elif self.temporizador > 5000:
            if self.contadorFotograma == 20:
                if self.colorFondo == COLOR_CANCHA:
                    self.colorFondo = COLOR_NARANJA
                else:
                    self.colorFondo = COLOR_CANCHA       
                self.contadorFotograma=0
        else:
            if self.contadorFotograma == 20:
                if self.colorFondo == COLOR_CANCHA or self.colorFondo == COLOR_NARANJA:
                    self.colorFondo = COLOR_ROJO
                else:
                    self.colorFondo = COLOR_CANCHA  
                self.contadorFotograma=0  
        
        return self.colorFondo
    
        """
        if self.temporizador < 10000 and self.temporizador > 5000:
            self.pantalla_principal.fill( FONDO_NARANJA )
        elif self.temporizador < 5000:
            self.pantalla_principal.fill(FONDO_ROJO) 
        else:
            self.pantalla_principal.fill( COLOR_CANCHA )            
        """

class Menu:
     pg.init()
     def __init__(self):
        self.pantalla_principal= pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Menu")
        self.tasa_refresco= pg.time.Clock()
        self.imagenFondo = pg.image.load("pongapp/images/fondo.png")
        self.fuente = pg.font.Font(FUENTE2,20)  

     def bucle_pantalla(self):
        game_over=True
        while game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False
                """
                if evento.type == pg.KEYDOWN:    
                    if evento.key == pg.K_RETURN:
                        print("precionaste enter")
                """
            enter = pg.key.get_pressed()
            if enter[pg.K_RETURN]:
                #game_over = False
                return "partida"       

            self.pantalla_principal.blit(self.imagenFondo,(0,0))

            texto_menu = self.fuente.render("Pulsa ENTER para jugar",True,COLOR_AMARILLO)
            self.pantalla_principal.blit(texto_menu,(200,ALTO//2))

            pg.display.flip()
        pg.quit()              

