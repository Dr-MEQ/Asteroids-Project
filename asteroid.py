import pygame
import random
from constants import *
from circleshape import CircleShape
from particles import Particle


class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color=None):
        super().__init__(x, y, radius)
        self.type = "asteroid"
        self.color = color or (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def handle_collision(self, other):
        self.split()

    def split(self):
        self.kill()
        number_of_particles = random.randint(100, 150)
        for _ in range(number_of_particles):
            particle = Particle(self.position.x, self.position.y)
            angle = random.uniform(0, 360)
            speed = random.uniform(5, 50)
            particle.velocity = pygame.Vector2(speed, 0).rotate(angle) * speed
            particle.lifetime = random.uniform(.1, .5)
                    
        if self.radius <= ASTEROID_MIN_RADIUS:
            return # do not split small asteroids
        
        # Generate two new angles to split in opposite directions
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle) * 1.4
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.4
        
        # Create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS, self.color)
        asteroid1.velocity = new_velocity1
        
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS, self.color)
        asteroid2.velocity = new_velocity2

        # Add the new asteroids to the sprite group
        asteroid1.add(self.containers)
        asteroid2.add(self.containers)
        
        
        
