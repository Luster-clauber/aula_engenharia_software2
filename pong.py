import pygame
import random

# Inicializando o pygame
pygame.init()

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definindo as dimens�es da tela
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Definindo os par�metros do jogo
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
BALL_SIZE = 15
FPS = 60

# Definindo as posi��es iniciais das raquetes e da bola
paddle1_x = 30
paddle2_x = SCREEN_WIDTH - 30 - PADDLE_WIDTH
paddle1_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
ball_velocity_x = random.choice([-4, 4])
ball_velocity_y = random.choice([-4, 4])

# Pontua��o
score1 = 0
score2 = 0

# Fun��o para desenhar as raquetes e a bola
def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 1)
    pygame.draw.rect(screen, WHITE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 1)
    
    # Exibindo a pontua��o
    font = pygame.font.SysFont("Arial", 24)
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))
    
    pygame.display.update()

# Fun��o para salvar a pontua��o em um arquivo de texto
def save_score():
    with open("score.txt", "a") as file:
        file.write(f"Pontua��o Final: {score1} - {score2}\n")

# Fun��o principal do jogo
def game_loop():
    global paddle1_y, paddle2_y, ball_x, ball_y, ball_velocity_x, ball_velocity_y, score1, score2

    clock = pygame.time.Clock()

    # Loop principal do jogo
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Movendo as raquetes
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1_y > 0:
            paddle1_y -= 5
        if keys[pygame.K_s] and paddle1_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
            paddle1_y += 5
        if keys[pygame.K_UP] and paddle2_y > 0:
            paddle2_y -= 5
        if keys[pygame.K_DOWN] and paddle2_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
            paddle2_y += 5
        
        # Movendo a bola
        ball_x += ball_velocity_x
        ball_y += ball_velocity_y

        # Verificando colis�o com o topo e a base da tela
        if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
            ball_velocity_y = -ball_velocity_y
        
        # Verificando colis�o com as raquetes
        if (ball_x <= paddle1_x + PADDLE_WIDTH and paddle1_y < ball_y + BALL_SIZE and paddle1_y + PADDLE_HEIGHT > ball_y):
            ball_velocity_x = -ball_velocity_x
        if (ball_x + BALL_SIZE >= paddle2_x and paddle2_y < ball_y + BALL_SIZE and paddle2_y + PADDLE_HEIGHT > ball_y):
            ball_velocity_x = -ball_velocity_x

        # Verificando se a bola ultrapassou as raquetes
        if ball_x <= 0:
            score2 += 1
            ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_velocity_x = random.choice([-4, 4])
            ball_velocity_y = random.choice([-4, 4])
        
        if ball_x >= SCREEN_WIDTH - BALL_SIZE:
            score1 += 1
            ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_velocity_x = random.choice([-4, 4])
            ball_velocity_y = random.choice([-4, 4])

        draw_objects()
        clock.tick(FPS)
    
    # Salvar a pontua��o ao fim do jogo
    save_score()
    pygame.quit()

# Rodando o jogo
game_loop()
