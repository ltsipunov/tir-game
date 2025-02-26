import pygame
import random

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
if sum(color) > 250: text_color = (color[0]//16, color[1]/16, color[2]//16)
else:  text_color = (255-color[0]//16, 255-color[1]/16, 255-color[2]//16)

font_name = pygame.font.match_font('scoreboard')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255,255,255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_img.set_colorkey(WHITE)
target_width = target_img.get_width()
target_height = target_img.get_height()
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

score, running = 0,True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        center_x,center_y = target_x + target_width/2, target_y + target_height/2
        dist = ((center_x-mouse_x)**2 + (center_y-mouse_y)**2)**0.5/(target_width/2)
        if dist < 1:
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            score += [25,10,4,2,1][int(dist*5)]

    screen.blit(target_img, (target_x, target_y))
    draw_text(screen, 'score: '+str(score), 40, SCREEN_WIDTH / 2, 10)
    pygame.display.flip()

pygame.quit()
