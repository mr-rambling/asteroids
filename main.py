import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    field = AsteroidField()

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the frame rate to 60 FPS
        dt = timer.tick(60) / 1000

        for asteroid in asteroids:
            if asteroid.collision(player1):
                print("Game over!")
                print(f"Score: {score}")
                return
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    score += 1

if __name__ == "__main__":
    main()