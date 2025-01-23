import pygame
from abc import *

class Screen():

    @abstractmethod
    def handle_event(self, event: pygame.event.EventType):
        pass

    @abstractmethod
    def update(self, screen: pygame.Surface):
        pass
     
    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass

    def update(self, screen: pygame.Surface):
        pygame.display.update()