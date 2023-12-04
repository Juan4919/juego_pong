from pongapp.pantallas  import Partida,Menu,Resultado



menu = Menu()


valor = menu.bucle_pantalla()

juego = Partida()

if valor == "partida":
    juego.bucle_fotograma()

resultado_partida =  juego.finalizacion_de_juego()

resultado = Resultado(resultado_partida)
resultado.bucle_pantalla()    