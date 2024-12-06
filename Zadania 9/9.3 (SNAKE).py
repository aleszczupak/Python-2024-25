import pygame
import random
import sys

pygame.init()

pygame.font.init()
move_font = pygame.font.SysFont('Consolas', 20)
font = pygame.font.SysFont('Consolas', 50, bold=True)

window_size = 800
tile_size = 40
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Snake')
# kafelki
tile_centers = (tile_size//2, window_size-tile_size//2, tile_size)
random_position = lambda: [random.randrange(*tile_centers),
                           random.randrange(*tile_centers)]
# głowa węża
snake = pygame.rect.Rect([0, 0, tile_size-2, tile_size-2])
# pozycja węża
snake.center = random_position()
# długość węża
snake_length = 1
snake_segments = [snake.copy()]
# poruszanie się węża
snake_direction = (0, 0)
directions = {pygame.K_UP: 1, pygame.K_DOWN: 1,
              pygame.K_RIGHT: 1, pygame.K_LEFT: 1}
# prędkość węża
start_time = 0.0000001
time, time_step = 0, 250 # opóźnienie [ms]
# czas życia danego owocu [ms]
fruit_time, living_time = 0, 10000

# owoce
fruit = pygame.rect.Rect([0, 0, tile_size-2, tile_size-2])
fruit.center = random_position()
type_fruit = 1
# zjedzone owoce
score = 0
# odliczanie czasu - gra się zakończy po 100 sekudach
counter = 100
counter_txt = font.render(str(counter), True, 'white')
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

clock = pygame.time.Clock()
t = 60

done = False
finish = False

# pętla główna
while not done:
    screen.fill('black')
    move_txt = move_font.render('Ruch węża strzałkami', True, 'white')
    screen.blit(move_txt, (550, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == timer_event:
            counter -= 1
            counter_txt = font.render(str(counter), True, 'white')
            
    if not finish:
        screen.blit(counter_txt, (20, 20))

        # poruszanie węża po planszy i zabronienie ruchu w przeciwnym kierunku
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if directions[pygame.K_UP]:
                snake_direction = (0, -tile_size)
                directions = {pygame.K_UP: 1, pygame.K_DOWN: 0,
                            pygame.K_RIGHT: 1, pygame.K_LEFT: 1}
            else:
                finish = True
        if keys[pygame.K_DOWN]:
            if directions[pygame.K_DOWN]:
                snake_direction = (0, tile_size)
                directions = {pygame.K_UP: 0, pygame.K_DOWN: 1,
                                pygame.K_RIGHT: 1, pygame.K_LEFT: 1}
            else:
                finish = True
        if keys[pygame.K_RIGHT]:
            if directions[pygame.K_RIGHT]:
                snake_direction = (tile_size, 0)
                directions = {pygame.K_UP: 1, pygame.K_DOWN: 1,
                                pygame.K_RIGHT: 1, pygame.K_LEFT: 0}
            else:
                finish = True
        if keys[pygame.K_LEFT]:
            if directions[pygame.K_LEFT]:
                snake_direction = (-tile_size, 0)
                directions = {pygame.K_UP: 1, pygame.K_DOWN: 1,
                                pygame.K_RIGHT: 0, pygame.K_LEFT: 1}
            else:
                finish = True
                
        # rysowanie węża zbudowanego z 'klocków'
        [pygame.draw.rect(screen, 'green', seg) for seg in snake_segments]

        # ruch węża
        start_time = pygame.time.get_ticks()
        time_now = pygame.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_direction)
            snake_segments.append(snake.copy())
            snake_segments = snake_segments[-snake_length:]

        # rysowanie owocu pożywnego i zatrutego
        if type_fruit == 1:
            pygame.draw.rect(screen, 'red', fruit)
        if type_fruit == 0:
            pygame.draw.rect(screen, 'blue', fruit)

        # interakcja węża z poszczególnymi rodzajami owoców
        if snake.center == fruit.center:
            if type_fruit == 1:           
                snake_length += 1
                score += 1
            if type_fruit == 0:
                snake_length -=1
                score -=1
            if snake_length == 0:
                finish == True
            type_fruit = random.randint(0, 1)
            fruit.center = random_position()
            # fruit_time_now = pygame.time.get_ticks()

        # zmiana miejsca i typu owocu na planszy
        fruit_time_now = pygame.time.get_ticks()
        if fruit_time_now - fruit_time > living_time:
            type_fruit = random.randint(0, 1)
            fruit.center = random_position()
            fruit_time = fruit_time_now
            # wzrastająca prędkość węża
            time_step -= 25
        if time_step == 0:
            finish = True

        # zakończ grę po 100 sekundach
        if counter == 0:
            finish = True
            
        # sprawdzenie uderzenia w krawędź albo samozjedzenia
        self_eat = pygame.Rect.collidelist(snake, snake_segments[:-1]) != -1
        if snake.left < 0 or snake.right > window_size or snake.top < 0\
           or snake.bottom > window_size or self_eat:
            finish = True

    if finish:
        screen.fill('black')
        game_txt = font.render('Koniec gry!', True, 'white')
        score_txt = font.render('Wynik: '+str(score), True, 'white')
        screen.blit(game_txt, (window_size/2-150, window_size/2-50))
        screen.blit(score_txt, (window_size/2-130, window_size/2+20))
    
    pygame.display.flip()
    clock.tick(t)

pygame.quit()
