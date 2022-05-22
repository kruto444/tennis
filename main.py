from pygame import *
clock = time.Clock()
FPS = 60
h_win = 500 #высота экрана
w_win = 700 #ширина экрана

class Wall(sprite.Sprite):
    def __init__(self,name,c_1,c_2,c_3,wall_x,wall_y,wall_w,wall_h):
        self.name = name
        self.c_1 = c_1
        self.c_2 = c_2
        self.c_3 = c_3
        self.w = wall_w
        self.h = wall_h
        self.image = Surface((self.w,self.h))
        self.image.fill((self.c_1,self.c_2,self.c_3))
        self.rect = self.image.get_rect()
        self.rect.y = wall_y
        self.rect.x = wall_x
    def paint(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class GameSprite(sprite.Sprite):
    def __init__(self,name,speed,h,w,y,x,images):
        super().__init__()
        self.name = name
        self.speed = speed
        self.images = transform.scale(image.load(images),(w,h))
        self.rect = self.images.get_rect()
        self.rect.y = y
        self.rect.x = x
    def reset(self):
        window.blit(self.images,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < w_win - 105:
            self.rect.x += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < w_win - 105:
            self.rect.x += self.speed

class Ball(GameSprite):
    direction = "left" #направление 
    def update(self): # Функция перемещения 
        if self.rect.x <= 200 : #граница
            self.direction = "right"
        if self.rect.x >= 400:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
font.init()
#создаем фоновую музыку
bgrd_color = (255,255,255)
'''
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()



win_sound = mixer.Sound('money.ogg')
kick_soind = mixer.Sound('kick.ogg')
'''
speed_ball = 5
#создай окно игры
window = display.set_mode((w_win,h_win))
img_tocket = 'images/sprite/rakerka.png'
image_ball = 'images/sprite/ball.png'
rocket1 = Player('ракетка 1',10,100,100,0,300,img_tocket)
rocket2 = Player('ракетка 2',10,100,100,400,300,img_tocket)
ball = Ball('мяч',speed_ball,50,50,225,325,image_ball)
#задай фон сцены
'''
b_im = image.load('background.jpg')
bdgr = transform.scale(b_im,(w_win,h_win))
#создай 2 спрайта и размести их на сцене
w1 = Wall('w1',255, 202, 138,50,100,20,400)


font = font.Font(None,70)
win_text = font.render('mission complete',True,(0,255,0))
fail_text = font.render('mission failed',True,(255,0,0))



player = Player('player',10,100,100,250,300,'hero.png')
monster = Enemy('nps',10,100,100,100,20,'cyborg.png')
gold = GameSprite('gold',10,100,100,10,330,'treasure.png')
#игровой цыкл
#игровой цыкл
'''
game = True
finish = False
while game:
    
    
    #обработай событие «клик по кнопке "Закрыть окно"»
    for e in event.get():#перебор событий
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(bgrd_color)
        rocket1.update1()
        rocket1.reset()
        rocket2.update2()
        rocket2.reset() 
        ball.update()
        ball.reset()
    display.update()
    clock.tick(FPS)
