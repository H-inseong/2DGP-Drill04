from pico2d import *


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

dirx = 0

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
x = 800 // 2
frame = 0


while running:
    clear_canvas()
    grass.draw(400,30)
    if dirx != -1:
       character.clip_draw(frame*100, 100, 100, 100, x, 90)
    elif dirx == -1:
        character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', x, 90, 100, 100)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dirx * 5
    delay(0.05)

close_canvas()