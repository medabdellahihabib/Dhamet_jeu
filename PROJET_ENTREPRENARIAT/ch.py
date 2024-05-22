import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
RUNNING = True

TOTAL_CASES = 64  # (8x8) = 64
TOTAL_POINTS = 81  # (9x9) = 81

COULEUR_PIECES = ['rouge', 'noir']
DICO_PIECES = {
    'pion': [8, 9, 10, 11, 12, 13, 14, 15,
             48, 49, 50, 51, 52, 53, 54, 55],
    'tour': [0, 7, 56, 63],
    'cavalier': [1, 6, 57, 62],
    'fou': [2, 5, 58, 61],
    'roi': [3, 60],
    'reine': [4, 59],
}

## Initialiser pygame.
pygame.init()

fenetre = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jeu Echec')


def load_image(filename, convert_alpha=False):
    """ Une fonction, pour chager les images,
        évite la répétition (si possible).
    """
    image = pygame.image.load(filename)
    if not convert_alpha:
        return image.convert()
    else:
        return image.convert_alpha()


###############################################################
## CHOIX 1: (Image..) #########################################
###############################################################
damier = load_image('k__.png')
damier = pygame.transform.scale(damier, (SCREEN_WIDTH, SCREEN_HEIGHT))
fenetre.blit(damier, (0, 0))


def detect_all_case_in_picture(screen, wh):
    """
        Trouvez les points de chaque rectangle(carré), dans l'image
        En sachant qu'il y a (8x8)64 cases, donc (9x9)81 points,
        on trouve le nombre de pixels pour chaque carré.
    """

    def draw_one_circle(screen, x, y, color=(255, 0, 0), radius=3, thickness=3):
        return pygame.draw.circle(screen, color, (x, y), radius, thickness)

    racine = int(TOTAL_POINTS ** (0.5))  ## Racine Carré (81**(0.5) = 9)

    ## Si vous voulez une liste en 2-Dimensions à la place d'un dico
    lst_2D = [[None for j in range(racine)] for i in range(racine)]
    dico = {}

    COUNT = 0
    X, Y = 0, 0
    for i in range(len(lst_2D)):
        for j in range(len(lst_2D[i])):
            draw_one_circle(screen, X, Y)  ## À Supprimer

            dico[COUNT] = [X, Y, X + wh, Y + wh]

            ## Si vous voulez une liste 2-Dimensions
            # lst_2D[i][j] = [X, Y, X+wh, Y+wh]

            COUNT += 1
            X += wh

            if X >= SCREEN_WIDTH:
                Y += wh
                X = 0
    return dico


VARIABLE_A_CHANGER = 88
dico_rect = detect_all_case_in_picture(fenetre, VARIABLE_A_CHANGER)
groupes = pygame.sprite.Group()  # Juste pour pas avoir d'erreur dans la boucle


###############################################################
## CHOIX 2: (Rectangles, uniquement) ##########################
###############################################################
def creer_echiquier(screen, wh):
    dico = {}
    X, Y = 0, 0
    colors = [(255, 255, 255), (0, 0, 0)]
    for i in range(64):
        ## S'il est divisible par 8, on change le sens des couleurs.
        if i % 8 == 0 and i != 0:
            colors = [colors[1], colors[0]]
        ## S'il est divisible par 2, on change de couleur.
        if i % 2 == 0:
            color = colors[0]
        else:
            color = colors[1]

        ## On sauvegarde chaque rectangle créé, dans le dico
        dico[i] = pygame.draw.rect(
            screen, color, (X, Y, X + wh, Y + wh))

        X += wh
        if X >= SCREEN_WIDTH:
            Y += wh
            X = 0
    return dico


VARIABLE_A_CHANGER = 88
dico_rect = creer_echiquier(fenetre, VARIABLE_A_CHANGER)
groupes = pygame.sprite.Group()  # Pour la boucle, pas d'erreur..


###############################################################
## CHOIX 3: (Sprites Case) ####################################
###############################################################
class Case(pygame.sprite.Sprite):
    def __init__(self, pos, color=None):
        super().__init__()

        self.image = pygame.Surface([VARIABLE_A_CHANGER, VARIABLE_A_CHANGER])
        if color is not None:
            self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.piece = None

    def draw_image(self, image, size=(50, 50)):
        try:
            self.piece = load_image(image, True)
            self.piece = pygame.transform.scale(self.piece, size)
        except:
            pass

    def update(self):
        if self.piece is not None:
            fenetre.blit(self.piece, self.rect)


def creer_echiquier_sprite(screen, wh):
    dico = {}
    group = pygame.sprite.Group()

    colors = [(255, 255, 255), (0, 0, 0)]
    X, Y = 0, 0
    for i in range(64):
        ## S'il est divisible par 8, on change le sens des couleurs.
        if i % 8 == 0 and i != 0:
            colors = [colors[1], colors[0]]
        ## S'il est divisible par 2, on change de couleur.
        if i % 2 == 0:
            color = colors[0]
        else:
            color = colors[1]

        ## Une classe (Sprite)
        case = Case([X, Y], color)

        for piece, all_list in DICO_PIECES.items():
            len_list = len(all_list)
            if i in all_list:
                for nb, j in enumerate(all_list):
                    ## Trouvez la bonne couleur
                    if nb <= len_list / 2:
                        c = ' ' + COULEUR_PIECES[0]
                    else:
                        c = ' ' + COULEUR_PIECES[1]

                filename = piece + c + '.png'
                # print(filename) ## SI TROUVE PAS D'IMAGE, À REGARDEZ
                case.draw_image(filename)

        ## On sauvegarde chaque rectangle créé, dans le dico
        dico[i] = case.rect
        ## On sauvegarde dans le group de sprites.
        group.add(case)

        X += wh
        if X >= SCREEN_WIDTH:
            Y += wh
            X = 0
    return dico, group


VARIABLE_A_CHANGER = 88
dico_rect, groupes = creer_echiquier_sprite(fenetre, VARIABLE_A_CHANGER)


#################################################################
## NE PAS TOUCHEZ, MAIS À COMPRENDRE ############################
#################################################################


## GESTION COLLISION (SOURIS + Rectangle)
def my_collidepoint(point, width_height):
    px, py = point  # Le point

    ## On énumère le dictionnaire, pour trouver le bon rectangle
    for rect, value in dico_rect.items():
        vx, vy, vx2, vy2 = value
        ## On trouve le range de l'axe X et Y
        rangeX = range(vx, vx + width_height)
        rangeY = range(vy, vy + width_height)
        ## Si les deux (px, py) sont dans le range, c'est le bon rectangle
        if px in rangeX:
            if py in rangeY:
                return rect
    return None


## EVENT PRINCIPALE
def main_event():
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    ## GESTION SOURIS
    pressed = pygame.mouse.get_pressed()
    if pressed[0] == 1:
        position = pygame.mouse.get_pos()
        the_rect = my_collidepoint(position, VARIABLE_A_CHANGER)
        print('gauche', position, 'carrer #:', the_rect)

    if pressed[1] == 1:
        print('middle', position)
    if pressed[2] == 1:
        print('droit', position)


## BOUCLE PRINCIPALE:
while RUNNING:
    main_event()

    groupes.draw(fenetre)
    groupes.update()

    pygame.display.flip()

pygame.quit()