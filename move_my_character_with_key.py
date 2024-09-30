from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('Sprite_Sheet.png')

dirx = 0
diry = 0

def handle_events():
    global running
    global dirx
    global diry

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1

running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hide_cursor()

frame_width = 80
frame_y = 80
frame_height = 80
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    if dirx == 0 and diry == 0:
       character.clip_draw(frame * frame_width, frame_y * 3 + 64, frame_width, frame_height, x, y)
    elif dirx == -1:
        character.clip_composite_draw(frame * frame_width, frame_y * 11 + 64, frame_width, frame_height, 0, 'h', x, y, 80, 80)
    elif dirx == 1:
        character.clip_draw(frame * frame_width, frame_y * 11 + 64, frame_width, frame_height, x, y)
    elif diry == -1:
        character.clip_draw(frame * frame_width + frame_width * 6, frame_y * 6 + 64, frame_width, frame_height, x, y)
    elif diry == 1:
        character.clip_draw(frame * frame_width, frame_y * 6 + 64, frame_width, frame_height, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 6
    x += dirx * 5
    y += diry * 5
    delay(0.1)

close_canvas()