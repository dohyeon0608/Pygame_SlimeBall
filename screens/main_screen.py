import pygame
from screens.abstract_screen import Screen
from screens.util.button import Button
import data.main_data

class MainScreen(Screen):
    def __init__(self):
        screen_width = 1080
        screen_height = 720
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.background = pygame.image.load('resources/mainscreen.png')
        pygame.display.set_caption("Slime Ball")

        font = pygame.font.SysFont('Noto Sans KR', 30)

        button_x = 100
        button_y = 300
        button_width = 350
        button_height = 70

        button_surface = pygame.Surface((button_width, button_height))

        text = font.render("시작하다", True, (0, 0, 0))
        self.text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))

        self.button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

        self.start_button = Button((200, 200, 200), button_x, button_y, button_width, button_height, '시작하다!')
        self.exit_button = Button((200, 200, 200), button_x, button_y + 150, button_width, button_height, '나가다!')

    def handle_event(self, event: pygame.event.EventType) -> bool:
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            return False # 게임이 진행중이 아님

                # Check for the mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
            if self.start_button.isOver(pos=pygame.mouse.get_pos()):
                data.main_data.stage = 1
            elif self.exit_button.isOver(pos=pygame.mouse.get_pos()):
                return False
        return True

    def draw(self, screen: pygame.Surface):
        screen.blit(self.background, (0, 0))
        start_button = self.start_button
        exit_button = self.exit_button
        screen = self.screen
        if start_button.isOver(pos=pygame.mouse.get_pos()):
            start_button.draw(screen, (0, 0, 0))
        else:
            start_button.draw(screen)

        if exit_button.isOver(pos=pygame.mouse.get_pos()):
            exit_button.draw(screen, (0, 0, 0))
        else:
            exit_button.draw(screen)