import pygame
import math

# 위 아래 sin처럼 흔들흔들거리게
# 골인지점도 여기로
# TODO
class Item(pygame.sprite.Sprite):
    GOAL = 'A'
    ENERGY = 'B'
    
    def __init__(self, type: str, position: tuple[int]):
        pygame.sprite.Sprite.__init__(self)

        size = (40, 40)

        images = {}
        images['A'] = pygame.image.load('resources/goal.png')
        images['B'] = pygame.image.load('resources/energy.png')

        self.type = type

        self.rect = pygame.Rect(position, size)
        self.position = position

        for key, value in images.items():
            images[key] = pygame.transform.scale(value, size)

        self.images = images
        self.image = self.images[self.type]
        self.t = 0

    def update(self):
        self.t += 0.05
        self.rect.y = self.position[1] + 10 * math.sin(self.t)
        # if self.t >= 2 * math.pi: self.t = 0
    
    def to_string(self):
        return f'type={self.type}, pos={self.rect.center}'
