import pygame
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)  # Initializes and adds particle to the container groups automatically
        self.type = "particle"
        self.position = pygame.Vector2(x, y)
        speed = random.uniform(1, 10)
        angle = random.uniform(0, 360)
        self.radius = random.randint(1, 3)
        self.lifetime = random.uniform(.1, .5)  # seconds
        self.velocity = pygame.Vector2(speed, 0).rotate(angle) * speed

    def update(self, dt):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
        self.position += self.velocity * dt

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 165, 0), self.position, self.radius)