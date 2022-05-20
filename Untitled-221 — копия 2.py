import pygame
import random
import os
pygame.init() # Инициализирует работу пай гем
path = os.path.abspath(__file__ + '/..') # находим абсолютный путь к файлу
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('GAME')
class Img:
    def __init__(self,width,height,image,x,y):
        self.width = width
        self.height = height
        self.x, self.y = x,y 
        self.image = os.path.join(path,'image',image)
        self.image = pygame.image.load(self.image)
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)

img1 = Img(150,150,'3.jpeg',0,0)
def start_game():
    fps = pygame.time.Clock()
    game = True
    color = (0,0,0)
    while game:
        screen.fill(color)
        screen.blit(img1.image, (img1.x,img1.y))
        pygame.draw.rect(screen,(255,255,255),img1.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                
                if img1.rect.collidepoint(click):
                    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            img1.x -= 10
        if keys[pygame.K_RIGHT]:
            img1.x += 10
        if keys[pygame.K_DOWN]:
            img1.y += 10
        if keys[pygame.K_UP]:
            img1.y -= 10
        pygame.display.flip()
        fps.tick(40)
start_game()