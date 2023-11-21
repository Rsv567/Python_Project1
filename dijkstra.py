from heapq import *
from bfs import *

screen1 = pygame.display.set_mode((WIDTH, HEIGHT))


def get_circle(x, y):
    return (x * TILE + TILE // 2, y * TILE + TILE // 2), TILE // 4


def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


def get_next_nodes(x, y):
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [
        (map_area[y + dy][x + dx], (x + dx, y + dy))
        for dx, dy in ways
        if check_next_node(x + dx, y + dy)
    ]


cols, rows = 15, 14
TILE = 50

pygame.init()
sc = pygame.display.set_mode([cols * TILE, rows * TILE])
clock = pygame.time.Clock()
# map_area
map_area = [
    "444412241222222",
    "111441141111322",
    "221141141114444",
    "222141224441111",
    "222241110121112",
    "222441111111212",
    "214411111111122",
    "244100000000111",
    "441111111101101",
    "100444411102111",
    "014111441100222",
    "124222441110011",
    "244112244211102",
    "214422422212202",
]
map_area = [[int(char) for char in string] for string in map_area]

graph = {}
for y, row in enumerate(map_area):
    for x, col in enumerate(row):
        graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)


def dijkstra():
    start = (0, 7)
    goal = start
    queue = []
    heappush(queue, (0, start))
    cost_visited = {start: 0}
    visited = {start: None}

    bg = pygame.image.load("images/forest.png").convert()
    bg = pygame.transform.scale(bg, (cols * TILE, rows * TILE))
    while True:

        sc.blit(bg, (0, 0))

        mouse_pos = get_click_mouse_pos(screen1)
        if mouse_pos:
            goal = mouse_pos
        if goal != start:
            pygame.draw.circle(sc, pygame.Color("purple"), *get_circle(*goal))


        if queue:
            cur_cost, cur_node = heappop(queue)
            if cur_node == goal:
                queue = []
                continue

            next_nodes = graph[cur_node]
            for next_node in next_nodes:
                neigh_cost, neigh_node = next_node
                new_cost = cost_visited[cur_node] + neigh_cost

                if (
                    neigh_node not in cost_visited
                    or new_cost < cost_visited[neigh_node]
                ):
                    heappush(queue, (new_cost, neigh_node))
                    cost_visited[neigh_node] = new_cost
                    visited[neigh_node] = cur_node

        path_head, path_segment = cur_node, cur_node
        while path_segment:
            pygame.draw.circle(sc, pygame.Color("brown"), *get_circle(*path_segment))
            path_segment = visited[path_segment]

        pygame.draw.circle(sc, pygame.Color("blue"), *get_circle(*start))
        pygame.draw.circle(sc, pygame.Color("magenta"), *get_circle(*path_head))

        [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
        pygame.display.flip()
        clock.tick(7)
