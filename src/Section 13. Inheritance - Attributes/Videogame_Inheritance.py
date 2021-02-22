class Sprite:

    def __init__(self, x, y, img_file, speed, life_counter):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = speed
        self.life_counter = life_counter


class Enemy(Sprite):

    def __init__(self, x, y, img_file, speed, life_counter=5):
        Sprite.__init__(self, x, y, img_file, speed, life_counter)
        self.message = "I'm here to protect my master"


class Player(Sprite):

    def __init__(self, x, y, img_file, speed=56, life_counter=6):
        Sprite.__init__(self, x, y, img_file, speed, life_counter)
    # This is a fixed option. no customization is possible. Defining value in __init__ method allows customization.
    # self.speed = 56


class DifficultEnemy(Enemy):

    def __init__(self, x, y, img_file):
        Enemy.__init__(self, x, y, img_file, 80)
        # thats an example


class EasyEnemy(Enemy):

    def __init__(self, x, y, img_file):
        Enemy.__init__(self, x, y, img_file, 40, 1)
        self.speed = 40
        self.life_counter = 1


var1 = Sprite(x=1, y=1, img_file="heh.png", speed=86, life_counter=3)
var2 = Enemy(x=1, y=1, img_file="heh.png", speed=79)
var3 = Player(x=1, y=1, img_file="heh.png")
var4 = DifficultEnemy(x=1, y=1, img_file="heh.png")
var5 = EasyEnemy(1, 1, "kfl")
print(var5.message)
