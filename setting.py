class Setting():
    def __init__(self):
        #Screen Settings
        self.width = 1200
        self.height = 800
        self.color = (150,150,150)

        #Ship Settings
        self.ship_limit = 3

        #Bullet Settings
        self.bullet_width = 4
        self.bullet_height = 10
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3000

        #Alien Settings
        self.drop_speed = 10

        #Game Speed Up
        self.speedup_scale = 2

        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #Set up before game starts
        self.ship_speed = 3
        self.bullet_speed = 5
        self.alien_speed = 2
        self.fleet_direction = 2
        self.alien_points = 100

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)
        # print(self.alien_points)

