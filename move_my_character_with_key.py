from pico2d import *

# 캔버스 열기
open_canvas()

# 이미지 로드
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
                direction = 1  # 오른쪽 방향
                is_moving = True
            elif event.key == SDLK_LEFT:
                direction = -1  # 왼쪽 방향
                is_moving = True
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT or event.key == SDLK_LEFT:
                is_moving = False


# 전역 변수 초기화
running = True
x = 800 // 2
frame = 0
frame2 = 0  # idle 애니메이션을 위한 별도 프레임
direction = 1
is_moving = False  #

# 메인 루프
while running:
    clear_canvas()
    grass.draw(404, 246)

    if is_moving:
        if direction == 1:
            player_running_img.clip_draw(frame * 100, 100, 100, 100, x, 90)
            x += 5  # 오른쪽으로 이동 (속도 조절)
        else:
            player_running_img.clip_draw(frame * 100, 0, 100, 100, x, 90)
            x -= 5  # 왼쪽으로 이동 (속도 조절)

        frame = (frame + 1) % 15
    else:
        if direction == 1:
            player_idle_img.clip_draw(frame2 * 100, 100, 100, 100, x, 90)
        else:
            player_idle_img.clip_draw(frame2 * 100, 0, 100, 100, x, 90)

        frame2 = (frame2 + 1) % 4

    # 캔버스 경계 처리
    x = clamp(50, x, 800 - 50)

    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()
