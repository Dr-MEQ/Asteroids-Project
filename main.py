import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from particles import Particle


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
    global particle_group
    particle_group = pygame.sprite.Group()
    Particle.containers = (particle_group, updatable, drawable)
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
                    player.shoot()  # Attempt to call the shoot method

        # Check for collisions
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                pygame.quit()
                return
            for obj in asteroids:
                for other_asteroid in asteroids:
                    if asteroid != other_asteroid and asteroid.check_collision(other_asteroid):
                        # Calculate the collision normal
                        collision_normal = (asteroid.position - other_asteroid.position).normalize()
                        # check for asteroid overlap
                        overlap = (asteroid.radius + other_asteroid.radius) - (asteroid.position - other_asteroid.position).length()
                        correction_vector = collision_normal * overlap / 2
                        asteroid.position += correction_vector
                        other_asteroid.position -= correction_vector
                        # Calculate the masses
                        asteroid.mass = asteroid.radius
                        other_asteroid.mass = other_asteroid.radius
                        # Calculate the absorbed factor
                        absorbed_factor = .9
                        # Calculate the new velocities, based on mass and previous velocity
                        m1, m2 = asteroid.mass, other_asteroid.mass
                        v1, v2 = asteroid.velocity, other_asteroid.velocity
                        new_v1 = ((m1 - m2) / (m1 + m2)) * v1 + (2 * m2 / (m1 + m2)) * v2
                        new_v2 = ((m2 - m1) / (m1 + m2)) * v2 + (2 * m1 / (m1 + m2)) * v1
                        # Apply absorption
                        asteroid.velocity = new_v1 #* absorbed_factor
                        other_asteroid.velocity = new_v2 #* absorbed_factor
                        
            
                        
            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.handle_collision(shot)
                    shot.handle_collision(asteroid)
                
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
