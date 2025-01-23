import pygame
from pygame.math import Vector2
from block import Block
import data.main_data
import copy
from item import Item

class Player(pygame.sprite.Sprite):
    LEFT = 0
    RIGHT = 1
    VERTICAL = 2

    velocity = 0.3

    def __init__(self, position, block_group: pygame.sprite.Group, item_group: pygame.sprite.Group, speed = 5):
        pygame.sprite.Sprite.__init__(self)

        self.size = size = (25, 25)

        images = []
        images.append(pygame.image.load('resources/character.png'))

        self.rect = pygame.Rect(position, size)
        self.item_group = item_group
        self.images = [pygame.transform.scale(image, size) for image in images]
        self.index = 0
        self.image = self.images[self.index] 
        self.speed = speed
        
        self.force = 0.1
        self.energy = 100

        self.block_group = block_group

    def update(self):
        self.last_loc = self.rect
        
        data.main_data.recent_pos.append(copy.deepcopy(self.rect))
        # if len(data.main_data.recent_pos) >= 2: print(f'{data.main_data.recent_pos[0].center} => {data.main_data.recent_pos[1].center}')
        if len(data.main_data.recent_pos) >= 3: data.main_data.recent_pos.pop(0)
        self.image = self.images[self.index]

    def move(self, direction, fps):
        self.detect_collision()
        if direction == self.LEFT:
            self.rect.x -= self.speed * fps
        if direction == self.RIGHT:
            self.rect.x += self.speed * fps
        if direction == self.VERTICAL:
            self.rect.y += self.velocity * (fps / 60)
            self.velocity += self.force * (fps / 60)
            

    '''
    Must be run before update
    '''
    def detect_collision(self):
        collisions: list[Block] = pygame.sprite.spritecollide(self, self.block_group, False)
        
        result = []

        dmx = 0
        dpx = 0
        dmy = 0
        dpy = 0

        is_collide = False

        # if len(collisions) != 0:
        #     print()
        #     print(len(collisions))
        #     self.energy = 100

        for collision in collisions:
            if collision.type != 0:
                
                print(f"{data.main_data.recent_pos[0].right} < {collision.rect.left} < {data.main_data.recent_pos[1].right}")
                if (collision.rect.left < data.main_data.recent_pos[1].right and collision.rect.left >= data.main_data.recent_pos[0].right) :
                    print("L")
                    dmx = abs(collision.rect.left - self.rect.right) + 1
                if (collision.rect.right > data.main_data.recent_pos[1].left and collision.rect.right <= data.main_data.recent_pos[0].left) :
                    print("R")
                    dpx = abs(collision.rect.right - self.rect.left) + 1
                if (collision.rect.top < data.main_data.recent_pos[1].bottom and collision.rect.top >= data.main_data.recent_pos[0].bottom) :
                    print("T")
                    dmy = abs(collision.rect.top - self.rect.bottom) + 1
                    is_collide = True
                    # self.velocity = 0
                    self.velocity = -7 * (self.energy / 100)
                
                if (collision.rect.bottom > data.main_data.recent_pos[1].top and collision.rect.bottom <= data.main_data.recent_pos[0].top) :
                    print("B")
                    dpy = abs(collision.rect.bottom - self.rect.top) + 1
                    result.append(2)
                    
                    # self.velocity = 0
                    self.velocity = 0
                # if (bottom < self.rect.bottom) and (bottom > self.last_loc.top):
                # if (collision.rect.bottom < self.rect.bottom):
                #     print("아래에서 충돌입니다!")
                #     dpy = abs(collision.rect.top - self.rect.bottom) - 1
                #     result.append(3)
                #     self.velocity = -7
                # if (collision.rect.left < data.main_data.recent_pos[1].right) and not(data.main_data.recent_pos[1].bottom < collision.rect.top):
                #     print("왼쪽에서 충돌입니다!")
                #     dmx = abs(collision.rect.left - self.rect.right) - 1
                #     result.append(0)
                # if (collision.rect.right > self.rect.left) and not(self.rect.bottom < collision.rect.top):
                # # if (right > self.rect.left) and (right < self.last_loc.right) and ((self.rect.bottom <= bottom) or (self.rect.top >= top)):
                #     print("오른쪽에서 충돌입니다!")
                #     dpx = abs(collision.rect.right - self.rect.left) + 1
                #     result.append(1)
                # # if (top > self.rect.top) and (top < self.last_loc.bottom) :

        # print(f'len : {len(collisions)}')
        # print(f'dx = {dpx} - {dmx}, dy = {dpy} - {dmy}')
        self.rect.x += (dpx - dmx) #d plus x - d minus x
        self.rect.y += (dpy - dmy)

        if is_collide: self.energy -= 2

        
            

    def teleport(self, pos):
        self.rect.center = pos

    # def check_collision(self, block_group):
    #     collisions: list[Block] = pygame.sprite.spritecollide(self, block_group, False)
    #     for collision in collisions:
    #         if collision.type == 1:
    #             A = self.rect.bottom > collision.rect.top
    #             return A
