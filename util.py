import pygame

def tuple_to_vector2(t: tuple):
    result = pygame.Vector2()
    result.x = t[0]
    result.y = t[1]
    return result