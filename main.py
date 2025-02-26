import pygame
import random
import time

color = (random.randint(0, 64), random.randint(0, 255), random.randint(0, 128))
if sum(color) > 250: text_color = (color[0]//2, color[1]/2, color[2]//2)
else:  text_color = (255-color[0]//2, 255-color[1]//2, 255-color[2]//2)
target_color = (255-3*color[0]//4,255-3*color[1]//4,255-3*color[2]//4)

font_name = pygame.font.match_font('scoreboard')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_target(surf, color, rad, x, y):
    pygame.draw.circle(surf,color,(x+rad,y+rad),rad,5 )
    pygame.draw.circle(surf,color,(x+rad,y+rad),rad*5/8,3 )
    pygame.draw.line(surf, color, (x-rad/4, y+rad),(x+3*rad/4, y+rad ) , 3)
    pygame.draw.line(surf, color, (x+5*rad/4, y+rad),(x+9*rad/4, y+rad ) , 3)
    pygame.draw.line(surf, color, (x+rad, y-rad/4),(x+rad, y+3*rad/4 ) , 3)
    pygame.draw.line(surf, color, (x+rad, y+5*rad/4),(x+rad, y+9*rad/4 ) , 3)

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255,255,255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

target_width , target_height = 96,96
target_img = pygame.Surface( (target_width, target_height) )
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

score,shots, running = 0,10, True
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
            shots -= 1
            running = (shots > 0)
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            score += [25,10,4,2,1][int(dist*5)]

    draw_target( screen,target_color, target_width/2,target_x,target_y)
    draw_text(screen, f"shots left: {shots}  score: {score}", 40, SCREEN_WIDTH / 2, 10)
    pygame.display.flip()

draw_text(screen, "GAME OVER!", 40, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
pygame.display.flip()
time.sleep(3)
pygame.quit()
