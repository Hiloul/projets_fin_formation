import pygame

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre de jeu
WIDTH = 600
HEIGHT = 600

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialisation de la fenêtre de jeu
window = pygame.display.set_mode((WIDTH, HEIGHT))
# Titre du jeu en haut à gauche de la fenêtre
pygame.display.set_caption("Jeu du morpion")

# Grille de jeu
grid = [['', '', ''],
        ['', '', ''],
        ['', '', '']]

# Joueur actuel (X ou O)
current_player = 'X'

# Taille de la police d'écriture du texte
font = pygame.font.Font(None, 28)

# Fonction pour afficher la grille de jeu et les messages
def draw_grid():
    window.fill(BLACK)
    pygame.draw.line(window, WHITE, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 2)
    pygame.draw.line(window, WHITE, (2 * WIDTH / 3, 0), (2 * WIDTH / 3, HEIGHT), 2)
    pygame.draw.line(window, WHITE, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 2)
    pygame.draw.line(window, WHITE, (0, 2 * HEIGHT / 3), (WIDTH, 2 * HEIGHT / 3), 2)

    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'X':
                pygame.draw.line(window, RED, (j * WIDTH / 3, i * HEIGHT / 3), ((j + 1) * WIDTH / 3, (i + 1) * HEIGHT / 3), 2)
                pygame.draw.line(window, RED, (j * WIDTH / 3, (i + 1) * HEIGHT / 3), ((j + 1) * WIDTH / 3, i * HEIGHT / 3), 2)
            elif grid[i][j] == 'O':
                pygame.draw.circle(window, RED, (int((j + 0.5) * WIDTH / 3), int((i + 0.5) * HEIGHT / 3)), int(WIDTH / 6), 2)

    # Affichage des messages
    if game_over:
        if winner == 'X':
            text = font.render("Le joueur X a gagné !", True, WHITE)
        elif winner == 'O':
            text = font.render("Le joueur O a gagné !", True, WHITE)
        else:
            text = font.render("Match nul !", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - HEIGHT // 6))
        window.blit(text, text_rect)

# Fonction pour vérifier si un joueur a gagné
def check_winner(player):
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] == player:
            return True
        if grid[0][i] == grid[1][i] == grid[2][i] == player:
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] == player:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == player:
        return True
   
        return False

# Fonction pour vérifier si la grille est pleine
def is_grid_full():
    for row in grid:
        if '' in row:
            return False
    return True


# Fonction pour le joueur ordinateur
def joueur_ordi():
    pass

# Boucle principale du jeu
running = True
game_over = False
winner = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # Obtenir les coordonnées du clic de la souris
            x, y = pygame.mouse.get_pos()
            # Convertir les coordonnées en indices de la grille
            row = int(y // (HEIGHT / 3))
            col = int(x // (WIDTH / 3))
            # Vérifier si la case est vide
            if grid[row][col] == '':
                # Jouer le coup du joueur actuel
                grid[row][col] = current_player
                # Vérifier si le joueur a gagné
                if check_winner(current_player):
                    game_over = True
                    winner = current_player
                # Vérifier si la grille est pleine
                elif is_grid_full():
                    game_over = True
                # Changer de joueur
                current_player = 'O' if current_player == 'X' else 'X'

    draw_grid()
    pygame.display.flip()

# Fermeture de la fenêtre de jeu
pygame.quit()
