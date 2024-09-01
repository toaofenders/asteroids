# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for drawer in drawable:
            drawer.draw(screen)
        for updater in updatable:
            updater.update(dt)
        pygame.display.flip()

        dt= clock.tick(60) / 1000

if __name__ == "__main__":
    main()