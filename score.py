# score.py

import pygame
player_score = 0

pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)


def update(points):
    global player_score  # Use the global score variable
    player_score += points  # Update the global score by adding points
    
def draw(screen, player_score):
    score_surface = my_font.render(f'Score: {player_score}', True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))
