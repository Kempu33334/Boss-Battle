import pygame
import random
import math
import sys
import time

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Boss Battle")

pIndexX = 5
pIndexY = 5
places = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
enemyIndexX = 1
enemyIndexY = 1
enemyIndexX2 = 1
enemyIndexY2 = 1
enemyIndexX3 = 1
enemyIndexY3 = 1
enemyIndexX4 = 1
enemyIndexY4 = 1
cycle = 51
score = 0
gameRound = 1;
health = 100
recordHealth = 0
endGame = 0
font = pygame.font.SysFont('couriernew', 40)
counter = 0

for i in range(1,2):
    places.append(places)

pygame.draw.rect(screen, (151, 240, 178), pygame.Rect(300, 800, 400, 20), border_radius=10)
pygame.draw.rect(screen, (253, 66, 68), pygame.Rect(300, 800, 4*(100-health), 20), border_radius=10, border_top_right_radius=0, border_bottom_right_radius=0)

running = True
start_time = time.time()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pIndexY -= 1
            if event.key == pygame.K_DOWN:
                pIndexY += 1
            if event.key == pygame.K_LEFT:
                pIndexX -= 1
            if event.key == pygame.K_RIGHT:
                pIndexX += 1
                
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen, (255,255,255), (350,350,300,300), 15)
    
    if pIndexX > 9:
        pIndexX = 9
    if pIndexY > 9:
        pIndexY = 9
    if pIndexX < 1:
        pIndexX = 1
    if pIndexY < 1:
        pIndexY = 1

    places = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    places[10*pIndexY+pIndexX] = 1
    cycle += 1
    places[10*enemyIndexY+enemyIndexX] = 2
    # Round 1
    if gameRound == 1:
        cycle = (cycle%(900-4*int(score)))
        if (time.time()-start_time < 4) :
            if ((time.time()-start_time)%0.75>0.375) :
                screen.blit(font.render("Round 1", True, (255, 255, 255)), (500-(font.render("Round 1", True, (255, 255, 255))).get_width()/2,50))
        else:
            screen.blit(font.render("Round 1", True, (255, 255, 255)), (500-(font.render("Round 1", True, (255, 255, 255))).get_width()/2,50))
            if 0 == math.floor(cycle/60):
                for x in range(1,10):
                    places[enemyIndexY*10+x]=2
                    places[enemyIndexX+x*10]=2
            if cycle == 61:
                enemyIndexX = random.randint(1,9)
                enemyIndexY = random.randint(1,9)
                if enemyIndexX == pIndexX and enemyIndexY == pIndexY:
                    enemyIndexX = random.randint(1,9)
                    enemyIndexY = random.randint(1,9)
                    if enemyIndexX == pIndexX and enemyIndexY == pIndexY:
                        enemyIndexX = random.randint(1,9)
                        enemyIndexY = random.randint(1,9)
                score += 1
            if score > 20:
                places[10*enemyIndexY2+enemyIndexX2] = 2
                if 0 == math.floor(cycle/60):
                    for y in range(1,10):
                        places[(enemyIndexY2)*10+y]=2
                        places[enemyIndexX2+y*10]=2
                if cycle == 61:
                    enemyIndexX2 = random.randint(1,9)
                    enemyIndexY2 = random.randint(1,9)
                    if enemyIndexX2 == pIndexX and enemyIndexY2 == pIndexY:
                        enemyIndexX2 = random.randint(1,9)
                        enemyIndexY2 = random.randint(1,9)
                        if enemyIndexX2 == pIndexX and enemyIndexY2 == pIndexY:
                            enemyIndexX2 = random.randint(1,9)
                            enemyIndexY2 = random.randint(1,9)
            if score > 40:
                places[10*enemyIndexY3+enemyIndexX3] = 2
                if 0 == math.floor(cycle/60):
                    for z in range(1,10):
                        places[(enemyIndexY3)*10+z]=2
                        places[enemyIndexX3+z*10]=2
                if cycle == 61:
                    enemyIndexX3 = random.randint(1,9)
                    enemyIndexY3 = random.randint(1,9)
                    if enemyIndexX3 == pIndexX and enemyIndexY3 == pIndexY:
                        enemyIndexX3 = random.randint(1,9)
                        enemyIndexY3 = random.randint(1,9)
                        if enemyIndexX3 == pIndexX and enemyIndexY3 == pIndexY:
                            enemyIndexX3 = random.randint(1,9)
                            enemyIndexY3 = random.randint(1,9)
        
        if (score == 50):
            start_time = time.time()
            gameRound = 2
    # Round 2
    elif gameRound == 2:
        cycle = (cycle%(900-3*(int(score)-50)))
        if (time.time()-start_time < 4) :
            if ((time.time()-start_time)%0.75>0.375) :
                cycle = 51
                screen.blit(font.render("Round 2", True, (255, 255, 255)), (500-(font.render("Round 2", True, (255, 255, 255))).get_width()/2,50))
        else:
            screen.blit(font.render("Round 2", True, (255, 255, 255)), (500-(font.render("Round 2", True, (255, 255, 255))).get_width()/2,50))
            if 0 == math.floor(cycle/45):
                for x in range(1,10):
                    places[(enemyIndexY)*10+x]=2
                    places[enemyIndexX+x*10]=2
            if cycle == 46:
                enemyIndexX = random.randint(1,9)
                enemyIndexY = random.randint(1,9)
                if enemyIndexX == pIndexX and enemyIndexY == pIndexY:
                    enemyIndexX = random.randint(1,9)
                    enemyIndexY = random.randint(1,9)
                    if enemyIndexX == pIndexX and enemyIndexY == pIndexY:
                        enemyIndexX = random.randint(1,9)
                        enemyIndexY = random.randint(1,9)
                score += 1
            if score > 55:
                places[10*enemyIndexY2+enemyIndexX2] = 2
                if 0 == math.floor(cycle/45) or 4 == math.floor(cycle/45):
                    for y in range(1,10):
                        places[(enemyIndexY2)*10+y]=2
                        places[enemyIndexX2+y*10]=2
                if cycle == 46 or cycle == 181:
                    enemyIndexX2 = random.randint(1,9)
                    enemyIndexY2 = random.randint(1,9)
                    if enemyIndexX2 == pIndexX and enemyIndexY2 == pIndexY:
                        enemyIndexX2 = random.randint(1,9)
                        enemyIndexY2 = random.randint(1,9)
                        if enemyIndexX2 == pIndexX and enemyIndexY2 == pIndexY:
                            enemyIndexX2 = random.randint(1,9)
                            enemyIndexY2 = random.randint(1,9)
            if score > 79:
                start_time = time.time()
                gameRound = 3
    elif gameRound == 3:
        cycle = (cycle%(900-3*(int(score)-90)))
        if (time.time()-start_time < 4) :
            if ((time.time()-start_time)%0.75>0.375) :
                cycle = 51
                screen.blit(font.render("Round 3", True, (255, 255, 255)), (500-(font.render("Round 3", True, (255, 255, 255))).get_width()/2,50))
        else:
            screen.blit(font.render("Round 3", True, (255, 255, 255)), (500-(font.render("Round 3", True, (255, 255, 255))).get_width()/2,50))
            if 0 == math.floor(cycle/45):
                for x in range(1,10):
                    places[(enemyIndexY)*10+x]=2
                    places[enemyIndexX+x*10]=2
            if cycle == 46:
                enemyIndexX = random.randint(1,9)
                enemyIndexY = random.randint(1,9)
                if enemyIndexX == pIndexX and enemyIndexY == pIndexY:
                    enemyIndexX = random.randint(1,9)
                    enemyIndexY = random.randint(1,9)
                    if enemyIndexX == pIndexX and enemyIndexY == pIndexY:
                        enemyIndexX = random.randint(1,9)
                        enemyIndexY = random.randint(1,9)
                score += 1
            if score > 100:
                places[10*enemyIndexY2+enemyIndexX2] = 2
                if math.floor((600-3*int(score-55))/90) == math.floor(cycle/45):
                    for y in range(1,10):
                        places[(enemyIndexY2)*10+y]=2
                        places[enemyIndexX2+y*10]=2
                if cycle == (600-3*int(score-55))/2+46:
                    enemyIndexX2 = random.randint(1,9)
                    enemyIndexY2 = random.randint(1,9)
                    if enemyIndexX2 == pIndexX and enemyIndexY2 == pIndexY:
                        enemyIndexX2 = random.randint(1,9)
                        enemyIndexY2 = random.randint(1,9)
                        if enemyIndexX2 == pIndexX and enemyIndexY2 == pIndexY:
                            enemyIndexX2 = random.randint(1,9)
                            enemyIndexY2 = random.randint(1,9)

            if score > 120:
                places[10*enemyIndexY3+enemyIndexX3] = 2
                if math.floor((600-3*int(score-55))/90) == math.floor(cycle/45):
                    for y in range(1,10):
                        places[(enemyIndexY3)*10+y]=2
                        places[enemyIndexX3+y*10]=2
                if cycle == (600-3*int(score-55))/2+46:
                    enemyIndexX3 = random.randint(1,9)
                    enemyIndexY3 = random.randint(1,9)
                    if enemyIndexX3 == pIndexX and enemyIndexY3 == pIndexY:
                        enemyIndexX3 = random.randint(1,9)
                        enemyIndexY3 = random.randint(1,9)
                        if enemyIndexX3 == pIndexX and enemyIndexY3 == pIndexY:
                            enemyIndexX3 = random.randint(1,9)
                            enemyIndexY3 = random.randint(1,9)

            if (score>129):
                start_time = time.time()
                gameRound = 4
                recordHealth = (100+health)/2
                while (health<recordHealth):
                    health+=0.04
    
    if (score<21):
        screen.blit(font.render("21", True, (255, 255, 255)), (500-(font.render("21", True, (255, 255, 255))).get_width()/2,250))
    elif (score>20 and score<41):
        screen.blit(font.render("41", True, (255, 255, 255)), (500-(font.render("41", True, (255, 255, 255))).get_width()/2,250))
    elif (score>40 and score<50):
        screen.blit(font.render("50", True, (255, 255, 255)), (500-(font.render("50", True, (255, 255, 255))).get_width()/2,250))
    elif (score>49 and score<56):
        screen.blit(font.render("56", True, (255, 255, 255)), (500-(font.render("56", True, (255, 255, 255))).get_width()/2,250))
    elif (score>55 and score<80):
        screen.blit(font.render("80", True, (255, 255, 255)), (500-(font.render("80", True, (255, 255, 255))).get_width()/2,250))
    elif (score>79 and score<101):
        screen.blit(font.render("101", True, (255, 255, 255)), (500-(font.render("101", True, (255, 255, 255))).get_width()/2,250))
    elif (score>100 and score<121):
        screen.blit(font.render("121", True, (255, 255, 255)), (500-(font.render("121", True, (255, 255, 255))).get_width()/2,250))
    elif (score>120 and score<130):
        screen.blit(font.render("130", True, (255, 255, 255)), (500-(font.render("130", True, (255, 255, 255))).get_width()/2,250))
    for k in range(0,100):
        if places[k] == 1:
            screen.blit(pygame.image.load("player.jpg"),(335+30*((k%10)),335+30*((k-(k%10))/10)))
        if places[k] == 2:
            screen.blit(pygame.image.load("enemy.jpg"),(335+30*((k%10)),335+30*((k-(k%10))/10)))
            if 10*pIndexY+pIndexX == k:
                health -= 0.04

    pygame.draw.rect(screen, (151, 240, 178), pygame.Rect(300, 800, 400, 20), border_radius=10)
    if (health>=2.5):
        pygame.draw.rect(screen, (253, 66, 68), pygame.Rect(300, 800, 4*(100-health), 20), border_radius=10, border_top_right_radius=0, border_bottom_right_radius=0)
    else:
        pygame.draw.rect(screen, (253, 66, 68), pygame.Rect(300, 800, 4*(100-health), 20), border_radius=10)
    #calibri
    #couriernew
    #consolas
    #lucidaconsole
    screen.blit(font.render(str(score), True, (255, 255, 255)), (500-(font.render(str(score), True, (255, 255, 255))).get_width()/2,100))
    screen.blit(font.render("Next Milestone:", True, (255, 255, 255)), (320,200))
    if (health<=0):
        endGame = 1
        health = 0
    if (endGame == 1):
        counter += 0.1
        for x in range(0,math.floor(counter)):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10*x, 0, 10, 10*(counter-x)))
    if (counter>250):
        screen.blit(pygame.font.SysFont('couriernew', 80).render("Game Over", True, (0, 0, 0)), (min(10*(counter-284)-300,284),454.4))
    if (counter>400):
        running = False
    pygame.display.update()
