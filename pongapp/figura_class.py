import pygame as pg
from .utils import *

class Raqueta:
    def __init__(self,pos_x, pos_y,color=COLOR_BLANCO,w=20,h=120):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h

    def dibujar(self,surface):
       pg.draw.rect(surface,self.color,(self.pos_x-(self.w//2), self.pos_y-(self.h//2) ,self.w,self.h) )

    def mover(self,teclado_arriba,teclado_abajo,y_max=ALTO,y_min=ALTO_MIN):
        estado_teclado = pg.key.get_pressed()

        if estado_teclado[teclado_arriba] == True and self.pos_y > y_min+(self.h//2):
            self.pos_y -= 1

        if estado_teclado[teclado_abajo] == True and self.pos_y < y_max-(self.h//2):
            self.pos_y += 1

    @property
    def derecha(self):
        return self.pos_x + (self.w//2)
    
    @property
    def izquierda(self):
        return self.pos_x - (self.w//2)  
    
    @property
    def arriba(self):
        return self.pos_y - (self.h//2)
    
    @property
    def abajo(self):
        return self.pos_y + (self.h//2)      




class Pelota:
    def __init__(self,pos_x, pos_y,color=COLOR_BLANCO,radio=15,vx=1,vy=1):
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
        if self.pos_x >= x_max + (1*self.radio):
            self.pos_x = 400
            self.pos_y = 300
            self.vx *=-1
            self.vy *=-1
            self.contadorDerecho +=1
        #limite izquierdo
        if  self.pos_x <= 0-(1*self.radio):
            self.pos_x = 400
            self.pos_y = 300
            self.vx *=-1
            self.vy *=-1
            self.contadorIzquierdo +=1

        if self.pos_y >= y_max or self.pos_y <=0:
            self.vy *=-1

    def mostrar_marcador(self,pantalla):
        fuente = pg.font.Font(None,40)
        marcador1 = fuente.render(str(self.contadorDerecho),True,COLOR_NARANJA)
        marcador2 = fuente.render(str(self.contadorIzquierdo),True,COLOR_NARANJA)
        pantalla.blit(marcador1,(250,50))
        pantalla.blit(marcador2,(550,50))

    @property
    def derecha(self):
        return self.pos_x + self.radio
    
    @property
    def izquierda(self):
        return self.pos_x - self.radio 
    
    @property
    def arriba(self):
        return self.pos_y - self.radio
    
    @property
    def abajo(self):
        return self.pos_y + self.radio   

    def comprobar_choque(self,r1,r2):
        if self.derecha >= r2.izquierda and\
            self.izquierda <= r2.derecha and\
            self.abajo >= r2.arriba and\
            self.arriba <= r2.abajo:            
                self.vx *= -1

        if  self.derecha >= r1.izquierda and\
            self.izquierda <= r1.derecha and\
            self.abajo >= r1.arriba and\
            self.arriba <= r1.abajo:            
                self.vx *= -1  

    def comprobar_choqueV2(self,*raquetas): 
        for r in raquetas:
            if self.derecha >= r.izquierda and\
                self.izquierda <= r.derecha and\
                self.abajo >= r.arriba and\
                self.arriba <= r.abajo:
                    self.vx *= -1           