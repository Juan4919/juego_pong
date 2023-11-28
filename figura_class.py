import pygame as pg

class Raqueta:
    def __init__(self,pos_x, pos_y,color=(255,255,255),w=20,h=120,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h
        self.vx = vx
        self.vy = vy

    def dibujar(self,surface):
        pg.draw.rect(surface,self.color,(self.pos_x-(self.w//2), self.pos_y-(self.h//2) ,self.w,self.h) )

    def mover(self,teclado_arriba,teclado_abajo):
        estado_teclado = pg.key.get_pressed()

        if estado_teclado[teclado_arriba] == True and self.pos_y >= 0+(self.h//2):
            self.pos_y -= 1

        if estado_teclado[teclado_abajo] == True and self.pos_y <= 600-(self.h//2):
            self.pos_y += 1    


class Pelota:
    def __init__(self,pos_x, pos_y,color=(255,255,255),radio=5):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio

    def dibujar(self,surface):
        pg.draw.circle(surface,self.color,(self.pos_x,self.pos_y),self.radio )    
        