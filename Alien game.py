import pygame
from setting import Setting
from pygame.sprite import Group
from ship import Ship
from alien import Alien
from game_stats import GameStats
from game_function import *
from button import Button
from scoreboard import Scoreboard
#Use the * Because it doesn't read game_fuctions as gf instead it uses the normal variable
def run_game():
    pygame.init()
    ai_setting =  Setting()
    screen = pygame.display.set_mode([ai_setting.width,ai_setting.height])


    ship = Ship(screen, ai_setting)
    pygame.display.set_caption("Alien Invaders")

    # Play the game
    play_button = Button(ai_setting, screen, "Start: 1 Player")


    #Overall Stats before and after game
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats, ai_setting.ship_limit)

    #Shoots bullets
    bullets = Group()
    aliens = Group()
    create_fleet(ai_setting, screen, aliens, ship)

    while True:
        check_event(ai_setting, screen, stats, play_button, sb, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            update_bullet(ai_setting, screen, stats, sb, ship, bullets, aliens)
            update_alien(ai_setting, stats, screen, ship, aliens, bullets,sb)
        update_screen(screen,ai_setting, sb, ship, stats, bullets, aliens, play_button)
#Note that the lives will not count to 3 to 1 and reset to 3 instead i use the print way
run_game()
