import pygame


def play_game():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("blue")

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
