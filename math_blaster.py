import pygame
import random

# --- LÓGICA DO NEGÓCIO (Igual ao anterior) ---
class MathEngine:
    def __init__(self):
        self.score = 0
        self.lives = 3

    def generate_question(self):
        ops = ['+', '-', '*']
        op = random.choice(ops)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        if op == '-' and a < b: a, b = b, a
        question_text = f"{a} {op} {b}"
        answer = eval(question_text)
        return question_text, answer

    def check_answer(self, user_input, correct_answer):
        try:
            return int(user_input) == correct_answer
        except ValueError:
            return False

    def update_score(self, correct):
        if correct: self.score += 10
        return self.score

    def lose_life(self):
        self.lives -= 1
        return self.lives > 0

# --- INTERFACE DO JOGO COM IMAGENS ---
def run_game():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Math Blaster: Dog vs Meteors")
    clock = pygame.time.Clock()
    
    # Fontes
    font_math = pygame.font.SysFont("Arial Black", 24, bold=True) # Fonte mais grossa para o meteoro
    font_hud = pygame.font.SysFont("Arial", 32)

    # --- CARREGAMENTO/CRIAÇÃO DE IMAGENS ---
    # NOTA IMPORTANTE: Se você tiver imagens reais (ex: "meteoro.png"), 
    # você substituiria as linhas abaixo por: 
    # meteor_img = pygame.image.load("meteoro.png").convert_alpha()
    
    # 1. Imagem do Meteoro (Placeholder: Quadrado Marrom)
    METEOR_SIZE = 70
    meteor_img = pygame.Surface((METEOR_SIZE, METEOR_SIZE))
    meteor_img.fill((100, 50, 0)) # Cor marrom
    # Desenhando uma borda rochosa simples
    pygame.draw.rect(meteor_img, (80, 40, 0), meteor_img.get_rect(), 3)

    # 2. Imagem do Jogador (Placeholder: Nave Azul do Cão)
    PLAYER_WIDTH, PLAYER_HEIGHT = 80, 50
    player_img = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
    player_img.fill((0, 100, 200)) # Cor azul
    # Desenhando um "cockpit"
    pygame.draw.circle(player_img, (200, 200, 255), (PLAYER_WIDTH//2, PLAYER_HEIGHT//2), 15)
    
    # Posição do jogador
    player_x = WIDTH // 2 - PLAYER_WIDTH // 2
    player_y = HEIGHT - PLAYER_HEIGHT - 10

    engine = MathEngine()
    enemies = []
    spawn_timer = 0
    input_text = ""
    game_over = False
    running = True

    while running:
        # Fundo estilo espaço
        screen.fill((10, 10, 30)) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if not game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    hit = False
                    for enemy in enemies:
                        if engine.check_answer(input_text, enemy['ans']):
                            enemies.remove(enemy)
                            engine.update_score(True)
                            hit = True
                            # Opcional: Adicionar som de tiro aqui
                            break 
                    input_text = "" # Limpa input após atirar
                
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if event.unicode.isnumeric():
                        input_text += event.unicode

        if not game_over:
            spawn_timer += 1
            if spawn_timer > 120: # Um pouco mais lento para dar tempo de ver
                q_text, q_ans = engine.generate_question()
                # O inimigo agora precisa considerar o tamanho da imagem para não nascer fora da tela
                enemies.append({
                    'text': q_text, 
                    'ans': q_ans, 
                    'x': random.randint(0, WIDTH - METEOR_SIZE), 
                    'y': -METEOR_SIZE
                })
                spawn_timer = 0

            for enemy in enemies[:]:
                enemy['y'] += 1.5 # Velocidade de queda
                if enemy['y'] > HEIGHT:
                    enemies.remove(enemy)
                    is_alive = engine.lose_life()
                    if not is_alive:
                        game_over = True

        # --- DESENHAR ---
        
        # 1. Desenhar a Nave do Jogador
        screen.blit(player_img, (player_x, player_y))

        # 2. Desenhar Inimigos (Meteoros com texto em cima)
        for enemy in enemies:
            # a) Desenha a imagem do meteoro
            screen.blit(meteor_img, (enemy['x'], enemy['y']))
            
            # b) Desenha o texto centralizado no meteoro
            text_surf = font_math.render(enemy['text'], True, (255, 255, 255))
            # Cálculo para centralizar o texto sobre a imagem do meteoro
            text_x = enemy['x'] + (METEOR_SIZE - text_surf.get_width()) // 2
            text_y = enemy['y'] + (METEOR_SIZE - text_surf.get_height()) // 2
            screen.blit(text_surf, (text_x, text_y))

        # Interface do Jogador (HUD)
        score_text = f"Score: {engine.score} | Lives: {engine.lives}"
        score_surf = font_hud.render(score_text, True, (255, 255, 0))
        screen.blit(score_surf, (10, 10))

        # Caixa de Input (Visualmente perto da nave)
        input_bg = pygame.Surface((200, 40))
        input_bg.fill((50, 50, 50))
        screen.blit(input_bg, (WIDTH//2 - 100, HEIGHT - 110))
        
        input_surf = font_hud.render(input_text, True, (0, 255, 0))
        # Centralizar o texto do input na caixa
        input_rect = input_surf.get_rect(center=(WIDTH//2, HEIGHT - 90))
        screen.blit(input_surf, input_rect)

        if game_over:
            over_surf = font_hud.render("GAME OVER", True, (255, 0, 0))
            over_rect = over_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(over_surf, over_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run_game()