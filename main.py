from gamemanager import GameManager
import pygame

#system variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

#game objects
#TODO:make a masterboard instance and gamemanager instance
#TODO:give the game manager the masterboard to manage
#TODO:use the gamemanager to perform manipulations to the masterboard in main gameloop!

#pygame gameloop 
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ultimate Tic Tac Toe")
    clock = pygame.time.Clock()
    running = True
    game_manager = GameManager(SCREEN_WIDTH, SCREEN_HEIGHT, screen)

    while running:

        game_manager.draw_game()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                sel_cell = game_manager.get_hovered_cell(position)
                #set that cells sel val to true

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()