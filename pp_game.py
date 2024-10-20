from pygame import *


class GameSprite(sprite.Sprite):
    """базовый класс для создания спрайтов"""

    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
    def move_left(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed

    def move_right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed


win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Лабиринт')
back = 'aquamarine'
window.fill(back)

racket1 = Player('racket.png', 30, 200, 4, 70, 150)
racket2 = Player('racket.png', 520, 200, 4, 70, 150)
ball = Player('tenis_ball.png', 200, 200, 4, 50, 50)

game = True
finish = False
clock = time.Clock()
FPS = 60
speed_X = 3
speed_Y = 3


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)

        racket1.move_right()
        racket2.move_left()

        ball.rect.x += speed_X
        ball.rect.y += speed_Y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_X *= -1
            speed_Y *= -1

        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)
