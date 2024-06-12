
# 2023-05-18 ngio add
# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
#현재 폴더 경로; 작업 폴더 기준
print(os.getcwd())
#현재 파일의 폴더 경로; 작업 파일 기준
real_path = os.path.dirname(os.path.realpath(__file__))
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path)

import pygame
import random


pygame.init()
screen = pygame.display.set_mode((700,650))
clock = pygame.time.Clock()

basket_image = pygame.transform.scale(pygame.image.load("basket.png"),(100,80))
fruit_image1 = pygame.transform.scale(pygame.image.load("apple.png"),(50,50))
rect_image = pygame.transform.scale(pygame.image.load("rect.png",),(100,20))
fruit_image2 = pygame.transform.scale(pygame.image.load("banana.png"),(50,50))
fruit_image3 = pygame.transform.scale(pygame.image.load("Dragon fruit.png"),(50,50))

largefont = pygame.font.Font(None,80)
smfont = pygame.font.Font(None,30)

class Fruit():
    def __init__(self,fruit_image , y):
        self.image = fruit_image
        self.rect = self.image.get_rect(center = (random.randint(0, 650),y))
        self.speed = 1

    def move(self):
        self.rect.bottom += self.speed 
        
    def collision(self , basket):
        if self.rect.colliderect(basket.rect):
            self.rect.center = (random.randint(0, 700),0)
            self.speed += 1
            self.move()
            basket.speed += 1
            basket.score += 1
            score = largefont.render(f"Score: {basket.score}",False , "black")
            return True
        else:
            return False
           
class Basket():
    def __init__(self,basket_image):
        self.image = basket_image
        self.rect = self.image.get_rect(center = (350,610))
        self.scoreFont = largefont.render("0" , False , "black")
        self.score_rect = self.scoreFont.get_rect(right = 700)
        self.livesFont = largefont.render("5",False,"black")
        self.score = 0
        self.speed = 2
        self.lives = 5

    def control(self):    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if self.rect.right <= 700:
                self.rect.left += self.speed 
                #print(self.rect.left)

        if keys[pygame.K_LEFT]:
            if self.rect.left >= 0:
                self.rect.left -= self.speed
                #print(self.rect.left)
     
class SFruit(Fruit):
    def __init__(self,fruit_image,y):
        super().__init__(fruit_image,y)

    def collision(self, basket):

        if super().collision(basket) :
            print("new life")
            basket.lives += 1
            self.rect.center = (random.randint(0, 700),-500)
 


fruit1 = Fruit(fruit_image1 , random.randint(-400 , 0))
fruit2 = Fruit(fruit_image2 , random.randint(-400 , 0))#
fruit3 = SFruit(fruit_image3, random.randint(-400,-0))



fruits = [fruit1 , fruit2, fruit3]

basket = Basket(basket_image)

def checkLoss():
    for fruit in fruits:
        if fruit.rect.bottom > screen.get_height():
            print("collision")
            basket.lives -= 1 
            fruit.speed +=1
            fruit.rect.center = (random.randint(0, 700),random.randint(-400,0))
            
    basket.livesFont = largefont.render(f"Lives: {basket.lives}",False,"black")

def restart():
    if basket.lives <= 0:
        screen.fill("Black")
        screen.blit(smfont.render("You lose CLICK SPACE TO RESTART",False,"red"),(170,200))
        if basket.score >= 22:
            screen.blit(smfont.render(f"well done your score was: {basket.score}",False,"green"),(230,400))
        else:
            screen.blit(smfont.render(f"good try your score was: {basket.score}",False,"Red"),(200,400))
        for fruit in fruits:
            fruit.rect.center = (random.randint(0, 700),0)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            basket.score = 0
            basket.lives = 5
            draw()
            for fruit in fruits:
                fruit.speed = 1
            basket.speed = 2


def draw():
    screen.fill("light blue")
    screen.blit(fruit_image1,fruit1.rect)
    screen.blit(fruit_image2,fruit2.rect)
    screen.blit(fruit_image3,fruit3.rect)
    screen.blit(basket.image,basket.rect)
    screen.blit(basket.scoreFont , basket.score_rect)
    basket.score_rect.right = 700
    screen.blit(basket.livesFont , (10 , 10))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    basket.score_rect = basket.scoreFont.get_rect(right = 700)

    basket.control()
    for fruit in fruits:
        fruit.move()
        fruit.collision(basket)
    
    basket.scoreFont = largefont.render(f"Score: {basket.score}" , False , "black")
    checkLoss()
    draw()
    restart()
    pygame.display.flip()
    clock.tick(30)