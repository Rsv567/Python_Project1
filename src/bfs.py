from collections import deque
from generator_of_labirint import *


def create_graph():
    graph = {}
    for i in range(cols * rows):
        x_cord = grid_cells[i].x
        y_cord = grid_cells[i].y
        if not grid_cells[i].walls["top"]:
            graph[(x_cord, y_cord)] = graph.get((x_cord, y_cord), []) + [
                (x_cord, y_cord - 1)
            ]
        if not grid_cells[i].walls["bottom"]:
            graph[(x_cord, y_cord)] = graph.get((x_cord, y_cord), []) + [
                (x_cord, y_cord + 1)
            ]
        if not grid_cells[i].walls["left"]:
            graph[(x_cord, y_cord)] = graph.get((x_cord, y_cord), []) + [
                (x_cord - 1, y_cord)
            ]
        if not grid_cells[i].walls["right"]:
            graph[(x_cord, y_cord)] = graph.get((x_cord, y_cord), []) + [
                (x_cord + 1, y_cord)
            ]
    return graph


def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


def find_way():
    start = (0, 0)
    goal = start
    queue = deque([start])
    visited = {start: None}

    running = True
    while running:
        [pygame.draw.rect(screen, (19, 242, 17), get_rect(x, y)) for x, y in visited]
        [pygame.draw.rect(screen, (19, 242, 17), get_rect(x, y)) for x, y in queue]
        graph = create_graph()
        # BFS logic

        mouse_pos = get_click_mouse_pos(screen)
        if mouse_pos:
            queue, visited = bfs(start, mouse_pos, graph)
            goal = mouse_pos

        # draw path
        path_head, path_segment = goal, goal
        while path_segment and path_segment in visited:
            pygame.draw.rect(
                screen,
                pygame.Color("white"),
                get_rect(*path_segment),
                TILE,
                border_radius=TILE // 3,
            )
            path_segment = visited[path_segment]
            pygame.draw.rect(
                screen, pygame.Color("blue"), get_rect(*start), border_radius=TILE // 3
            )
            pygame.draw.rect(
                screen,
                pygame.Color("magenta"),
                get_rect(*path_head),
                border_radius=TILE // 3,
            )

        pygame.display.flip()
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


def get_click_mouse_pos(screen):
    x, y = pygame.mouse.get_pos()
    cell_x, cell_y = x // TILE, y // TILE

    click = pygame.mouse.get_pressed()
    if click[0]:
        pygame.draw.rect(screen, pygame.Color("red"), get_rect(cell_x, cell_y))
    return (cell_x, cell_y) if click[0] else False


def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return queue, visited
