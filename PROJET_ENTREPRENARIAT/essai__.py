import pygame
import pygame.draw

def main() :
    pygame.init()
    xx, yy = 200, 200
    size = [xx, yy]
    screen = pygame.display.set_mode(size)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                print('==> Evenement :', event.type)
                for k, v in event.dict.items():
                    print(k, v)
                print()

    pygame.quit()

if __name__ == '__main__' :
    main()