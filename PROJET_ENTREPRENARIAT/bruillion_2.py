import pygame

from pieces import Piece
from view import WhiteP


def cidscercle(x, y, r, x0=0, y0=0):
    if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:
        return True
    return False


print(cidscercle(52, 2, 8))


def draw_one_circle(screen, x, y, color=(255, 0, 0), radius=3, thickness=3):
    return pygame.draw.circle(screen, color, (x, y), radius, thickness)


# class white_move:
#     global position,keys
#     def __init__(self,white_piece,pos):
#         self.pos = pos
#         self.white_piece = white_piece
#         self.step_y = 76
#         position[white_piece] =pos
#     def move(self):
#         if keys[pygame.K_DOWN] and self.pos[1] > 12 and self.pos not in position.keys:
#             self.pos[1] += self.step_y


# step_x, step_y = 94, 76à
# x, y = 12, 35
#
#
position = [(u, v) for v in range(68, 700, 66) for u in range(15, 800, 93)]
#
# l = []
# for i in range(40):
#     l.append("pb_" + str(i))
#
# for i in range(40):
#     print(l[i])

l = [5, 4, 9, 12]
for i in range(len(l) - 1, -1, -1):
    print(l[i])
k = 0
l = []
for i in range(9):
    l.append(position[k:k + 9])
    k += 9
for i in l:
    if i == l[3]:
        pass
    else:
        print(i)

try:
    for i in range(500):
        print(i)
        print(l[i])
except IndexError:
    pass

position_b = []
position_n = []
for i in range(40):
    position_n.append(Piece(position[i + 41], "black"))
    position_b.append(Piece(position[i], "white"))
on_init = [position_b, position_n]
for i in on_init[0]:
    print(i.getpos())

on_init[0][0].setpos()
print("\n\n")
for i in on_init[0]:
    print(i.getpos())

position = [(u, v) for v in range(68, 700, 66) for u in range(15, 800, 93)]


def inPos(pos, pos_piece, r=13):
    if (pos_piece[0] - pos[0] + 12.5) ** 2 + (pos_piece[1] - pos[1] + 12.5) ** 2 <= 2 * r ** 2:
        return True
    return False


def pos_cl(pos):
    k = 400
    for i in range(81):
        if inPos(pos, position[i]):
            k = i
    if k == 400:
        pass
    else:
        return position[k]


def bn_dsc(pos):
    if pos_cl(pos):
        for u in on_init[1]:
            if u.getpos() == pos_cl(pos):
                return u


k, t = 0, 0
l = []
for i in position:
    if bn_dsc(i):
        l.append((bn_dsc(i)))
        bn_dsc(i).setpos()
        k += 1
    else:
        t += 1
print(len(position), k, t)
print("\n\n")
for i in on_init[0]:
    print(i.getpos())
print("\n\n")
for i in l:
    print(i.getpos())

k = on_init[0][1]
k.setpos()
print("\n\n")
for i in on_init[0]:
    print(i.getpos())


def Multiplication(x, y=8):
    x = y+5
    return x


a = 5
b = 6
if Multiplication(a, b):
    Multiplication(a, b)
    print(a, b)
print(a, b)

print(WhiteP(None))

# Imports
from pygame.locals import *

# Main init
pygame.init()

# Basic vars
run = True
s_width = 100
s_height = 600


# Making display screen. Don't forget the last tag!
screen = pygame.display.set_mode((s_width, s_height), RESIZABLE)

# Main loop
while run:
    # event detection
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        # The part which matters for our purposes
        if event.type == WINDOWRESIZED:
            s_width, s_height = screen.get_width(), screen.get_height()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
    # Test line to see if the window resizing works properly
    pygame.draw.line(screen, (255, 255, 255), (int(0.3*s_width), int(0.25*s_height)), (int(0.8*s_width), int(0.25*s_height)))
    # Final flip
    pygame.display.flip()

# Quit
pygame.quit()