from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, picture_image, picture_x, picture_y, picture_width, picture_height, picture_speed):
        super().__init__()

        self.image = transform.scale(image.load(picture_image), (picture_width, picture_height))
        self.speed = picture_speed

        self.rect = self.image.get_rect()
        self.rect.x = picture_x
        self.rect.y = picture_y
    def reset(self,window):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_rocket1(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
    def update_rocket2(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
        