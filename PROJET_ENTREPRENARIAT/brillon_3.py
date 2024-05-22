from movement import *
from view import P_inPos

position = [(u, v) for v in range(68, 700, 66) for u in range(15, 800, 93)]
listposition = []
k = 0
for i in range(9):
    listposition.append(position[k:k + 9])
    k += 9

lignes = listposition + [[row[j] for row in listposition] for j in range(len(listposition))]
print(lignes)
"""
position = [(u, v) for v in range(68, 700, 66) for u in range(15, 800, 93)]
position_b = []
position_n = []
for i in range(40):
    position_n.append(Piece(position[i + 41], "black"))
    position_b.append(Piece(position[i], "white"))
on_init = [position_b, position_n]


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


def bb_inpos(pos):
    if pos_cl(pos):
        for u in on_init[0]:
            if u.getpos() == pos_cl(pos):
                return u


def bn_inpos(pos):
    if pos_cl(pos):
        for u in on_init[1]:
            if u.getpos() == pos_cl(pos):
                return u

elif [P_inPos(i) for i in
      l[l.index(self.poscl) + 1:l.index(pos) - 1]].count(
    None) == len(l[l.index(self.poscl) + 1:l.index(pos) - 1]) - 1:
for i in l[l.index(self.poscl) + 1:l.index(pos) - 1]:
    if P_inPos(i):
        if P_inPos(i).getcolor() == "white":
            P_inPos(i).setpos()
            P_inPos(self.poscl).superMove(pos)
            self.moved(pos)
        else:
            pass

elif [P_inPos(i) for i in
      l[l.index(self.poscl) + 1:l.index(pos) - 1]].count(
    None) == len(l[l.index(self.poscl) + 1:l.index(pos) - 1]) - 1:
for i in l[l.index(self.poscl) + 1:l.index(pos) - 1]:
    if P_inPos(i):
        if P_inPos(i).getcolor() == "black":
            P_inPos(i).setpos()
            P_inPos(self.poscl).superMove(pos)
            self.moved(pos)
        else:
            pass
        
        """
for i in range(10):
    if i==2:
        pass
    print(i)
""""
for j in l[l.index() + 1:l.index()-1]:
    print("qsdddddddddddddddddddddddddddddddddddddddddddddddd")
for i in l:
    if not [ for j in l[l.index(diag2[0]) + 1:diag2[3]+1]]:
  """

