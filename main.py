import pygame
from player import Player
from logger import log_state
from constants import *
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from highscoring import *
from logger import log_event
import sys
import pickle
import os

def main():
    pygame.init()
    current_highscore = load_highscore()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
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
        updatable.update(dt)
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        for ast in asteroids:
            if player1.collides_with(ast):
                log_event("player_hit")
                print("---------- GAME OVER! ----------")
                print()
                print(f"SCORE: {player1.score}")
                if player1.score > current_highscore:
                    print(f"NEW HIGHSCORE! {player1.score}")
                    save_highscore(player1.score)
                print(f"CURRENT HIGHSCORE: {current_highscore}")
                print()
                print("---- THANK YOU FOR PLAYING! -----")
                sys.exit()
        for ast in asteroids:
            for s in shots:
                if ast.collides_with(s):
                    log_event("asteroid_shot")
                    if ast.radius == ASTEROID_MIN_RADIUS:
                        player1.score += 50
                    elif ast.radius == ASTEROID_MAX_RADIUS:
                        player1.score += 100
                    else:
                        player1.score += 75
                    ast.split()
                    s.kill()

        pygame.display.flip()
        dt = clock.tick(60)/1000      
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
