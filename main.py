import pygame
import data.main_data
from stage import Stage
from screens.main_screen import MainScreen
from screens.stage_screen import StageScreen

pygame.init()

test_map: Stage = Stage.from_stage_file(file='maps/testmap', start_point=(3, 14))
test_map2: Stage = Stage.from_stage_file(file='maps/testmap 2', start_point=(3, 0))
test_map3: Stage = Stage.from_stage_file(file='maps/testmap 3', start_point=(3, 14))

# scenes  = {'Main': MainScreen(),
#            'map01': StageScreen(test_map)
#            }
scenes = [MainScreen(), StageScreen(test_map), StageScreen(test_map2), StageScreen(test_map3), MainScreen()]
scene = scenes[0]

# 충돌이 왜 2번 처리되지? => 그야 충돌 물체가 2개라서
            
if __name__ == '__main__':
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption("Slime Ball")
    running = True

    while running:
        data.main_data.clock.tick(data.main_data.FPS)
        scene = scenes[data.main_data.stage]
        for event in pygame.event.get():
            running = scene.handle_event(event)
        scene.draw(screen)
        scene.update(screen)