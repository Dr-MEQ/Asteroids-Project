import pygame
import random
from constants import *

shots = set()
from circleshape import CircleShape
from shot import Shot
from particles import Particle

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.type = "player"
        self.rotation = 0
        self.shoot_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle())

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
             
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_RATE
        shot = Shot(self.position.x, self.position.y, self.rotation)
        shots.add(shot)
        

    def handle_collision(self, other: 'CircleShape'):
        self.kill()
        number_of_particles = random.randint(100, 150)
        for _ in range(number_of_particles):
            particle = Particle(self.position.x, self.position.y)
            angle = random.uniform(0, 360)
            speed = random.uniform(5, 50)
            particle.velocity = pygame.Vector2(speed, 0).rotate(angle) * speed
            particle.lifetime = random.uniform(.1, .5)
        
        

        
