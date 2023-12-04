from pongapp.pantallas  import Partida,Menu



menu = Menu()


valor = menu.bucle_pantalla()

juego = Partida()

if valor == "partida":
    juego.bucle_fotograma()