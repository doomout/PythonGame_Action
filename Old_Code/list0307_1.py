import tkinter
import random

# 키 입력
key = ""
koff = False
def key_down(e): #키를 눌렀을 때
    global key, koff
    key = e.keysym
    koff = False

def key_up(e): #키를 눌렀다 땟을 때
    #Win용
    global koff
    key = "" 
    #Mac 용
    #global koff
    #koff = True
    

#캐릭터 방향 정의 변수들
DIR_UP = 0 
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3
ANIMATION = [0,1,0,2] #에니메이션 번호 정의

idx = 0 #인덱스
tmr = 0 #타이머
score = 0 #점수
candy = 0 #각 스테이지에 있는 사탕수

pen_x = 0
pen_y = 0
pen_d = 0 #펜펜의 방향
pen_a = 0 #펜펜의 이미지 번호

red_x = 0
red_y = 0
red_d = 0
red_a = 0

map_data = []

def set_stage():
    global map_data, candy
    map_data = [
        [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 0],
        [0, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 0],
        [0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0],
        [0, 3, 2, 2, 3, 0, 0, 3, 2, 2, 3, 0],
        [0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0],
        [0, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 0],
        [0, 2, 3, 3, 2, 0, 0, 2, 3, 3, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    candy = 32

def set_chara_pos():
    global pen_x, pen_y, pen_d, pen_a
    global red_x, red_y, red_d, red_a
    pen_x = 90
    pen_y = 90
    pen_d = DIR_DOWN
    pen_a = 3
    red_x = 630
    red_y = 450
    red_d = DIR_DOWN
    red_a = 3

def draw_txt(txt, x, y, siz, col):
    fnt = ("Times New Roman", siz, "bold")
    canvas.create_text(x+2, y+2, text=txt, fill="black",font=fnt, tag="SCREEN") #문자열 그림자 효과
    canvas.create_text(x, y, text=txt, fill=col,font=fnt, tag="SCREEN") #지정한 색으로 문자 표시

def draw_screen():  # 게임 화면 그리기
    canvas.delete("SCREEN") #먼저 화면 삭제
    for y in range(9): #미로 그리기
        for x in range(12):
            canvas.create_image(x * 60 + 30, y * 60 + 30, image=img_bg[map_data[y][x]], tag="SCREEN")
    canvas.create_image(pen_x, pen_y, image=img_pen[pen_a], tag="SCREEN") #펜펜 표시
    canvas.create_image(red_x, red_y, image=img_red[red_a], tag="SCREEN") #레드 표시
    draw_txt("SCORE " +  str(score), 200, 30, 30, "white") #점수 표시

def check_wall(cx, cy, di, dot):  # 각 방향에 벽 존재 여부 확인
    chk = False
    if di == DIR_UP:
        mx = int((cx - 30) / 60)
        my = int((cy - 30 - dot) / 60)
        if map_data[my][mx] <= 1:  # 좌상
            chk = True
        mx = int((cx + 29) / 60)
        if map_data[my][mx] <= 1:  # 우상
            chk = True
    if di == DIR_DOWN:
        mx = int((cx - 30) / 60)
        my = int((cy + 29 + dot) / 60)
        if map_data[my][mx] <= 1:  # 좌하
            chk = True
        mx = int((cx + 29) / 60)
        if map_data[my][mx] <= 1:  # 우하
            chk = True
    if di == DIR_LEFT:
        mx = int((cx - 30 - dot) / 60)
        my = int((cy - 30) / 60)
        if map_data[my][mx] <= 1:  # 좌상
            chk = True
        my = int((cy + 29) / 60)
        if map_data[my][mx] <= 1:  # 좌하
            chk = True
    if di == DIR_RIGHT:
        mx = int((cx + 29 + dot) / 60)
        my = int((cy - 30) / 60)
        if map_data[my][mx] <= 1:  # 우상
            chk = True
        my = int((cy + 29) / 60)
        if map_data[my][mx] <= 1:  # 우하
            chk = True
    return chk

def move_penpen():  # 펜펜 움직이기
    global pen_x, pen_y, pen_d, pen_a, score, candy
    if key == "Up":
        pen_d = DIR_UP
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y = pen_y - 20
    if key == "Down":
        pen_d = DIR_DOWN
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y = pen_y + 20
    if key == "Left":
        pen_d = DIR_LEFT
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x = pen_x - 20
    if key == "Right":
        pen_d = DIR_RIGHT
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x = pen_x + 20
            
    pen_a = pen_d * 3 + ANIMATION[tmr % 4] #펜펜 에니메이션 번호 계산
    mx = int(pen_x / 60)
    my = int(pen_y / 60)
    if map_data[my][mx] == 3: #사탕에 닿았나?
        score = score + 100
        map_data[my][mx] = 2 #사탕 삭제
        candy = candy - 1
        
#레드 움직이기
def move_enemy():
    global red_x, red_y, red_d, red_a, idx, tmr
    speed = 10
    if red_x % 60 == 30 and red_y % 60 == 30:
        red_d = random.randint(0,6)
        if red_d >= 4: #펜펜 쫒아다니기
            if pen_y < red_y:
                red_d  = DIR_UP
            if pen_y > red_y:
                red_d = DIR_DOWN
            if pen_x < red_x:
                red_d = DIR_LEFT
            if pen_x > red_x:
                red_d = DIR_RIGHT
    if red_d == DIR_UP:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y - speed
    if red_d == DIR_DOWN:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y + speed
    if red_d == DIR_LEFT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x - speed
    if red_d == DIR_RIGHT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x + speed
    
    red_a = red_d * 3 + ANIMATION[tmr % 4]
    #펜펜과 레드가 접촉했다면.
    if abs(red_x - pen_x) <= 40 and abs(red_y - pen_y) <= 40:
        idx = 2
        tmr = 0

def main():  # 메인 루프
    global key, koff, tmr, idx, score
    tmr = tmr + 1
    draw_screen()
    if idx == 0:#타이틀 화면
        canvas.create_image(360, 200, image=img_title, tag="SCREEN")
        if tmr % 10 < 5:
            draw_txt("Press SPACE !", 360, 380, 30, "yellow")
            if key == "space":
                score = 0
                set_stage()
                set_chara_pos()
                idx = 1
    if idx == 1: #게임 플레이
        move_penpen()
        move_enemy()
        if candy == 0:
            idx = 4
            tmr = 0
    if idx == 2: #적과 충돌!
        draw_txt("GAME OVER", 360, 270, 40, "red")
        if tmr == 50:
            idx = 0
    if idx == 4: #스테이지 클리어.
        draw_txt("STAGE CLEAR", 360, 270, 40, "pink")
        if tmr == 50:
            idx = 0
    root.after(100, main) #100 밀리초마다 반복


root = tkinter.Tk()

img_bg = [
    tkinter.PhotoImage(file="image_penpen/chip00.png"),
    tkinter.PhotoImage(file="image_penpen/chip01.png"),
    tkinter.PhotoImage(file="image_penpen/chip02.png"),
    tkinter.PhotoImage(file="image_penpen/chip03.png")
]

img_pen = [
    tkinter.PhotoImage(file="image_penpen/pen00.png"),
    tkinter.PhotoImage(file="image_penpen/pen01.png"),
    tkinter.PhotoImage(file="image_penpen/pen02.png"),
    tkinter.PhotoImage(file="image_penpen/pen03.png"),
    tkinter.PhotoImage(file="image_penpen/pen04.png"),
    tkinter.PhotoImage(file="image_penpen/pen05.png"),
    tkinter.PhotoImage(file="image_penpen/pen06.png"),
    tkinter.PhotoImage(file="image_penpen/pen07.png"),
    tkinter.PhotoImage(file="image_penpen/pen08.png"),
    tkinter.PhotoImage(file="image_penpen/pen09.png"),
    tkinter.PhotoImage(file="image_penpen/pen10.png"),
    tkinter.PhotoImage(file="image_penpen/pen11.png")
]

img_red = [
    tkinter.PhotoImage(file="image_penpen/red00.png"),
    tkinter.PhotoImage(file="image_penpen/red01.png"),
    tkinter.PhotoImage(file="image_penpen/red02.png"),
    tkinter.PhotoImage(file="image_penpen/red03.png"),
    tkinter.PhotoImage(file="image_penpen/red04.png"),
    tkinter.PhotoImage(file="image_penpen/red05.png"),
    tkinter.PhotoImage(file="image_penpen/red06.png"),
    tkinter.PhotoImage(file="image_penpen/red07.png"),
    tkinter.PhotoImage(file="image_penpen/red08.png"),
    tkinter.PhotoImage(file="image_penpen/red09.png"),
    tkinter.PhotoImage(file="image_penpen/red10.png"),
    tkinter.PhotoImage(file="image_penpen/red11.png")
]
img_title = tkinter.PhotoImage(file="image_penpen/title.png")

root.title("아슬아슬 펭귄 미로")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=720, height=540)
canvas.pack()
set_stage() #각 캐릭터 데이터 설정
set_chara_pos() #각 캐릭터 시작 위치로 이동
main()
root.mainloop()
