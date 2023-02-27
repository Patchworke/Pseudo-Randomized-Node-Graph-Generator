from random import randrange
from tkinter import Tk, Canvas
from math import sqrt


# Dictionary data looks like this:
#   A B C D E
# 0 a,b,c,d,e,
# 1 a,g,h,i,j,
# 2 b,g,m,n,o,
# 3 c,h,m,s,t,
# 4 d,i,n,s,y,
# 5 e,j,o,t,y
# So it could be simplified later

# Sorted list structure could save calculating distances to every other node

# Some nodes are isolated or in islands

# Add an island structure (with "n" islands)

# Node labels could be arranged left to right, top to bottom instead of randomly distributed

# Complexity is maximum, not average, and not derived from placement of nodes


def draw_graph(nodes, complexity):
    # Variables
    width = 400
    diameter = round(width / 20)
    radius = round(diameter / 2)
    space = 100
    font_size = round(diameter / 1.5)
    bg = '#282828'

    # Window & Canvas Initialization
    window = Tk()
    window.geometry(f'{width}x{width}')
    window.configure(background=bg)
    window.title('Graph')
    canvas = Canvas(window,
                    width=width,
                    height=width,
                    background=bg)
    canvas.pack()

    # Randomly Generate Nodes
    coords = []
    graph_coords = {}
    for node in range(nodes):
        x = randrange(diameter, width - diameter)
        y = randrange(diameter, width - diameter)

        # for node_2 in range(len(graph_coords)):
        #     while sqrt((graph_coords[node_2][0] - x) ** 2 + (graph_coords[node_2][1] - y) ** 2) < space:
        #         x = randrange(diameter, width - diameter)  # x and y are not updated?
        #         y = randrange(diameter, width - diameter)

        canvas.create_oval(x, y, x + diameter, y + diameter,
                           width=0,
                           fill='white')
        coords.append([x, y])
        graph_coords.update({node: coords[node]})
    # print(graph_coords)

    # Determine Edges
    edges = []
    for node in range(nodes):
        distance_0 = {}
        x = graph_coords[node][0]
        y = graph_coords[node][1]
        # Calculate Nodal Distances
        for node_2 in range(nodes):
            if node != node_2:
                x_0 = graph_coords[node_2][0]
                y_0 = graph_coords[node_2][1]
                delta_x = abs(x_0 - x)
                delta_y = abs(y_0 - y)
                distance_0.update({f'{node}>{node_2}': (round(sqrt(delta_x ** 2 + delta_y ** 2)))})
        # print(distance_0)
        # Find Minimum Distances
        for node_mins in range(m := randrange(2, complexity)):
            key_list = list(distance_0.keys())
            val_list = list(distance_0.values())
            min_val = min(distance_0.values())
            min_val_index = val_list.index(min_val)
            min_key = key_list[min_val_index]
            del distance_0[f'{min_key}']
            edges.append(min_key)
    # print(edges)

    # Draw Edges
    for node in range(nodes - 1):
        node_x = graph_coords[node][0]
        node_y = graph_coords[node][1]
        for node_2 in range(nodes):
            if node != node_2 and f'{node}>{node_2}' in edges:  # Does not account for slow redundancies (creates two lines)
                node_2_x = graph_coords[node_2][0]
                node_2_y = graph_coords[node_2][1]
                # print(f'({node_x},{node_y})>({node_2_x},{node_2_y})')
                canvas.create_line(node_x + radius, node_y + radius, node_2_x + radius, node_2_y + radius,
                                   width=3,
                                   fill='white')

    # Label Node
    for node in range(nodes):
        x = graph_coords[node][0]
        y = graph_coords[node][1]
        canvas.create_text(x + radius, y + radius,
                           text=node,
                           font=('Calibri', font_size))

    window.mainloop()


def main():
    while True:
        nodes = 10
        complexity = 3
        draw_graph(nodes, complexity)


if __name__ == '__main__':
    main()
