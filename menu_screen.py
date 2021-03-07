import pygame as pg
import pygame.font

class Button_title:
    def __init__(self, settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.background_image = pg.image.load('images/menu2.jpg')
        self.alien1 = pg.image.load('images/alien00.png')
        self.alien2 = pg.image.load('images/alien10.png')
        self.alien3 = pg.image.load('images/alien20.png')
        self.alien4 = pg.image.load('images/alien30.png')
        self.point1 = pg.image.load('images/x50ff.png')
        self.point2 = pg.image.load('images/x50ff.png')
        self.point3 = pg.image.load('images/x50ff.png')
        self.point4 = pg.image.load('images/x50ff.png')

        self.width, self.height = 200, 50
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.rect.centerx

    def draw(self):

        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.alien1, (300, 75))
        self.screen.blit(self.alien2, (300, 175))
        self.screen.blit(self.alien3, (300, 275))
        self.screen.blit(self.alien4, (300, 375))
        self.screen.blit(self.point1, (375, 100))
        self.screen.blit(self.point2, (375, 200))
        self.screen.blit(self.point3, (375, 300))
        self.screen.blit(self.point4, (375, 400))

        self.screen.blit(self.msg_image, self.msg_image_rect)
