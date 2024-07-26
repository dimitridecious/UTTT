import pygame


class Cell:
    def __init__(self, font, cell_width, cell_height):
        self.font = font
        self.taken = False
        self.value = '_'
        self.cell_width = cell_width
        self.cell_height = cell_height


    def get_cell_surface(self):
        cell_surface =  pygame.Surface((self.cell_width, self.cell_height))
        cell_surface.fill('white')

        if self.value != '_':
            font_surface = self.font.render(self.value, True, (0, 0, 0), (255, 255, 255, 0))
            f_x = font_surface.get_width() / 2
            f_y = font_surface.get_height() / 2
            cell_surface.blit(font_surface, ((self.cell_width / 2) - f_x + 4, (self.cell_height / 2) - f_y + 10))
        return cell_surface
    
    
    def set_value(self, value):
        if self.taken == False:
            self.value = value
            self.taken = True


class Board:
    def __init__(self, font, board_width, board_height):
        self.font = font
        self.board_pixel_width = board_width
        self.board_pixel_height = board_height
        self.cell_width = self.board_pixel_width / 3
        self.cell_height = self.board_pixel_height / 3
        self.surface = self.get_board_surface()
        self.taken = False
        self.value = '_'
        
        self.cells = []
        self.initialize_cells()


    def set_value(self, value):
        if self.taken == False:
            self.value = value
            self.taken = True


    def get_board_surface(self):
        board_surface = pygame.Surface((self.board_pixel_width, self.board_pixel_height))
        board_surface.fill('white')
        return board_surface


    def initialize_cells(self):
        for i in range(3):
            temp_arr = []
            for j in range(3):
                temp_cell = Cell(self.font, self.cell_width, self.cell_height)
                temp_arr.append(temp_cell)
            self.cells.append(temp_arr)

    def draw_winning_symbol(self):
        if self.value in ['X', 'O']:
            large_font = pygame.font.Font('../assets/tf2build.ttf', int(self.board_pixel_width))
            symbol_surface = large_font.render(self.value, True, (0, 0, 0))
            f_x = symbol_surface.get_width() / 2
            f_y = symbol_surface.get_height() / 2

            self.surface.fill('white')
            self.surface.blit(symbol_surface, ((self.board_pixel_width / 2) - f_x + 10, (self.board_pixel_height / 2) - f_y + 25))

    def draw_board(self, hover_pos = None):
        pos_x = 0
        pos_y = 0
        for i in range(3):
            for j in range(3):
                cell_surface = self.cells[i][j].get_cell_surface()
                self.surface.blit(cell_surface, (pos_x, pos_y))
                pos_x += self.cell_width
            pos_x = 0
            pos_y += self.cell_height
            pygame.draw.line(self.surface, (0, 0, 0), (self.cell_width, 0) , (self.cell_width, self.board_pixel_height))
            pygame.draw.line(self.surface, (0, 0, 0), (self.cell_width*2, 0) , (self.cell_width*2, self.board_pixel_height))
            pygame.draw.line(self.surface, (0, 0, 0), (0, self.cell_height) , (self.board_pixel_width, self.cell_height))
            pygame.draw.line(self.surface, (0, 0, 0), (0, self.cell_width*2) , (self.board_pixel_width, self.cell_width*2))

        if hover_pos:
            self.highlight_hovered_cell(hover_pos)

        if self.taken:
            self.draw_winning_symbol()


    def update_board(self, pos, player):
        if pos:
            x, y = pos
            row = int(y // self.cell_height)
            col = int(x // self.cell_width)
            if not self.cells[row][col].taken:
                self.cells[row][col].set_value(player)
                winner = self.check_winner()
                if winner:
                    self.set_value(winner)
                return True
            return False
        

    def check_winner(self):
        # row
        for i in range(3):
            if (self.cells[i][0].value == self.cells[i][1].value == self.cells[i][2].value) and (self.cells[i][0].value != '_'):
                return self.cells[i][0].value
        # col
        for i in range(3):
            if (self.cells[0][i].value == self.cells[1][i].value == self.cells[2][i].value) and (self.cells[0][i].value != '_'):
                return self.cells[0][i].value
        # diag
        if (self.cells[0][0].value == self.cells[1][1].value == self.cells[2][2].value) and (self.cells[0][0].value != '_'):
            return self.cells[0][0].value
        if (self.cells[0][2].value == self.cells[1][1].value == self.cells[2][0].value) and (self.cells[0][2].value != '_'):
            return self.cells[0][2].value

        return None


    def highlight_hovered_cell(self, pos):
        if pos:
            x, y = pos
            row = int(y // self.cell_height)
            col = int(x // self.cell_width)
            if not self.taken and not self.cells[row][col].taken:
                highlight_surface = pygame.Surface((self.cell_width, self.cell_height))
                highlight_surface.set_alpha(128)
                highlight_surface.fill('azure4')
                self.surface.blit(highlight_surface, (col * self.cell_width, row * self.cell_height))


class MasterBoard:
    def __init__(self, surface, font):
        self.surface = surface
        self.font = font
        self.master_board_pixel_width = surface.get_width()
        self.master_board_pixel_height = surface.get_height()
        self.board_width = self.master_board_pixel_width / 3
        self.board_height = self.master_board_pixel_height / 3
        
        self.boards = []
        self.initialize_boards()
        self.next_allowed_board = None


    def initialize_boards(self):
        for i in range(3):
            temp_arr = []
            for j in range(3):
                temp_board = Board(self.font, self.board_width, self.board_height)
                temp_arr.append(temp_board)
            self.boards.append(temp_arr)

    
    def draw_master_board(self, hover_pos = None):
        pos_x = 0
        pos_y = 0
        for i in range(3):
            for j in range(3):
                rel_hover_pos = None
                if hover_pos:
                    hover_x, hover_y = hover_pos
                    if (pos_x <= hover_x < pos_x + self.board_width) and (pos_y <= hover_y < pos_y + self.board_height):
                        rel_hover_pos = (hover_x - pos_x, hover_y - pos_y)

                self.boards[i][j].draw_board(rel_hover_pos)
                self.surface.blit(self.boards[i][j].surface, (pos_x, pos_y))
                pos_x += self.board_width
            pos_x = 0
            pos_y += self.board_height
            pygame.draw.line(self.surface, (0, 0, 0), (self.board_width, 0) , (self.board_width, self.master_board_pixel_height), 3)
            pygame.draw.line(self.surface, (0, 0, 0), (self.board_width*2, 0) , (self.board_width*2, self.master_board_pixel_height), 3)
            pygame.draw.line(self.surface, (0, 0, 0), (0, self.board_height) , (self.master_board_pixel_width, self.board_height), 3)
            pygame.draw.line(self.surface, (0, 0, 0), (0, self.board_width*2) , (self.master_board_pixel_width, self.board_width*2), 3)

 
    def update_master_board(self, pos, player):
        if pos:
            x, y = pos
            row = int(y // self.board_height)
            col = int(x // self.board_width)
            if self.next_allowed_board and self.next_allowed_board != (row, col):
                return False

            # Find the relative position in the mini board
            rel_x = x % self.board_width
            rel_y = y % self.board_height
            if not self.boards[row][col].taken:
                valid_move = self.boards[row][col].update_board((rel_x, rel_y), player)
                if valid_move:
                    board_won = self.boards[row][col].check_winner()
                    if board_won:
                        self.boards[row][col].set_value(player)
                    self.next_allowed_board = (int(rel_y // self.boards[row][col].cell_height), int(rel_x // self.boards[row][col].cell_width))
                    # If the next allowed board is taken or filled, open  the board
                    if self.boards[self.next_allowed_board[0]][self.next_allowed_board[1]].taken:
                        self.next_allowed_board = None
                    return True
        return False



    def check_winner(self):
        # row
        for i in range(3):
            if (self.boards[i][0].value == self.boards[i][1].value == self.boards[i][2].value) and (self.boards[i][0].value != '_'):
                return self.boards[i][0].value
        # col
        for i in range(3):
            if (self.boards[0][i].value == self.boards[1][i].value == self.boards[2][i].value) and (self.boards[0][i].value != '_'):
                return self.boards[0][i].value
        # diag
        if (self.boards[0][0].value == self.boards[1][1].value == self.boards[2][2].value) and (self.boards[0][0].value != '_'):
            return self.boards[0][0].value
        if (self.boards[0][2].value == self.boards[1][1].value == self.boards[2][0].value) and (self.boards[0][2].value != '_'):
            return self.boards[0][2].value

        return None
