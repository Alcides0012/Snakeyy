import pygame
import random

pygame.init()

Height, Width = 600, 600
screen = pygame.display.set_mode((Width, Height))

clock = pygame.time.Clock()
FPS = 24

snake_dir = (5, 0)
snake_size = 10
snake = [(Width//2, Height//2),(Width//2 -snake_size,Height//2 -snake_size),(Width//2 - (2*snake_size), Height//2 - (2*snake_size)) ]

apple = (random.randrange(0,Width,snake_size),random.randrange(0,Height,snake_size))

running = True


while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0,10): snake_dir = (0,-10)
    if keys[pygame.K_DOWN] and snake_dir != (0,-10): snake_dir = (0,10)
    if keys[pygame.K_LEFT] and snake_dir != (10 ,0): snake_dir = (-10,0)
    if keys[pygame.K_RIGHT] and snake_dir != (-10,0): snake_dir = (10,0)

    head = (snake[0][0] + snake_dir[0], snake[0][1] +snake_dir[1])
    snake.insert(0,head)

    if head == apple :
        apple = (random.randrange(0,Width,snake_size),random.randrange(0,Height,snake_size))
    else:
        snake.pop()

    screen.fill('black')
    for body in snake:
        pygame.draw.rect(screen,(0,255,0),(*body,snake_size,snake_size))
    pygame.draw.rect(screen,(255,0,0),(*apple, snake_size,snake_size))

    pygame.display.flip()

pygame.quit()
