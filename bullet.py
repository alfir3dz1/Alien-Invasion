import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_setting, ship, screen):
        super(Bullet, self).__init__()
        self.screen = screen

        #initialize the bullet
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top

        self.y = float(self.rect.y)
        self.color = ai_setting.bullet_color
        self.speed = ai_setting.bullet_speed

    def update(self):
        #moving the bullet forward
        self.y -= self.speed
        #changing the bullet's position
        self.rect.y = self.y
        # print(self.rect.y)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

