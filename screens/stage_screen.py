import pygame
from screens.abstract_screen import Screen
from stage import Stage
from player import Player
from block import Block
import data.main_data
from util import *
from item import Item

class StageScreen(Screen):
    def __init__(self, stage: Stage):
        self.stage = stage
        self.initize()

    def initize(self):
        stage = self.stage
        blocks = stage.get_game_blocks()
        self.block_group = block_group = pygame.sprite.Group(blocks)

        items = stage.get_game_items()

        goal_count = 0
        for item in items:
            if item.type == 'A' : goal_count += 1

        self.goal_count = goal_count
        self.item_group = item_group = pygame.sprite.Group(items)

        self.player = player = Player((100, 300), block_group, item_group, speed=0.05)
        self.players = pygame.sprite.Group(player) 

        self.moving_dir = []

        player.teleport(Stage.pos_converter(pos=stage.start_point))

        self.game_font = pygame.font.SysFont('Noto Sans KR ExtraBold', 60)
        self.info_font = pygame.font.SysFont('Noto Sans KR', 15)
        self.is_cleared = False
        self.stage = stage

    def handle_event(self, event: pygame.event.EventType) -> bool:
        moving_dir = self.moving_dir
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_dir.append(Player.LEFT)
            elif event.key == pygame.K_RIGHT:
                moving_dir.append(Player.RIGHT)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and Player.LEFT in moving_dir:
                moving_dir.remove(Player.LEFT)
            elif event.key == pygame.K_RIGHT and Player.RIGHT in moving_dir:
                moving_dir.remove(Player.RIGHT)
        return True

    def draw(self, screen: pygame.Surface):
        moving_dir = self.moving_dir
        player = self.player
        players = self.players
        block_group = self.block_group
        item_group = self.item_group
        for dir in moving_dir:
            player.move(dir, data.main_data.FPS)
        
        Fnet = player.force
        player.velocity += Fnet

        screen.fill((255, 255, 255))
        players.draw(screen)
        block_group.draw(screen)
        item_group.draw(screen)

        # 게임 오버
        if (player.rect.y > data.main_data.screen_height or player.energy <= 0) and not self.is_cleared:
            render = self.game_font.render("게임 오버!", True, (255, 0, 0))
            player.teleport(Stage.pos_converter(pos=self.stage.start_point))
            player.energy = 100
            player.velocity = 0

            # player.init 필요...
            screen.blit(render, (data.main_data.screen_width / 2, data.main_data.screen_height / 2))
            pygame.display.update()

            pygame.time.wait(1500)
            self.initize()
        
        # if player.energy > 0: player.energy -= 0.1 # 실전에서는 더 느리게
        # if player.energy <= 0: player.energy = 0
        # print(f'v = {player.velocity}')
        player.move(player.VERTICAL, fps=60)

        item_collisions: list[Item] = pygame.sprite.spritecollide(player, player.item_group, False)
        for collision in item_collisions:
            if collision.type == 'A':
                collision.remove(self.item_group)
                self.goal_count -= 1
                if self.goal_count <= 0:
                    render = self.game_font.render("클리어!!", True, (234, 191, 21))
                    screen.blit(render, (data.main_data.screen_width / 2, data.main_data.screen_height / 2))
                    pygame.display.update()

                    pygame.time.wait(1500)
                    self.initize()
                    data.main_data.stage += 1
            if collision.type == 'B':
                collision.remove(self.item_group)
                player.energy += 10
                if player.energy >= 100: player.energy = 100
                    
        
        
        # collisions: list[Block] = pygame.sprite.spritecollide(player, block_group, False)
        # for collision in collisions:
        #     if collision.type == 1:
        #         if dif.x > 0:
        #             player.rect.x = collision.rect.left - 1
        #             player.update()
        #         if dif.x < 0:
        #             player.rect.y = collision.rect.right + 1
        #             player.update()
        #         if dif.y >= 0:
        #             print(f"player = {player.rect.y}, collision = {collision.rect.top}")
        #             player.rect.y = collision.rect.top - player.size[0] - 1
        #             player.velocity = -10 * (player.energy / 100)
        #             player.energy -= 3
        #             player.update()
        #         if dif.y < 0:
        #             player.rect.y = collision.rect.bottom
        #             player.velocity = 0
        #             player.update()
        #     if collision.type == 2:
        #         block_group.remove(collision)
        #         self.is_cleared = True

        
        # if self.is_cleared:
            # render = self.game_font.render("클리어!!", True, (234, 191, 21))
            # screen.blit(render, (data.main_data.screen_width / 2, data.main_data.screen_height / 2))
            # pygame.display.update()

            # pygame.time.wait(1500)
            # data.main_data.stage += 1

        screen.blit(self.info_font.render("ENERGY: {:.1f}%".format(player.energy), True, (0, 0, 0)), (10, 10))
        screen.blit(self.info_font.render("{} GOALS LEFT!".format(self.goal_count), True, (0, 0, 0)), (10, 30))

    def update(self, screen: pygame.Surface):
        player = self.player
        # print(f'last = {player.last_loc}, now = {player.rect.center}')
        player.update()
        self.item_group.update()
        pygame.display.update()