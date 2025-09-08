from settings import *
from Snake import Snake, Apple  

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
        pygame.display.set_caption('~Snakeyy~')
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.apple_group = pygame.sprite.Group()
        self.snake = Snake(self.all_sprites)
        self.apple = Apple(self.all_sprites)
        self.apple_group.add(self.apple)

    def Food_Touched(self):
        if pygame.sprite.spritecollide(self.snake,self.apple_group,True):
            self.apple = Apple(self.all_sprites)
            self.apple_group.add(self.apple)

    def run(self):
        while self.running:

            dt = self.clock.tick(60)/1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running  = False

            #update
            pygame.display.flip()
            self.Food_Touched()
            self.all_sprites.update(dt)

            #draw
            self.display.fill("black")
            self.all_sprites.draw(self.display)
        
        pygame.quit()


if __name__ == '__main__':    
    game = Game()
    game.run()

    

        
    
    

