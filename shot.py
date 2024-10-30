# Create a new shot class that inherits from the CircleShape class that represents a bullet

import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.update_image()

    def update_image(self):
        self.image.fill((0, 0, 0, 0))  # Clear the image
        pygame.draw.circle(self.image, "white", (self.radius, self.radius), self.radius)

    def update_position(self, time_delta):
        self.position += self.velocity * time_delta
        self.rect.center = self.position
        
    def update(self, dt):
        self.update_position(dt)
        self.update_image()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def handle_collision(self, other):
        self.image.fill((0, 0, 0, 0))  # Clear the image
        self.kill()