import pygame as gg

# Para ativar a biblioteca do pygame é necessario usar o metodo "init()"
gg.init()

# Para iniciar uma tela é necessario usar o metodo set_mode()
# Como parametro desse metodo colocamos o tamanho da tela em x e y
# Se uma var receber esse metodo poderemos nos referir a essa tela criada depois
window = gg.display.set_mode((800, 400))

# Para que a tela não pare de funcionar 
# e para podermos atualizar os elementos dentro da tela (displays)
# Iniciamos um loop

while True:
    # O metodo display.update atualiza a tela com os novos elementos
    gg.display.update()
