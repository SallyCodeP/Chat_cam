import pygame as gg

# Para ativar a biblioteca do pygame é necessario usar o metodo "init()"
gg.init()

# Para iniciar uma tela é necessario usar o metodo set_mode()
# Como parametro desse metodo colocamos o tamanho da tela em x e y
# Se uma var receber esse metodo poderemos nos referir a essa tela criada depois
window = gg.display.set_mode((800, 400))

# Da um nome a pagina do jogo
gg.display.set_caption("Potato")

# Precisamos definir a quantidade de fps que nosso jogo ira rodar (a animacao e captura de input do player)
# Para isso precisamos de um objeto "Clock" ou seja um objeto que possa settar a velocidade do nosso jogo
clock = gg.time.Clock()

# Para que a tela não pare de funcionar 
# e para podermos atualizar os elementos dentro da tela (displays)
# Iniciamos um loop

while True:
    
    # Para capturarmos os inputs do jogador (eventos), como, movimento do mouse ou teclado
    # Usamos uma funcao em loop for que retorna cada tecla apertada 
    for event in gg.event.get():
        # para analizarmos o tipo de evento que foi ativado usamos (variavel_for).type 
        # Para que possamos fechar a janela do jogo usamos:
        if event.type == gg.QUIT:
            gg.quit()
            exit()


    # O metodo display.update atualiza a tela com os novos elementos
    gg.display.update()

    # Para definir o FPS maximo do nosso jogo usamos o objeto clock e usamos o metodo tick()
    # Como parametro passamos o FPS que queremos para o nosso jogo
    clock.tick(70)
    
    
