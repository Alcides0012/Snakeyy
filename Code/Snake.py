from settings import *
from random import randint

class Snake(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface((20,20))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = (S_WIDTH//2,S_HEIGHT//2))
        self.direction = pygame.math.Vector2(1,0)
        self.speed = 300

    def movement(self,dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.direction.x != -1:
            self.direction = pygame.math.Vector2(1,0)
        elif keys[pygame.K_LEFT] and self.direction.x != 1:
            self.direction = pygame.math.Vector2(-1,0)
        elif keys[pygame.K_UP] and self.direction.y != 1:
            self.direction = pygame.math.Vector2(0,-1)
        elif keys[pygame.K_DOWN] and self.direction.y != -1:
            self.direction = pygame.math.Vector2(0,1)

        self.rect.center += self.direction *self.speed *dt

    def update(self,dt):
        self.movement(dt)

class Apple(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface((20,20))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = (randint(20,S_WIDTH-20),randint(20,S_HEIGHT - 20)))
        
        
        
        