import pygame
import mImage

pygame.init()

bg = pygame.image.load("dmh2.jpg")
screenWidth = 800
screenHeight = 700
bg = pygame.transform.scale(bg, (screenWidth, screenHeight))
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("DHAMT_essai_1")
clock = pygame.time.Clock()

image_nr_sel = pygame.image.load("p_sel_n.png")
image_bl_sel = pygame.image.load("p_sel_b.png")


class Piece_B:
    def __init__(self, pos, width_height):
        self.wh = pygame.image.load("blanc.png")
        self.p_b = pygame.transform.scale(self.wh, (25, 25))
        self.pos = pos
        self.up = False
        self.step_y = 76
        self.width_height = width_height

    def set_im(self, newimg):
        self.wh = newimg
        self.p_b = pygame.transform.scale(self.wh, (25, 25))

    def imgpr(self):
        self.wh = pygame.image.load("blanc.png")
        self.p_b = pygame.transform.scale(self.wh, (25, 25))

    def set_pos(self, newpos):
        self.pos = newpos

    def draw(self, screen):
        screen.blit(self.p_b, self.pos)

    def npos(self):
        return self.pos


class Piece_N:
    def __init__(self, pos, width_height):
        self.bk = pygame.image.load("noir.png")
        self.p_n = pygame.transform.scale(self.bk, (25, 25))
        self.pos = pos
        self.down = False
        self.step_y = 76
        self.width_height = width_height

    def set_im(self, newimg):
        self.wh = newimg
        self.p_b = pygame.transform.scale(self.wh, (25, 25))

    def imgpr(self):
        self.wh = pygame.image.load("blanc.png")
        self.p_b = pygame.transform.scale(self.wh, (25, 25))

    def set_pos(self, newpos):
        self.pos = newpos

    def draw(self, screen):
        screen.blit(self.p_n, self.pos)

    def npos(self):
        return self.pos


#



position = [(u, v) for v in range(68, 700, 66) for u in range(15, 800, 93)]

# cordonné circulaire des points


# savoir le position de clic

listposition = []
l = []
for i in range(1, 10):
    l = []
    for j in range(9):
        l.append(position[j * i])
    listposition.append(l)
print(listposition)



while True:
    clock.tick(100)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # print('==> Évènement :', event.type)
            # print(dict(event.dict.items())['pos'])

            # print(pos_cl(dict(event.dict.items())['pos']))
            # if pos_cl()
            try:
                if pos_cl(dict(event.dict.items())['pos']) and bb_dsc(dict(event.dict.items())['pos']):
                    position_b[bb_dsc(dict(event.dict.items())['pos'])].set_im(image_bl_sel)
                    k = bb_dsc(dict(event.dict.items())['pos'])

                if pos_cl(dict(event.dict.items())['pos']) and not bb_dsc(dict(event.dict.items())['pos']):
                    position_b[k].set_pos(pos_cl(dict(event.dict.items())['pos']))
                    position_b[k].imgpr()
            except NameError:
                position_b[k].imgpr()
                pass
    redrawGame()
