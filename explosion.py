class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.pos = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2()
        self.lifetime = 1.0  # seconds

    def update(self, dt):
    self.lifetime -= dt
    if self.lifetime <= 0:
        self.kill()  # removes particle from all sprite groups
    self.pos += self.velocity * dt

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 165, 0), self.pos, 2)  # small orange dot