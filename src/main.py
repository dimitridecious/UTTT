from uttt import Cell, Board, MasterBoard
import pygame


def draw_starting_menu(screen, font, start_button, x_button, o_button):
    screen.fill("white")

    title_surface_1 = font.render("Ultimate", True, (0, 0, 0))
    title_surface_2 = font.render("Tic Tac Toe", True, (0, 0, 0))
    title_rect_1 = title_surface_1.get_rect(center = (screen.get_width() // 2, screen.get_height() // 4 - 75))
    title_rect_2 = title_surface_2.get_rect(center = (screen.get_width() // 2, screen.get_height() // 4 + 30))

    screen.blit(title_surface_1, title_rect_1)
    screen.blit(title_surface_2, title_rect_2)
    
    # start button
    pygame.draw.rect(screen, "green", start_button)
    start_surface = font.render("Start Game", True, (0, 0, 0))
    start_x = start_button.x + (start_button.width - start_surface.get_width()) // 2
    start_y = start_button.y + (start_button.height - start_surface.get_height()) // 2 + 10
    screen.blit(start_surface, (start_x, start_y))

    # x button
    pygame.draw.rect(screen, "blue", x_button)
    x_surface = font.render("X", True, (0, 0, 0))
    x_x = x_button.x + (x_button.width - x_surface.get_width()) // 2 + 3
    x_y = x_button.y + (x_button.height - x_surface.get_height()) // 2 + 10
    screen.blit(x_surface, (x_x, x_y))

    # o button
    pygame.draw.rect(screen, "red", o_button)
    o_surface = font.render("O", True, (0, 0, 0))
    o_x = o_button.x + (o_button.width - o_surface.get_width()) // 2 + 3
    o_y = o_button.y + (o_button.height - o_surface.get_height()) // 2 + 10
    screen.blit(o_surface, (o_x, o_y))

    pygame.display.flip()


def draw_winning_menu(screen, font, winner, reset_button, exit_button):
    screen.fill("white")

    if winner:
        message = f"{winner} Wins!"
    else:
        message = "It's a Draw!"

    message_surface = font.render(message, True, (0, 0, 0))
    message_rect = message_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 4))
    screen.blit(message_surface, message_rect)

    # Reset button
    pygame.draw.rect(screen, "green", reset_button)
    reset_surface = font.render("Reset", True, (0, 0, 0))
    reset_x = reset_button.x + (reset_button.width - reset_surface.get_width()) // 2
    reset_y = reset_button.y + (reset_button.height - reset_surface.get_height()) // 2 + 10
    screen.blit(reset_surface, (reset_x, reset_y))

    # Exit button
    pygame.draw.rect(screen, "red", exit_button)
    exit_surface = font.render("Exit", True, (0, 0, 0))
    exit_x = exit_button.x + (exit_button.width - exit_surface.get_width()) // 2
    exit_y = exit_button.y + (exit_button.height - exit_surface.get_height()) // 2 + 10
    screen.blit(exit_surface, (exit_x, exit_y))

    pygame.display.flip()


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("UTTT")
    clock = pygame.time.Clock()
    running = True
    clicked = False
    pos = None
    current_player = 'X'
    font = pygame.font.Font('../assets/tf2build.ttf', int(screen.get_width() / 9))
    master_board = MasterBoard(screen, font)
    winner = None
    hovered_pos = None

    # menu setups
    start_button = pygame.Rect((screen.get_width() - 700) // 2, screen.get_height() // 2 - 50, 700, 100)
    x_button = pygame.Rect(screen.get_width() // 2 - 150, screen.get_height() // 2 + 100, 100, 100)
    o_button = pygame.Rect(screen.get_width() // 2 + 50, screen.get_height() // 2 + 100, 100, 100)
    reset_button = pygame.Rect((screen.get_width() - 700) // 2, screen.get_height() // 2 - 50, 700, 100)
    exit_button = pygame.Rect((screen.get_width() - 700) // 2, screen.get_height() // 2 + 100, 700, 100)
    show_menu = True
    show_winning_menu = False

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False
                pos = pygame.mouse.get_pos()
                if show_menu:
                    if start_button.collidepoint(pos):
                        show_menu = False
                    if x_button.collidepoint(pos):
                        current_player = 'X'
                    if o_button.collidepoint(pos):
                        current_player = 'O'
                elif show_winning_menu:
                    if reset_button.collidepoint(pos):
                        show_winning_menu = False
                        show_menu = True
                        master_board = MasterBoard(screen, font)
                        current_player = 'X'
                    if exit_button.collidepoint(pos):
                        running = False
                else:
                    if master_board.update_master_board(pos, current_player):
                        winner = master_board.check_winner()
                        if winner:
                            show_winning_menu = True
                        else:
                            current_player = 'O' if current_player == 'X' else 'X'
            if event.type == pygame.MOUSEMOTION:
                hovered_pos = pygame.mouse.get_pos()

        if show_menu:
            draw_starting_menu(screen, font, start_button, x_button, o_button)
        elif show_winning_menu:
            draw_winning_menu(screen, font, winner, reset_button, exit_button)
        else:
            # fill the screen with a color to wipe away anything from last frame
            screen.fill("white")

            # RENDER YOUR GAME HERE
            master_board.draw_master_board(hovered_pos)
            # flip() the display to put your work on screen
            pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == '__main__':
    main()