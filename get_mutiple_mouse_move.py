from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280,1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
IDLE_character = load_image('Woodcutter_idle.png')
MOVE_character = load_image('Woodcutter_run.png')
Arrow_cursur = load_image('hand_arrow.png')

xlist = [TUK_WIDTH // 2]
ylist = [TUK_HEIGHT // 2]
running = True
moving = False
isClicked = False
mouseX, mouseY = TUK_WIDTH//2, TUK_HEIGHT//2
nowX, nowY = TUK_WIDTH//2, TUK_HEIGHT//2
x, y = TUK_WIDTH//2, TUK_HEIGHT//2
def keyboard_events():
    global running
    keyevents = get_events()
    for keyevent in keyevents:
        if keyevent.type == SDL_KEYDOWN:
            if keyevent.key == SDLK_ESCAPE:
                running = False
def handle_events():
    global mouseX,mouseY,isClicked
    global nowX,nowY
    global i
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == 1:
                print("clicked")
                isClicked =True
                nowX, nowY = mouseX, mouseY
                xlist.append(event.x)
                ylist.append(TUK_HEIGHT -1 -event.y)
                print(f"{xlist}")
                print(f"{ylist}")
                mouseX = xlist[1]
                mouseY = ylist[1]
        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == 1:
                isClicked = False
def move_character():
    global x,y,nowX,nowY,i
    global moving
    if(x == mouseX and y == mouseY):
        moving = False
        nowX = xlist.pop(0)
        nowY = ylist.pop(0)
    elif( x != mouseX and y != mouseY):
        moving = True
def draw_cursur():
    for n in range(0,len(xlist),1):
        Arrow_cursur.draw(xlist[n],ylist[n])


runframe = 0
idleframe = 0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    draw_cursur()
    keyboard_events()
    handle_events()
    update_canvas()

# 계획:: 리스트를 기본적으로 사용
# 일단 리스트를 좀 써보면서 이해를 한다.
# x,y좌표를 일단 따로 받고 나중에 합쳐 보자
# 마우스 좌표 받기 자체는 쉬웠다.
# 어제 했던 내용에 조금씩 붙이면 될듯하다.
# 입력을 받고 append로 삽입 pop으로 관리한다.
# 까다로운 점은 마우스 좌표를 받고 여러개의 그림을 남겨놓는게 아닐까

