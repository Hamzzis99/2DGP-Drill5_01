from pico2d import *
open_canvas()
character = load_image('realsprite.png')
frame = 0
for x in range(0, 800, 10): #원래 10
 clear_canvas()
 character.clip_draw(frame * 100, 0, 100, 100, x, 90)
 update_canvas()
 frame = (frame + 1) % 8
 delay(0.05)
close_canvas()