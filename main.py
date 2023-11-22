import pygame
from src.bfs import Bfs
from src.button import ImageButton
from src.config import WIDTH
from src.config import HEIGHT
from src.dijkstra import Dijkstra
from src.dijkstra import screen1
from src.dijkstra import clock
from src.generator_of_labirint import generate_labirint


pygame.init()
pygame.display.set_caption("Labirint")
generator1 = ImageButton(
    WIDTH / 2 - (150 / 2),
    70,
    150,
    74,
    "Лабиринт",
    "images/red.png",
    "images/green.com.png",
)

dijkstra1 = ImageButton(
    WIDTH / 2 - (150 / 2),
    200,
    150,
    74,
    "Дейкстра",
    "images/red.png",
    "images/green.com.png",
)
deikstra = Dijkstra()
generate = generate_labirint()
bfs2 = Bfs()


def MainMenu():
    running = True
    while running:

        screen1.fill((243, 215, 18))

        screen1.blit(
            pygame.transform.scale(
                pygame.image.load("images/icon.png"), (WIDTH, HEIGHT)
            ),
            (0, 0),
        )

        generator1.check_hover(pygame.mouse.get_pos())
        generator1.draw(screen1)

        dijkstra1.check_hover(pygame.mouse.get_pos())
        dijkstra1.draw(screen1)

        pygame.display.flip()
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and event.button == generator1:
                generate.generate_labirint()
                bfs2.find_way()
            if event.type == pygame.USEREVENT and event.button == dijkstra1:
                deikstra.dijkstra()
            generator1.handle_event(event)
            dijkstra1.handle_event(event)
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


MainMenu()
