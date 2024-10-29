import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def handle_collision(self, other):
        self.split()

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return # do not split small asteroids
        
        # Generate two new angles to split in opposite directions
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2
        
        # Create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        asteroid1.velocity = new_velocity1
        
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        asteroid2.velocity = new_velocity2

        # Add the new asteroids to the sprite group
        asteroid1.add(self.containers)
        asteroid2.add(self.containers)
        
        
        
