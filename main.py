import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    clock = pygame.time.Clock()
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateables, drawables)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updateables, drawables)
    
    AsteroidField.containers = (updateables)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updateables, drawables)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
           
        for object in updateables:
            object.update(dt)
        
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                exit()

            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.kill()
                    shot.kill()

        screen.fill("black")
        for object in drawables:
            object.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
