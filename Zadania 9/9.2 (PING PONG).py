import pygame
import sys, random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
bottle_green = (20, 30, 2)
width, height = 1250, 700
pygame.font.init()
font_title = pygame.font.SysFont('Consolas', 40, bold=True)
font_score = pygame.font.SysFont('Consolas', 45, bold=True)
font_over = pygame.font.SysFont('Consolas', 80, bold=True)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong!')
clock = pygame.time.Clock()
t = 300

# paletki
paddle1 = pygame.Rect(0, 0, 15, 100)
paddle2 = pygame.Rect(0, 0, 15, 100)
paddle1.center = (width-100, height/2)
paddle2.center = (100, height/2)

# piłka
ball = pygame.Rect(0, 0, 20, 20)
ball.center = (width/2, height/2)

# prędkość piłki
v = 0.75
vx, vy = v, v

# wyniki
score1, score2 = 0, 0

done = False
finish = False
end_score = 11

while not done:
    screen.fill(bottle_green)
    title_text = font_title.render('Gramy do ' + str(end_score)+' punktów!',
                                   False, white)
    screen.blit(title_text, (width/2-200, 50))

    # rysowanie obiektów
    pygame.draw.rect(screen, blue, paddle1)
    pygame.draw.rect(screen, red, paddle2)
    pygame.draw.circle(screen, white, ball.center, 15)
    pygame.draw.lines(screen, white, True,
                      [(10, 10), (width-10, 10),
                       (width-10, height-10), (10, height-10)],
                      width=3)
    pygame.draw.line(screen, white, (width/2, 120), (width/2, height-120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not finish:
        # poruszanie paletkami
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if paddle1.top > 0:
                paddle1.top -= 2
        if keys[pygame.K_DOWN]:
            if paddle1.bottom < height:
                paddle1.bottom += 2

        # ruch piłki
        ball.x += vx * 2
        ball.y += vy * 2

        # odbicie piłki od brzegu
        if ball.bottom >= height:
            vy = -v
        if ball.top <= 0:
            vy = v
        # dodanie punktu i odbicie piłki od brzegu    
        if ball.left <= 0:
            score1 += 1
            # powrót piłki do centrum stołu
            ball.center = (width/2, height/2)
            vx, vy = random.choice([-v, v]), random.choice([-v, v])
        if ball.right >= width:
            score2 += 1
            ball.center = (width/2, height/2)
            vx, vy = random.choice([-v, v]), random.choice([-v, v])
        # uderzenie piłki w paletkę
        if paddle1.x - ball.width <= ball.x <= paddle1.right and ball.y in range(paddle1.top - ball.width, paddle1.bottom + ball.width):
            vx = -v
        if paddle2.x - ball.width <= ball.x <= paddle2.right and ball.y in range(paddle2.top - ball.width, paddle2.bottom + ball.width):
            vx = v

        # ruch paletki komputera
        if paddle2.bottom < ball.top:
            paddle2.y += 1.5
        if paddle2.top > ball.bottom:
            paddle2.y -= 1.5

        # wyświetlanie wyniku
        pygame.draw.lines(screen, white, True,
                          [(width/2-95, 610), (width/2+100, 610),
                           (width/2+100, 670), (width/2-95, 670)])
        score1_txt = font_score.render(str(score1), True, white)
        score2_txt = font_score.render(str(score2), True, white)
        colon = font_score.render(':', True, white)
        screen.blit(score1_txt, (width/2+40, 620))
        screen.blit(score2_txt, (width/2-60, 620))
        screen.blit(colon, (width/2-10, 620))
            
        # zakończenie gry
        if score1 == end_score or score2 == end_score:
            finish = True
        
    if finish:
        screen.fill(bottle_green)
        if score1 == end_score:
            final_text = font_over.render('Wygranaaa!', False, white)
        else:
            final_text = font_over.render('Przegrana!', False, white)
        screen.blit(final_text, (width/2-200, height/2-50))
           
    pygame.display.flip()
    clock.tick(t)
    
pygame.quit()
