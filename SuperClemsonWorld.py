import pygame, time, sys
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.frame = 0
        self.images = []
        player = pygame.image.load('tig.png')
        player = pygame.transform.scale(player, (63, 100))
        self.images.append(player)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.isjumping = False
        self.jumpoffset = 0
        self.count = 0
        self.lives = 48
        self.lvlcomplete = False
        self.level = 0
        self.x = 0
    def control(self, x):
        self.movex += x
    def update(self):
        self.rect.x += self.movex
        self.rect.y -= self.jumpoffset
    def collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.lives -= 1

class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        enemy = pygame.image.load('os.png')
        enemy = pygame.transform.scale(enemy, (90, 100))
        self.images = []
        self.images.append(enemy)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.enemycount = 0
    def move(self):
        self.rect.x -= ENEMYMOVEDIST
    def enemyCount(self):
        self.enemycount += 1

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        enemy = pygame.image.load('lv.png')
        enemy = pygame.transform.scale(enemy, (91, 100))
        enemy = pygame.transform.flip(enemy, True, False)
        self.images = []
        self.images.append(enemy)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.enemycount = 0
    def move(self):
        self.rect.x -= ENEMYMOVEDIST
    def enemyCount(self):
        self.enemycount += 1

class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        enemy = pygame.image.load('fsu.png')
        enemy = pygame.transform.scale(enemy, (98, 100))
        enemy = pygame.transform.flip(enemy, True, False)
        self.images = []
        self.images.append(enemy)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.enemycount = 0
    def move(self):
        self.rect.x -= ENEMYMOVEDIST
    def enemyCount(self):
        self.enemycount += 1

class Enemy4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        enemy = pygame.image.load('gc.png')
        enemy = pygame.transform.scale(enemy, (100, 100))
        enemy = pygame.transform.flip(enemy, True, False)
        self.images = []
        self.images.append(enemy)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.enemycount = 0
    def move(self):
        self.rect.x -= ENEMYMOVEDIST
    def enemyCount(self):
        self.enemycount += 1

class Enemy5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        enemy = pygame.image.load('saban.png')
        enemy = pygame.transform.scale(enemy, (90, 100))
        self.images = []
        self.images.append(enemy)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.enemycount = 0
    def move(self):
        self.rect.x -= ENEMYMOVEDIST
    def enemyCount(self):
        self.enemycount += 1

def keys(player):
    keys = pygame.key.get_pressed()
    if keys[K_UP] and player.isjumping == False and player.jumpoffset == 0:
		player.isjumping = True

def jump(player):
    if player.isjumping:
        player.jumpoffset = 23
        player.count += 1
        if player.count >= JUMPDIST:
            player.isjumping = False
    elif player.count > 0 and player.isjumping == False:
        player.jumpoffset = -23
        player.count -= 1
    elif player.count == 0:
        player.jumpoffset = 0

def textObjs(words, font):
    textSurf = font.render(words, False, ORANGE)
    return textSurf, textSurf.get_rect()

def textObjsPurp(words, font):
    textSurf = font.render(words, False, PURPLE)
    return textSurf, textSurf.get_rect()

def displayMessage(text):
    largeText = pygame.font.Font('font.ttf', 75)
    Textsurf, Textrect = textObjs(text, largeText)
    Textrect.center = (halfWide), (halfHigh)
    DISPLAYSURF.blit(Textsurf, Textrect)
    pygame.display.flip()

def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        DISPLAYSURF.fill(PURPLE)
        daboText = pygame.font.Font('font.ttf', 135)
        dabosurf, daborect = textObjs('MAKE DABO PROUD!', daboText)
        daborect.center = (halfWide), (halfHigh-160)
        DISPLAYSURF.blit(dabosurf, daborect)
        largeText = pygame.font.Font('font.ttf', 75)
        Textsurf, Textrect = textObjs('Super Clemson World!', largeText)
        Textrect.center = (halfWide), (halfHigh-80)
        DISPLAYSURF.blit(Textsurf, Textrect)
        startText = pygame.font.Font('font.ttf', 75)
        startsurf, startrect = textObjs('press   s   to start!', startText)
        startrect.center = (halfWide), (halfHigh)
        DISPLAYSURF.blit(startsurf, startrect)
        endText = pygame.font.Font('font.ttf', 75)
        endsurf, endrect = textObjs('press   q   to exit!', endText)
        endrect.center = (halfWide), (halfHigh+80)
        DISPLAYSURF.blit(endsurf, endrect)
        instructText = pygame.font.Font('font.ttf', 25)
        instructsurf, instructrect = textObjs('dodge the mascots as they come at you to make Dabo proud', instructText)
        instructrect.center = (halfWide), (halfHigh+130)
        DISPLAYSURF.blit(instructsurf, instructrect)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                game()
        pygame.display.update()

def win():
    dabo = pygame.image.load('dabo.png').convert()
    dabo = pygame.transform.scale(dabo, (960, 823))
    daboText = pygame.font.Font('font.ttf', 75)
    dabosurf, daborect = textObjsPurp('You are a winner!', daboText)
    daborect.center = (halfWide+205), (halfHigh-160)
    DISPLAYSURF.blit(dabo, (0, 0))
    DISPLAYSURF.blit(dabosurf, daborect)
    pygame.display.flip()
def gameOver():
    time.sleep(2)


WORLDX = 960
WORLDY = 720
halfWide = WORLDX/2
halfHigh = WORLDY/2
ANI = 4
FPS = 30
MOVEDIST = 10
ENEMYMOVEDIST = 15
JUMPDIST = 8
BGCOLOR = (0, 255, 0)
WHITE = (255,255,255)
BLACK = (0, 0, 0)
ORANGE = (246, 103, 51)
PURPLE = (82, 45, 128)
mess = 0

CLOCK = pygame.time.Clock()
pygame.init()

fontObj = pygame.font.Font('font.ttf', 32)
cox = 0

pygame.mixer.music.load('bossFight0.mp3')
pygame.mixer.music.play(-1, 0.0)

pygame.display.set_caption('Super Clemson World')
DISPLAYSURF = pygame.display.set_mode((WORLDX, WORLDY))
BACKGROUND = pygame.image.load('bg.png').convert()
BACKGROUND = pygame.transform.scale(BACKGROUND, (6000, 1000))
GROUND = pygame.image.load('brick.png').convert()
GROUND = pygame.transform.scale(GROUND, (50, 50))
HEART = pygame.image.load('life.png')
HEART = pygame.transform.scale(HEART, (20, 20))
GAMEICON = pygame.image.load('icon.png')
pygame.display.set_icon(GAMEICON)
def game():
    player = Player()
    player.rect.x = 0
    player.rect.y = 420
    playerList = pygame.sprite.Group()
    playerList.add(player)
    enemy1 = Enemy1()
    enemy1.rect.x = WORLDX + 50
    enemy1.rect.y = 418
    enemy1List = pygame.sprite.Group()
    enemy1List.add(enemy1)
    enemy2 = Enemy2()
    enemy2.rect.x = (WORLDX + 50)
    enemy2.rect.y = 418
    enemy2List = pygame.sprite.Group()
    enemy2List.add(enemy2)
    enemy3 = Enemy3()
    enemy3.rect.x = (WORLDX + 50)
    enemy3.rect.y = 418
    enemy3List = pygame.sprite.Group()
    enemy3List.add(enemy3)
    enemy4 = Enemy4()
    enemy4.rect.x = (WORLDX + 50)
    enemy4.rect.y = 418
    enemy4List = pygame.sprite.Group()
    enemy4List.add(enemy4)
    enemy5 = Enemy5()
    enemy5.rect.x = (WORLDX + 50)
    enemy5.rect.y = 418
    enemy5List = pygame.sprite.Group()
    enemy5List.add(enemy5)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.control(-MOVEDIST)
                if event.key == pygame.K_RIGHT:
                    player.control(MOVEDIST)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.control(MOVEDIST)
                if event.key == pygame.K_RIGHT:
                    player.control(-MOVEDIST)
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()

        player.x = player.rect.x % BACKGROUND.get_rect().width
        player.x = player.x * -.35
        DISPLAYSURF.blit(BACKGROUND, (player.x - (1210*player.level), 0))
        for i in range(0, 20):
            for j in range(0, 4):
                DISPLAYSURF.blit(GROUND, ((50*i)-5, (50*j)+518))
        keys(player)
        jump(player)
        player.update()
        playerList.draw(DISPLAYSURF)
        if player.level == 0:
            enemy1List.draw(DISPLAYSURF)
            enemy1.move()
        if enemy1.rect.x <= -100:
            enemy1.rect.x = WORLDX + 50
            enemy1.rect.y = 418
            enemy1.enemyCount()
        if enemy1.enemycount >= 5:
            player.lvlcomplete = True
            player.level += 1
            enemy1.enemycount = 0
        if player.level == 1:
            enemy2List.draw(DISPLAYSURF)
            enemy2.move()
        if enemy2.rect.x <= -100:
            enemy2.rect.x = WORLDX + 50
            enemy2.rect.y = 418
            enemy2.enemyCount()
        if enemy2.enemycount >= 5:
            player.lvlcomplete = True
            player.level += 1
            enemy2.enemycount = 0
        if player.level == 2:
            enemy3List.draw(DISPLAYSURF)
            enemy3.move()
        if enemy3.rect.x <= -100:
            enemy3.rect.x = WORLDX + 50
            enemy3.rect.y = 418
            enemy3.enemyCount()
        if enemy3.enemycount >= 5:
            player.lvlcomplete = True
            player.level += 1
            enemy3.enemycount = 0
        if player.level == 3:
            enemy4List.draw(DISPLAYSURF)
            enemy4.move()
        if enemy4.rect.x <= -100:
            enemy4.rect.x = WORLDX + 50
            enemy4.rect.y = 418
            enemy4.enemyCount()
        if enemy4.enemycount >= 5:
            player.lvlcomplete = True
            player.level += 1
            enemy4.enemycount = 0
        if player.level == 4:
            enemy5List.draw(DISPLAYSURF)
            enemy5.move()
        if enemy5.rect.x <= -100:
            enemy5.rect.x = WORLDX + 50
            enemy5.rect.y = 418
            enemy5.enemyCount()
        if enemy5.enemycount >= 5:
            win()
        for i in range (0, player.lives - 1):
            DISPLAYSURF.blit(HEART, (i*20, 0))
        if player.lives <= 0:
            DISPLAYSURF.fill(PURPLE)
            gameOver()
            displayMessage('you didnt make Dabo proud :(')
        player.collide(enemy1List)
        player.collide(enemy2List)
        player.collide(enemy3List)
        player.collide(enemy4List)
        pygame.display.flip()
        CLOCK.tick(FPS)
gameIntro()
game()
