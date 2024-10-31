import pygame
import random

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def handle_collision(self, other: 'CircleShape'):
        self.kill()
        number_of_particles = random.randint(1000, 1500)
        for _ in range(number_of_particles):
            particle = Particle(self.position.x, self.position.y)
            angle = random.uniform(0, 360)
            speed = random.uniform(5, 50)
            particle.velocity = pygame.Vector2(speed, 0).rotate(angle) * speed
            particle.lifetime = random.uniform(.1, .5)
        current_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - current_time < 3000:
            pass
        pygame.quit()

    def check_collision(self, other: 'CircleShape'):
        if other.type in ('player', 'asteroid'):  # List types that should collide
            distance = self.position.distance_to(other.position)
            return distance < self.radius + other.radius
        return False

    def update(self, dt):
        # sub-classes must override
        pass

    