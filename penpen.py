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
BLINK = ["#fff","#ffc","#ff8","#fe4","#ff8","#ffc"] #깜박거림용 색 지정 리스트

idx = 0 #인덱스
tmr = 0 #타이머
stage = 1 #스테이지 수
score = 0 #점수
nokori = 3 #생명력
candy = 0 #각 스테이지에 있는 사탕수

pen_x = 0
pen_y = 0
pen_d = 0 #펜펜의 방향
pen_a = 0 #펜펜의 이미지 번호

red_x = 0
red_y = 0
red_d = 0
red_a = 0
red_sx = 0 #레드 시작 위치 x좌표
red_sy = 0 #레드 시작 위치 y좌표

kuma_x = 0
kuma_y = 0
kuma_d = 0 #쿠마곤의 방향
kuma_a = 0 #쿠마곤 이미지 번호
kuma_sx = 0 #시작위치 x 좌표
kuma_sy = 0 #시작위치 y 좌표
kuma_sd = 0 #시작시 쿠마곤 방향

map_data = [] #맵 리스트

def set_stage(): #스테이지 데이터 설정
    global map_data, candy
    global red_sx, red_sy
    global kuma_sx, kuma_sy ,kuma_sd
    if stage == 1:
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
        red_sx = 630
        red_sy = 450
        kuma_sd = -1 #쿠마곤 없음
    if stage == 2:
        map_data = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 0],
            [0, 3, 3, 0, 2, 1, 1, 2, 0, 3, 3, 0],
            [0, 3, 3, 1, 3, 3, 3, 3, 1, 3, 3, 0],
            [0, 2, 1, 3, 3, 3, 3, 3, 3, 1, 2, 0],
            [0, 3, 3, 0, 3, 3, 3, 3, 0, 3, 3, 0],
            [0, 3, 3, 1, 2, 1, 1, 2, 1, 3, 3, 0],
            [0, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 38
        red_sx = 630
        red_sy = 90
        kuma_sx = 330
        kuma_sy = 270
        kuma_sd = DIR_LEFT
    if stage == 3:
        map_data = [
            [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 1, 3, 1, 2, 2, 3, 3, 3, 3, 0],
            [0, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 0],
            [0, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 0],
            [0, 1, 1, 2, 0, 2, 2, 0, 1, 2, 2, 0],
            [0, 3, 3, 3, 1, 1, 1, 0, 3, 3, 3, 0],
            [0, 3, 3, 3, 2, 2, 2, 3, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 23
        red_sx = 630
        red_sy = 450
        kuma_sx = 330
        kuma_sy = 270
        kuma_sd = DIR_RIGHT
    if stage == 4:
        map_data = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 3, 0, 3, 3, 1, 3, 0, 3, 0, 3, 0],
            [0, 3, 1, 0, 3, 3, 3, 0, 3, 1, 3, 0],
            [0, 3, 3, 0, 1, 1, 1, 0, 3, 3, 3, 0],
            [0, 3, 0, 1, 3, 3, 3, 1, 3, 1, 1, 0],
            [0, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 50
        red_sx = 150
        red_sy = 270
        kuma_sx = 510
        kuma_sy = 270
        kuma_sd = DIR_UP

    if stage == 5:
        map_data = [
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 2, 0, 3, 0, 1, 3, 3, 1, 0, 3, 0],
            [0, 2, 0, 3, 0, 3, 3, 3, 3, 0, 3, 0],
            [0, 2, 1, 3, 1, 1, 3, 3, 1, 1, 3, 0],
            [0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        candy = 40
        red_sx = 630
        red_sy = 450
        kuma_sx = 390
        kuma_sy = 210
        kuma_sd = DIR_RIGHT

def set_chara_pos():
    global pen_x, pen_y, pen_d, pen_a
    global red_x, red_y, red_d, red_a
    global kuma_x, kuma_y ,kuma_d, kuma_a
    pen_x = 90
    pen_y = 90
    pen_d = DIR_DOWN
    pen_a = 3
    red_x = red_sx
    red_y = red_sy
    red_d = DIR_DOWN
    red_a = 3
    kuma_x = kuma_sx
    kuma_y = kuma_sy
    kuma_d = kuma_sd
    kuma_a = 0

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
    if kuma_sd != -1:
        canvas.create_image(kuma_x, kuma_y, image=img_kuma[kuma_a], tag="SCREEN") #쿠마 표시
    draw_txt("SCORE " +  str(score), 200, 30, 30, "white") #점수 표시
    draw_txt("STAGE " +  str(stage), 520, 30, 30, "lime") #스테이지 표시
    for i in range(nokori):
        canvas.create_image(60+i * 50, 500, image=img_pen[12], tag="SCREEN")

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
        
#쿠마 움직이기
def move_enemy2():
    global kuma_x, kuma_y, kuma_d, kuma_a, idx, tmr
    speed = 5
    if kuma_sd == -1:
        return
    if kuma_d == DIR_UP:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_y = kuma_y - speed
        else:
            kuma_d = DIR_DOWN
    if kuma_d == DIR_DOWN:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_y = kuma_y + speed
        else:
            kuma_d = DIR_UP
    if kuma_d == DIR_LEFT:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_x = kuma_x - speed
        else:
            kuma_d = DIR_RIGHT
    if kuma_d == DIR_RIGHT:
        if check_wall(kuma_x, kuma_y, kuma_d, speed) == False:
            kuma_x = kuma_x + speed
        else:
            kuma_d = DIR_LEFT
    kuma_a = ANIMATION[tmr % 4]
    #쿠마과 펜펜이 접촉했다면.
    if abs(kuma_x - pen_x) <= 40 and abs(kuma_y - pen_y) <= 40:
        idx = 2
        tmr = 0

def main():  # 메인 루프
    global key, koff, tmr, idx, score, stage, nokori
    tmr = tmr + 1
    draw_screen()
    if idx == 0:#타이틀 화면
        canvas.create_image(360, 200, image=img_title, tag="SCREEN")
        if tmr % 10 < 5:
            draw_txt("Press SPACE !", 360, 380, 30, "yellow")
            if key == "space":
                stage = 1
                score = 0
                nokori = 3 #수명 3으로 설정
                set_stage()
                set_chara_pos()
                idx = 1
    if idx == 1: #게임 플레이
        move_penpen()
        move_enemy()
        move_enemy2()
        if candy == 0:
            idx = 4
            tmr = 0
    if idx == 2: #적과 충돌!
        draw_txt("MISS", 360, 270, 40, "orange")
        if tmr == 1:
            nokori = nokori - 1
        if tmr == 30:
            if nokori == 0:
                idx = 3
                tmr = 0
            else:
                set_chara_pos()
                idx = 1
    if idx == 3: #게임 오버!
        draw_txt("GAME OVER", 360, 270, 40, "red")
        if tmr == 50:
            idx = 0
    if idx == 4: #스테이지 클리어.
        if stage < 5:
            draw_txt("STAGE CLEAR", 360, 270, 40, "pink")
        else:
            draw_txt("ALL STAGE CLEAR", 360, 270, 40, "violet")
        if tmr == 30:
            if stage < 5:
                stage = stage + 1
                set_stage()
                set_chara_pos()
                idx = 1
            else:
                idx = 5
                tmr = 0
    if idx == 5: #엔딩
        if tmr < 60:
            xr = 8 * tmr
            yr = 6 * tmr
            canvas.create_oval(360-xr, 270-yr, 360+xr, 270+yr, fill="black", tag="SCREEN")
        else:
            canvas.create_rectangle(0,0,720,540, fill="black", tag="SCREEN")
            canvas.create_image(360,300, image=img_ending, tag="SCREEN")
            draw_txt("Congratulations!",360,160,40,BLINK[tmr % 6])
            if tmr == 300:
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
    tkinter.PhotoImage(file="image_penpen/pen11.png"),
    tkinter.PhotoImage(file="image_penpen/pen_face.png")
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

img_kuma = [
    tkinter.PhotoImage(file="image_penpen/kuma00.png"),
    tkinter.PhotoImage(file="image_penpen/kuma01.png"),
    tkinter.PhotoImage(file="image_penpen/kuma02.png")
]
img_title = tkinter.PhotoImage(file="image_penpen/title.png")
img_ending = tkinter.PhotoImage(file="image_penpen/ending.png")

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
