import matplotlib.pyplot as plt
from networkx import *

g = Graph()
for i in range(1,82):
    g.add_node(i)
pos = spring_layout(g)
for i in range(9):
    for j in range(9):
        pos[j +9*i +1] = [j,i]

for i in range(0,9,2):
    for j in range(9):
        g.add_edge(i+1,i+73)
        g.add_edge(1+i*9,9+i*9)
x,y = 1,1
for i in range(5):
    g.add_edge(x, y)
    g.add_edge(x,82-y)
    g.add_edge(82-x,y)
    g.add_edge(82-x,82-y)
    x+=2
    y+=18
g.remove_edges_from([(81,81),(1,1),(9,9),(73,73)])

draw(g,pos,node_size =20,node_color= 'k',edge_color = 'k')
plt.show()