import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
FPS = 60

background = pygame.image.load('resources/mainscreen.png')
pygame.display.set_caption("Slime Ball")

font = pygame.font.SysFont('Noto Sans KR', 30)

class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
            
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('Unifont', 40)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

button_x = 100
button_y = 300
button_width = 350
button_height = 70

button_surface = pygame.Surface((button_width, button_height))

text = font.render("시작하다", True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))

button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

running = True

start_button = Button((200, 200, 200), button_x, button_y, button_width, button_height, '시작하다!')
exit_button = Button((200, 200, 200), button_x, button_y + 150, button_width, button_height, '나가다!')

while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

                # Check for the mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
            if start_button.isOver(pos=pygame.mouse.get_pos()):
                print("Button clicked!")
            elif exit_button.isOver(pos=pygame.mouse.get_pos()):
                running = False

    screen.blit(background, (0, 0))

    if start_button.isOver(pos=pygame.mouse.get_pos()):
        start_button.draw(screen, (0, 0, 0))
    else:
        start_button.draw(screen)

    if exit_button.isOver(pos=pygame.mouse.get_pos()):
        exit_button.draw(screen, (0, 0, 0))
    else:
        exit_button.draw(screen)
    
    pygame.display.update()