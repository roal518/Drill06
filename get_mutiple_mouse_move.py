from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
IDLE_character = load_image('Woodcutter_idle.png')
MOVE_character = load_image('Woodcutter_run.png')
Arrow_cursur = load_image('hand_arrow.png')

xlist = []
ylist = []
mouseX, mouseY = TUK_WIDTH//2, TUK_HEIGHT//2
nowX, nowY = TUK_WIDTH//2, TUK_HEIGHT//2
running = True
x, y = 0, 0
def keyboard_events():
    global running
    for keyevent in get_events():
        if keyevent.type == SDL_KEYDOWN:
            if keyevent.key == SDLK_ESCAPE:
                running = False
def handle_events():
    global mouseX, mouseY
    global nowX, nowY
    for event in get_events():
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            xlist.append(event.x)
            ylist.append(TUK_HEIGHT - event.y - 1)
def move_character():
    global nowX, nowY, mouseX, mouseY, i, x, y
    global moveonce
    i += 2
    if moveonce:
        if x != mouseX and y != mouseY:
            t = i / 1000
            x = (1 - t) * nowX + t * mouseX
            y = (1 - t) * nowY + t * mouseY
            if nowX < mouseX:
                MOVE_character.clip_draw(runframe * 100, 0, 100, 100, x, y)
            else:
                MOVE_character.clip_composite_draw(runframe * 100, 0, 100, 100,0,'h', x, y,100,100)
        else:
            moveonce = False
            nowX, nowY = mouseX, mouseY
            if xlist:
                xlist.pop(0)
                ylist.pop(0)
    else :
        if not xlist:
            IDLE_character.clip_draw(idleframe * 100, 0, 100, 100, x, y)
        else:
            mouseX = xlist[0]
            mouseY = ylist[0]
            moveonce = True
            i = 0
def draw_cursur():
    for n in range(len(xlist)):
        Arrow_cursur.draw(xlist[n], ylist[n])
moveonce = True
moving = True
i = 0
runframe = 0
idleframe = 0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    draw_cursur()
    move_character()
    keyboard_events()
    handle_events()
    update_canvas()
    runframe = (runframe + 5) % 6
    idleframe = (idleframe + 1) % 4
close_canvas()
#aaaa