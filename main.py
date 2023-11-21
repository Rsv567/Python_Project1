from dijkstra import *
from button import *

pygame.init()

WIDTH1, HEIGHT1 = WIDTH, HEIGHT

pygame.display.set_caption("Labirint")
generator1 = image_button(
    WIDTH1 / 2 - (150 / 2),
    70,
    150,
    74,
    "Лабиринт",
    "images/red.png",
    "images/green.com.png",
)

dijkstra1 = image_button(
    WIDTH1 / 2 - (150 / 2),
    200,
    150,
    74,
    "Дейкстра",
    "images/red.png",
    "images/green.com.png",
)


def main_menu():
    running = True
    while running:

        screen1.fill((243, 215, 18))

        screen1.blit(
            pygame.transform.scale(
                pygame.image.load("images/icon.png"), (WIDTH1, HEIGHT1)
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
                generate_labirint()
                find_way()
            if event.type == pygame.USEREVENT and event.button == dijkstra1:
                dijkstra()
            generator1.handle_event(event)
            dijkstra1.handle_event(event)
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


main_menu()
