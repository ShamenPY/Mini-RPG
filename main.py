import pygame

width,height = 1920,1160

map_img = pygame.image.load("images\\background\\middle_map.png")
youimg = pygame.image.load("images\\characters\\you.png")
you = pygame.transform.scale(youimg,(100,100))
enemyimg = pygame.image.load("images\\characters\\enemy.png")
enemy = pygame.transform.scale(enemyimg,(100,100))
map = pygame.transform.scale(map_img,(width,height))

screen = pygame.display.set_mode((width,height), pygame.FULLSCREEN | pygame.SCALED)

position_of_mouse = pygame.mouse.get_pos()
class App():
    def __init__(self):
        self.running = True
        self.yourposX = 500
        self.yourposY = 500
        self.enemyposX = 300
        self.enemyposY = 300
        self.main()

    def events_handling(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    return
                if event.key == pygame.K_LEFT:
                    self.yourposX -= 30
                if event.key == pygame.K_RIGHT:
                    self.yourposX += 30
                if event.key == pygame.K_UP:
                    self.yourposY -= 30
                if event.key == pygame.K_DOWN:
                    self.yourposY += 30

        self.rectenemyX = self.enemyposX + 50
        self.rectenemyY = self.enemyposY + 50
        self.rectyouX = self.yourposX + 50
        self.rectyouY = self.yourposY + 50
        self.rectofyou = you.get_rect(center=(self.rectyouX, self.rectyouY))
        self.rectofenemy = enemy.get_rect(center=(self.rectenemyX, self.rectenemyY))
        self.collide = pygame.Rect.colliderect(self.rectofyou, self.rectofenemy)

        if self.collide:
            print("jest kolizja :) ")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    def draw_screen(self):
        screen.blit(map, (0, 0))
        screen.blit(you, (self.yourposX, self.yourposY))
        screen.blit(enemy, (self.enemyposX, self.enemyposY))


    def main(self):
        while self.running:
            self.draw_screen()
            self.events_handling()

            pygame.display.flip()


class Enemy():
    def __init__(self):
        self.main()
    def main(self):
        pass

class You():
    def __init__(self):
        self.main()
    def main(self):
        pass

App = App()

Enemy = Enemy()

