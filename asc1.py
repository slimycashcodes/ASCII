import pygame
import math
import colorsys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
hue = 0

WIDTH = 800
HEIGHT = 900

x_separator = 10
y_separator = 20

rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0 

theta_spacing = 10
phi_spacing = 2 

chars = ".,-~:;=!*#$@"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Donut')
font = pygame.font.SysFont('Arial', 15, bold=True)

clock = pygame.time.Clock()  


def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, (255, 0, 0))
    display_surface.blit(text, (x_start, y_start))


run = True
while run:
    screen.fill((black))

    x_start, y_start = 0, 0

    z = [0] * screen_size 
    b = [' '] * screen_size
    for j in range(0, 628, theta_spacing): 
        for i in range(0, 628, phi_spacing): 
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d+2
            D = 1/(c*h*e + f*g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c*h*g - f*e
            x = int(x_offset + 40*D*(l*h*m -t*n))
            y = int(y_offset + 20*D*(l*h*n+ t*m))
            o = int(x + columns*y)
            N = int(8 * ((f*e - c*d*g)*m - c*d*e - f*g - l*d*n))
            if rows>y>0 and 0<x<columns and D>z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    for i in range(len(b)):
        A += 0.00004  
        B += 0.00002
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator

    pygame.display.update()
    hue += 0.005

    # handle quit & ESC
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    clock.tick(30) 

pygame.quit()
