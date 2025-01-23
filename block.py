import pygame

class Block(pygame.sprite.Sprite):
    VOID = 0
    NORMAL = 1
    GOAL = 2
    
    def __init__(self, type: int, position: tuple[int]):
        pygame.sprite.Sprite.__init__(self)

        size = (40, 40)

        images = []
        images.append(pygame.image.load('resources/block.png'))
        images.append(pygame.image.load('resources/goal.png'))

        self.type = type
        self.position = position

        self.rect = pygame.Rect(position, size)

        self.images = [pygame.transform.scale(image, size) for image in images]
        self.index = type - 1
        self.image = self.images[self.index]

    def update(self):
        self.image = self.images[self.index]
    
    def to_string(self):
        return f'type={self.type}, pos={self.rect.center}'
