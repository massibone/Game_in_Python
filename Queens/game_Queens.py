import pygame
import sys

# Inizializzazione di Pygame
pygame.init()

# Costanti
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colori
WHITE = (255, 255, 255)
BLACK = (240, 240, 240)
GOLD = (255, 215, 0)

# Creazione della finestra
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Queens Game")

# Inizializzazione della scacchiera
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Caricamento e ridimensionamento dell'immagine della corona
crown = pygame.image.load("crown.png")  # Assicurati di avere un'immagine "crown.png" nella stessa cartella del tuo script
crown = pygame.transform.scale(crown, (SQUARE_SIZE // 2, SQUARE_SIZE // 2))

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[row][col] == 1:
                screen.blit(crown, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4))

def is_safe(row, col):
    # Controlla la riga e la colonna
    if 1 in board[row] or 1 in [board[i][col] for i in range(ROWS)]:
        return False
    
    # Controlla le diagonali
    for i in range(ROWS):
        if (row - i >= 0 and col - i >= 0 and board[row-i][col-i] == 1) or \
           (row - i >= 0 and col + i < COLS and board[row-i][col+i] == 1) or \
           (row + i < ROWS and col - i >= 0 and board[row+i][col-i] == 1) or \
           (row + i < ROWS and col + i < COLS and board[row+i][col+i] == 1):
            return False
    
    return True

def main():
    queens_placed = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and queens_placed < 8:
                x, y = pygame.mouse.get_pos()
                col, row = x // SQUARE_SIZE, y // SQUARE_SIZE
                if is_safe(row, col):
                    board[row][col] = 1
                    queens_placed += 1
        
        screen.fill(WHITE)
        draw_board()
        pygame.display.flip()

        if queens_placed == 8:
            font = pygame.font.Font(None, 36)
            text = font.render("Congratulazioni! Hai vinto!", True, GOLD)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()