from pongapp.figura_class import Pelota,Raqueta
from pongapp.utils import*


class Partida:
    def __init__(self):
      
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Pong")
        self.tasa_refresco= pg.time.Clock()

        self.pelota = Pelota(ANCHO//2,ALTO//2,COLOR_PELOTA)
        self.raqueta1 = Raqueta(10 ,ALTO//2 )#raqueta izquierda
        self.raqueta1.direccion="izqda"
        self.raqueta2 = Raqueta(ANCHO-20,ALTO//2 )#raqueta derecha
        self.raqueta2.direccion="drcha"
        self.fuente = pg.font.Font(FUENTE1,SIZE_FUENTE_2)  
        self.fuenteTwo = pg.font.Font(FUENTE2,SIZE_FUENTE_2)
        
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0
        self.quienMarco=""
        self.temporizador = TIEMPO_JUEGO
        self.game_over = True
        self.contadorFotograma=0
        self.colorFondo=COLOR_CANCHA

        self.resultado_partida=""

    def bucle_fotograma(self):
        #iniciar en punto de partida con parametros de finalizacion de juego
        self.temporizador = TIEMPO_JUEGO
        self.tasa_refresco.tick()
        self.contadorDerecho =0
        self.contadorIzquierdo = 0
        
        while self.game_over and (self.contadorDerecho < 7 or self.contadorIzquierdo < 7) and self.temporizador > 0:
            self.valor_tasa = self.tasa_refresco.tick(VELOCIDAD_JUEGO)
            self.temporizador = self.temporizador -  self.valor_tasa
            self.finalizacion_de_juego()
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                   return True
            
            
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
           

            pg.display.flip()

        return self.resultado_partida
       

    def mostrar_linea_central(self):            
            for cont_linea in range(0,ALTO+1,70):    
                pg.draw.line(self.pantalla_principal,COLOR_BLANCO,(ANCHO//2,cont_linea),(ANCHO//2,cont_linea+50),width=10) 


    def mostrar_jugadores(self):
        jugador1 = self.fuenteTwo.render("Jugador 1",True,COLOR_AZUL)
        jugador2 = self.fuenteTwo.render("Jugador 2",True,COLOR_AZUL)
        self.pantalla_principal.blit(jugador1,(210,SIZE_FUENTE_2))
        self.pantalla_principal.blit(jugador2,(510,SIZE_FUENTE_2))

    def mostrar_marcador(self):
        if self.quienMarco == "right":
            self.contadorDerecho +=1
        elif self.quienMarco ==  "left":
            self.contadorIzquierdo +=1  
        marcador1 = self.fuente.render(str(self.contadorDerecho),True,COLOR_NARANJA)
        marcador2 = self.fuente.render(str(self.contadorIzquierdo),True,COLOR_NARANJA)
        self.pantalla_principal.blit(marcador1,(250,SIZE_FUENTE_2+30))
        self.pantalla_principal.blit(marcador2,(550,SIZE_FUENTE_2+30))

    def finalizacion_de_juego(self):
        if self.contadorDerecho > self.contadorIzquierdo:
            self.resultado_partida= f"Gana Jugador 1:  resultado = Jugador1:{self.contadorDerecho} , Jugador2:{self.contadorIzquierdo}"
        elif self.contadorIzquierdo > self.contadorDerecho:
            self.resultado_partida= f"Gana el Jugador 2: resultado = Jugador1:{self.contadorDerecho} , Jugador2:{self.contadorIzquierdo}"
        else:
            self.resultado_partida= f"Empate entre Jugador 1 y Jugador 2 resultado = Jugador1:{self.contadorDerecho} , Jugador2:{self.contadorIzquierdo}"  

    def mostrar_temporizador(self):
        tiempo_juego = self.fuente.render(str( int( self.temporizador/1000) ),True,COLOR_ROJO)
        self.pantalla_principal.blit(tiempo_juego,(ANCHO//2,SIZE_FUENTE_2))

    def fijar_fondo(self):
        self.contadorFotograma +=1
        if self.temporizador > TIEMPO_LIMIT_1:
            self.contadorFotograma=0
        elif self.temporizador > TIEMPO_LIMIT_2:
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

class Menu:
     def __init__(self):
        
        self.pantalla_principal= pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Menu")
        self.tasa_refresco= pg.time.Clock()
        self.imagenFondo = pg.image.load(IMG_FONDO)
        self.fuente = pg.font.Font(FUENTE2,18) 
        self.sonido = pg.mixer.Sound(SONIDO_AMBIENTE)#definimos el sonido con el path del archivo 

     def bucle_pantalla(self):
        game_over=True
        while game_over:
            pg.mixer.Sound.set_volume(self.sonido, 0.02)#controlando el volumen del sonido
            pg.mixer.Sound.play(self.sonido)#activamos el sonido
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True

            botones = pg.key.get_pressed()
            if botones[pg.K_RETURN]:
                #game_over = False
                pg.mixer.Sound.stop(self.sonido)#paramos el sonido
                return "partida"
            elif botones[pg.K_r]:
                pg.mixer.Sound.stop(self.sonido)
                return "record"       

            self.pantalla_principal.blit(self.imagenFondo,(0,0))

            texto_menu_partida = self.fuente.render("Pulsa ENTER para jugar",True,COLOR_AMARILLO)
            texto_menu_record  = self.fuente.render("Pulsa R para ver los mejores puntajes",True,COLOR_NARANJA)
            self.pantalla_principal.blit(texto_menu_partida,(200,ALTO//2))
            self.pantalla_principal.blit(texto_menu_record,(100,ALTO//2+40 ))

            pg.display.flip()
                     

class Resultado:
    def __init__(self):
        
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Resultado")
        self.tasa_refresco= pg.time.Clock()
        self.fuenteResultado = pg.font.Font(FUENTE1,18)
        self.resultado = ""

    def bucle_pantalla(self):
        game_over=True
        while game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False
            
            self.pantalla_principal.fill(COLOR_BLANCO)
            texto_resultado = self.fuenteResultado.render( str(self.resultado) ,True,COLOR_GRANATE)
            self.pantalla_principal.blit(texto_resultado,(120,ALTO//2))
            pg.display.flip()

                    

    def cargar_resultado(self,resultado):
        self.resultado = resultado


class Record:
    def __init__(self):
        
        self.pantalla_principal= pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Puntajes")
        self.tasa_refresco= pg.time.Clock()
        self.fuenteRecord=pg.font.Font(FUENTE1,20)

    def bucle_pantalla(self):
        game_over=True
        while game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:    
                    return True
            self.pantalla_principal.fill(COLOR_BLANCO)
            texto= self.fuenteRecord.render("Mejores Puntajes",0,COLOR_GRANATE) 

            enter = pg.key.get_pressed()
            if enter[pg.K_RETURN]:
                game_over = False
                
            self.pantalla_principal.blit(texto,(160,ALTO//2))

            pg.display.flip()

           


                   