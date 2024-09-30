from pico2d import *

open_canvas()

grass = load_image('TUK_GROUND.png')
player_running_img = load_image('movespritereal.png')
player_idle_img = load_image('stayspritereal.png')

def handle_events():
    global running
    global direction
    global is_moving

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                direction = 1
                is_moving = True
            elif event.key == SDLK_LEFT:
                direction = -1
                is_moving = True
            elif event.key == SDLK_UP:
                direction = 2
                is_moving = True
            elif event.key == SDLK_DOWN:
                direction = -2
                is_moving = True
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key in (SDLK_RIGHT, SDLK_LEFT, SDLK_UP, SDLK_DOWN):
                direction = 0
                is_moving = False

running = True
x = 800 // 2
y = 90
frame = 0
frame2 = 0
direction = 1
is_moving = False

while running:
    clear_canvas()
    grass.draw(404, 246)

    if is_moving:
        if direction == 1:
            player_running_img.clip_draw(frame * 100, 100, 100, 100, x, y)
            x += 5
        elif direction == -1:
            player_running_img.clip_draw(frame * 100, 0, 100, 100, x, y)
            x -= 5
        elif direction == 2:
            player_running_img.clip_draw(frame * 100, 200, 100, 100, x, y)
            y += 10
        elif direction == -2:
            player_running_img.clip_draw(frame * 100, 300, 100, 100, x, y)
            y -= 10
        frame = (frame + 1) % 15
    else:
        if direction == 1:
            player_idle_img.clip_draw(frame2 * 100, 100, 100, 100, x, y)
        elif direction == -1:
            player_idle_img.clip_draw(frame2 * 100, 0, 100, 100, x, y)
        elif direction == 2:
            player_idle_img.clip_draw(frame2 * 100, 200, 100, 100, x, y)
        elif direction == -2:
            player_idle_img.clip_draw(frame2 * 100, 300, 100, 100, x, y)
        frame2 = (frame2 + 1) % 4

    if x >= 800 or x <= -1 or y >= 800 or y <= -1:
        close_canvas()
        exit()

    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()
