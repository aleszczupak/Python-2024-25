import pygame
import random

pygame.init()
 
lightblue = (176, 224, 230)
white  = (255, 255, 255)
navy = (0, 0, 128)

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Padający śnieg')
t = 20
snow = []
r = 15
thr = height
for i in range(t):
    x = random.randrange(r, width-r)
    y = random.randrange(-250, 0)
    snow.append([x, y])
 
clock = pygame.time.Clock()
done = False
finish = False

while not done:
    screen.fill(lightblue)
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True
    
    if not finish:
        for i in range(len(snow)):
            pygame.draw.circle(screen, white, snow[i], r)    
            snow[i][1] += 1 # spadanie
            if pygame.mouse.get_pressed()[0]:
                p = pygame.mouse.get_pos()
                if((snow[i][0]-r < p[0] and snow[i][0]+r > p[0]) and
                   (snow[i][1]-r < p[1] and snow[i][1]+r > p[1])):
                    y = random.randrange(-250, 0)
                    snow[i][1] = y               
                    x = random.randrange(r, width-r)
                    snow[i][0] = x
            # wersja z zaspami śniegu
            if snow[i][1] == thr:
                y = random.randrange(-250, 0)
                snow[i][1] = y               
                x = random.randrange(r, width-r)
                snow[i][0] = x
                thr -= 2 * r
            if thr < height:
                box = pygame.Rect(0, thr, width, height-thr)
                pygame.draw.rect(screen, white, box)
            if thr <= r:
                del snow
                finish = True
                break
            # wersja z dolną krawędzią ekranu
            '''if snow[i][1] >= height:
                del snow
                finish = True
                break'''
    if finish:        
        pygame.font.init() 
        font = pygame.font.SysFont('Consolas', 75, bold=True)
        text_surface = font.render('Koniec gry!', False, navy)
        screen.blit(text_surface, (23, 200))
        
    pygame.display.flip()
    clock.tick(t)
    
pygame.quit()
