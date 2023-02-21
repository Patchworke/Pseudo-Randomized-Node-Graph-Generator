from random import randrange
from tkinter import Tk, Canvas
from math import sqrt


# Three problems with this code:

# 1. Too simplistic
#    The graph is created based on only 1 initial connection instead of multiple.
#    Reducing the possibilities of generated graphs.

# 2. Too convoluted
#    Realistically, paths should be more likely to be generated between closer nodes.
#    Instead, they pass through long distances, and between or over other nodes.
#    Therefore, the graph should be created based on the original location of the nodes.
#    Instead of randomly generating node locations and edges, only the node location will be randomized.

# 3. Too tight
#    The randomized node locations are not checked for proximity interception with other existing nodes,
#    creating nodes unrealistically close together.


def create_graph(n):
    nodes = n
    edges = []

    # Initial Connections
    for i in range(nodes):
        j = [randrange(0, nodes)]
        while i in j:
            j = [randrange(0, nodes)]
        edges.append(j)

    # Mutual Edges & Repetitive Statements
    for cur_node in range(nodes):
        for var_node in range(nodes):
            j = edges[var_node]
            if cur_node in j:
                edges[cur_node].append(var_node)
            edges[var_node] = [*set(edges[var_node])]  # removes duplicates TODO: Remove comment

    # Create Graph Dictionary
    graph = {}
    for i in range(nodes):
        graph.update({i: edges[i]})
    return graph


def draw_graph(nodes, graph):
    # Variables
    print(graph)
    width = 400
    diameter = round(width / 9)
    radius = round(diameter / 2)
    space = 500
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

    # Random Node Coordinate Generation
    coords = []
    graph_coords = {}
    for node in range(nodes):
        x = randrange(diameter, width - diameter)
        y = randrange(diameter, width - diameter)

        # for node_2 in range(len(graph_coords)):
        #     distance = round(
        #         sqrt((graph_coords[node_2][0] - x) ** 2 + (graph_coords[node_2][1] - y) ** 2))  # TODO remove
        #     while sqrt((graph_coords[node_2][0] - x) ** 2 + (graph_coords[node_2][1] - y) ** 2) < space:
        #         x = randrange(diameter, width - diameter)   # x and y are not updated?
        #         y = randrange(diameter, width - diameter)

        canvas.create_oval(x, y, x + diameter, y + diameter,
                           width=0,
                           fill='white')
        coords.append([x, y])
        graph_coords.update({node: coords[node]})
    print(graph_coords)

    # Determine Edges Between Nodes
    for node in range(nodes):
        x = graph_coords[node][0]
        y = graph_coords[node][1]
        for j in range(len(graph[node])):
            a = graph_coords[graph[node][j]][0]
            b = graph_coords[graph[node][j]][1]
            canvas.create_line(x + radius, y + radius, a + radius, b + radius,
                               width=3,
                               fill='white')

    for node in range(nodes):
        x = graph_coords[node][0]
        y = graph_coords[node][1]
        canvas.create_text(x + radius, y + radius,
                           text=node,
                           font=('Calibri', font_size))

    window.mainloop()


def main():
    nodes = 6
    while True:
        draw_graph(nodes, create_graph(nodes))


if __name__ == '__main__':
    main()
