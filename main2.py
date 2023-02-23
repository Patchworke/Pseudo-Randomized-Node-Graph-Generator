from random import randrange
from tkinter import Tk, Canvas
from math import sqrt


def draw_graph(nodes, complexity):
    # Variables
    width = 400
    diameter = round(width / 9)
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

    # Random Node Coordinate Generation
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
    print(graph_coords)

    # Node Finds "m" Closest Nodes
    m = randrange(1, complexity)

    for node in range(nodes):
        distances = []
        distance = []
        x = graph_coords[node][0]
        y = graph_coords[node][1]
        for node_2 in range(nodes):
            if node != node_2:
                print(f'{node}->{node_2}')
                x_0 = graph_coords[node_2][0]
                y_0 = graph_coords[node_2][1]
                delta_x = abs(x_0 - x)
                delta_y = abs(y_0 - y)
                print(delta_x)
                print(delta_y)
                distance.append(round(sqrt(delta_x ** 2 + delta_y ** 2)))
                print(distance)
                print()
        distances.append(distance)
    print(distances)

    for node in range(nodes):
        x = graph_coords[node][0]
        y = graph_coords[node][1]
        canvas.create_text(x + radius, y + radius,
                           text=node,
                           font=('Calibri', font_size))

    window.mainloop()


def main():
    nodes = 6
    complexity = 3
    draw_graph(nodes, complexity)


if __name__ == '__main__':
    main()
