import pygame

width, height = 1920, 1160

map_img = pygame.image.load("images\\background\\middle_map.png")
youimg = pygame.image.load("images\\characters\\you.png")
ask = pygame.image.load("images\\ask.png")
attackyes = pygame.image.load("images\\attack.png")
attacktrade = pygame.image.load("images\\trade.png")
askimg = pygame.transform.scale(ask,(651, 320))
you = pygame.transform.scale(youimg, (100, 100))
enemyimg = pygame.image.load("images\\characters\\enemy.png")
enemy = pygame.transform.scale(enemyimg, (100, 100))

map = pygame.transform.scale(map_img, (width, height))

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN | pygame.SCALED)

position_of_mouse = pygame.mouse.get_pos()


class App():
    def __init__(self):
        self.running = True
        self.movement = [0, 0]
        self.speed = 6

        self.yourposX = 500  # VALUE OF X AND Y YOU
        self.yourposY = 500
        self.enemyposX = 300  # VALUE OF X AND Y ENEMY
        self.enemyposY = 300
        self.attackcollider = 0
        self.main()

#108, 34


    def attackimagecollision(self):

        """
        This  function  is  creating  collide of position  of
        mouse  and  image of attack  or  trade  when  you  moving  on a mob.
        """

        for event in pygame.event.get():
            position_of_mouse = pygame.mouse.get_pos()
            self.rectofattack = attackyes.get_rect(center=(500 + 108, 570 + 34))
            self.rectoftrade = attacktrade.get_rect(center=(785 + 110, 570 + 34))
            mouse_position_in_mask = position_of_mouse[0] - self.rectofattack.x, position_of_mouse[1] - self.rectofattack.y
            if self.rectofattack.collidepoint(position_of_mouse) == 1:
                if_touching = 1
            else:
                if_touching = 0
            if event.type == pygame.MOUSEBUTTONDOWN and if_touching:
                print('clicked on image')


    def collide(self):
        screen.blit(askimg,(440,400))
        screen.blit(attacktrade,(785,570))
        screen.blit(attackyes,(500,570))
        self.attackcollider = 1

    def events_handling(self):
        while self.attackcollider != 0:
            self.attackimagecollision()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    return
                if event.key == pygame.K_LEFT:
                    self.movement[0] -= 1
                if event.key == pygame.K_RIGHT:
                    self.movement[0] += 1
                if event.key == pygame.K_UP:
                    self.movement[1] -= 1
                if event.key == pygame.K_DOWN:
                    self.movement[1] += 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.movement[0] += 1
                if event.key == pygame.K_RIGHT:
                    self.movement[0] -= 1
                if event.key == pygame.K_UP:
                    self.movement[1] += 1
                if event.key == pygame.K_DOWN:
                    self.movement[1] -= 1









        self.yourposX += self.movement[0] * self.speed
        self.yourposY += self.movement[1] * self.speed

        self.rectenemyX = self.enemyposX + 50
        self.rectenemyY = self.enemyposY + 50
        self.rectyouX = self.yourposX + 50
        self.rectyouY = self.yourposY + 50
        self.rectofyou = you.get_rect(center=(self.rectyouX, self.rectyouY))
        self.rectofenemy = enemy.get_rect(center=(self.rectenemyX, self.rectenemyY))
        self.collid = pygame.Rect.colliderect(self.rectofyou, self.rectofenemy)


        if self.collid:
            self.collide()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = Fals

    def draw_screen(self):
        screen.blit(map, (0, 0))
        screen.blit(you, (self.yourposX, self.yourposY))
        screen.blit(enemy, (self.enemyposX, self.enemyposY))


    def main(self):
        while self.running:

            self.draw_screen()

            self.events_handling()


            pygame.display.flip()


App = App()