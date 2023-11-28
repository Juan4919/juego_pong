import pygame as pg
from figura_class import Pelota

pg.init()

pantalla_principal = pg.display.set_mode( (800,600) )
pg.display.set_caption("Pong")

#creamos un objeto de la clase Pelota o instanciamos la clase pelota
pelota = Pelota(400,300,(228, 231, 19),15)

game_over = True

while game_over:

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = False

    pantalla_principal.fill( ( 27, 149, 47 ) )

    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=10)

    pelota.dibujar(pantalla_principal)

    pg.display.flip()

pg.quit()

