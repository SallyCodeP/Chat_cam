import pygame as gg

# Desenhando imagens na nossa window 
# Primeiro precisamos definir uma "display main" que vai se referir a tela em si
# la e onde vamos inserir outros os outros elementos do jogo, os "displays regulars"
# Os displays regulars sao completamente moldaveis e sao os proprios elementos do nosso jogo

gg.init()

# Criando Display Main
main = gg.display.set_mode((800, 400))

gg.display.set_caption("Images")
clock = gg.time.Clock()

# Criando um display regular
# Como parametro definimos o tamanho do nosso elemento
regular_1 = gg.Surface((200, 200))
#
#  Definindo cor do elemento display regular
regular_1.fill("blue")

while True:
    for event in gg.event.get():
        if event.type == gg.QUIT:
            gg.quit()
            exit()

    # Para inserir um display regular no main display chamamos o metodo blit no obj main
    # Como primeiro parametro colocamos o regular display
    # Como segundo parametro colocamos as coordenadas onde o regular display ira ser chamado
    main.blit(regular_1, (0,0))

    gg.display.update()
    clock.tick(70)
    
    
