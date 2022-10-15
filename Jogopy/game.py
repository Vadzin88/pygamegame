import pygame
from pygame.locals import *
pygame.init()
pygame.display.list_modes()




#Variaveis
y = 50
x = 50
velocidade = 7
janela_aberta = True

#Abrir Janela
janela = pygame.display.set_mode((495, 235))
pygame.display.set_caption("Meu Jogo")



#Fechar Janela e Movimentacao
while janela_aberta:
  for ev in pygame.event.get():
    if ev.type == pygame.QUIT:
      janela_aberta = False
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and y > 1:
      y-= velocidade
    if teclas[pygame.K_DOWN] and y < 183:
      y+= velocidade
    if teclas[pygame.K_LEFT] and x > 0:
      x-= velocidade
    if teclas[pygame.K_RIGHT] and x < 456:
      x+= velocidade

  
  #Método Draw
  pygame.draw.rect(janela, (0,255,0),(x,y,50,50))
  pygame.draw.circle(janela, (0,50,0), (50,50), 20)
  pygame.display.update()

pygame.quit()