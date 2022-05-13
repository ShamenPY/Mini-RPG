import pygame

width,height = 1920,1160

map_img = pygame.image.load("images\\background\\middle_map.png")
you = pygame.image.load("images\\characters\\you.png")
enemy = pygame.image.load("images\\characters\\enemy.png")
map = pygame.transform.scale(map_img,(1920,1160))
x = pygame.mask.from_surface(you)
screen = pygame.display.set_mode((width,height))
y = pygame.mask.from_surface(enemy)

position_of_mouse = pygame.mouse.get_pos()
class App():
    def __init__(self):

        self.posX = 500
        self.posY = 500
        self.enemyX = 300
        self.enemyY = 300

        self.main()

    def events_handling(self):
        ev = pygame.event.get()
        for event in ev:
            self.position_of_mouse = pygame.mouse.get_pos()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.posX -= 4
                if event.key == pygame.K_RIGHT:
                    self.posX += 4
                if event.key == pygame.K_UP:
                    self.posY -= 4
                if event.key == pygame.K_DOWN:
                    self.posY += 4



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    def main(self):
        running = True
        while True:

            screen.blit(map,(0,0))
            screen.blit(you,(self.posX,self.posY))
            screen.blit(enemy,(self.enemyX,self.enemyY))
            self.events_handling()
            print(self.posX, self.posY)
            print(self.position_of_mouse)
            pygame.display.flip()

App = App()
