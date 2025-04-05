import time

import pygame as pg

pg.init()
SIZE = WIDTH, HEIGHT, = 600, 400
screen = pg.display.set_mode(SIZE)

sun_y = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill('#b0b8a4')
    pg.draw.circle(screen, 'yellow', (300, sun_y), 50)
    pg.draw.rect(screen, '#277c22', (0, 230, WIDTH, 230))
    pg.draw.line(screen, 'black', (0, 230), (WIDTH, 230), 2)

    font = pg.font.Font(None, 50)
    s = font.render('Д.А.Л.Е.Р.', True, 'black')
    screen.blit(s, (0, 0))

    pg.display.flip()
    sun_y += 1
    time.sleep(0.05)
