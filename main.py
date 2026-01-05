import pygame
from player import Player
from logger import log_state
from constants import *
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)
        for ast in asteroids:
            if player1.collides_with(ast):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for ast in asteroids:
            for s in shots:
                if ast.collides_with(s):
                    log_event("asteroid_shot")
                    ast.split()
                    s.kill()

        pygame.display.flip()
        dt = clock.tick(60)/1000      
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
