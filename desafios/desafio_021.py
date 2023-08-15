import pygame as pg
pg.init()

#removido a musica por direitos autorais
pg.mixer.music.load('immigrant_song.mp3')

pg.mixer.music.play()
input()

pg.event.wait()