import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    global asteroids
    asteroids = pygame.sprite.Group()
    global shots
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # Check if any key is pressed
                if event.key == pygame.K_SPACE:  # Check specifically for the spacebar
                    print("Spacebar pressed!")  # Print to confirm it's detected
                    player.shoot()  # Attempt to call the shoot method

        # Check for collisions
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                pygame.quit()
                return
            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.handle_collision(shot)
                    shot.handle_collision(asteroid)
                
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
