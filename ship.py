import pygame

class Ship():
    def __init__(self, screen, ai_setting):
        self.screen = screen
        self.moving_right = False
        self.moving_left = False
        self.setting = ai_setting

        #Note that using other bmp it will not work for some
        self.image = pygame.image.load_basic("Spaceship.bmp")


        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()


        #Sets the size of the image
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.screen_rect.centerx)
        self.rect.centerx = self.center

    def blitme(self):
        #Shows the image of ship and other images of ship
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center +=self.setting.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.center -=self.setting.ship_speed

        self.rect.centerx = self.center

    def center_ship(self):
        self.centerx = self.screen_rect.centerx
