import pygame as pg

class Raqueta:
    def __init__(self,pos_x, pos_y,color=(255,255,255),w=20,h=120):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h

    def dibujar(self,surface):
        pg.draw.rect(surface,self.color,(self.pos_x-(self.w//2), self.pos_y-(self.h//2) ,self.w,self.h) )

    def mover(self,teclado_arriba,teclado_abajo):
        estado_teclado = pg.key.get_pressed()

        if estado_teclado[teclado_arriba] == True and self.pos_y >= 0+(self.h//2):
            self.pos_y -= 1

        if estado_teclado[teclado_abajo] == True and self.pos_y <= 600-(self.h//2):
            self.pos_y += 1

            




class Pelota:
    def __init__(self,pos_x, pos_y,color=(255,255,255),radio=5,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0

    def dibujar(self,surface):
        pg.draw.circle(surface,self.color,(self.pos_x,self.pos_y),self.radio )    

    def mover(self,x_max=800,y_max=600):
        self.pos_x += self.vx
        self.pos_y += self.vy
        #limite derecho
        if self.pos_x >= x_max + (5*self.radio):
            #self.pos_x = 400
            #self.pos_y = 300
            self.vx *=-1
            self.contadorDerecho +=1
        #limite izquierdo
        if  self.pos_x <= 0-(5*self.radio):
            #self.pos_x = 400
            #self.pos_y = 300
            self.vx *=-1
            self.contadorIzquierdo +=1

        if self.pos_y >= y_max or self.pos_y <=0:
            self.vy *=-1

    def mostrar_marcador(self,pantalla):
        fuente = pg.font.Font(None,30)
        marcador1 = fuente.render(str(self.contadorDerecho),True,(255,255,255))
        marcador2 = fuente.render(str(self.contadorIzquierdo),True,(255,255,255))
        pantalla.blit(marcador1,(350,50))
        pantalla.blit(marcador2,(450,50))