#파이썬을 이용한 액션 게임  
IDE : vs code  
언어 : python 3.11.1  
서적 : 파이썬으로 배우는 게임 개발 실전편  

게임 규칙
1. 방향키를 사용해 펭귄을 상하좌우로 이동
2. 사탕을 모두 먹으면 스테이지 클리어
3. 레드에게 닳으면 게임 오버

파이썬 문법  
1. 윈도우 변경 불가
```py
root.resizable(False, False) #윈도우 창의 가로, 세로를 변경 불가로 설정
canvas = tkinter.Canvas(width=720, height=540) #창 사이즈
```
2. 케릭터 움직이는 함수
```py
#ANIMATION[]는 걸음을 표현하기 위해 넣은 번호를 넣은 리스트
ANIMATION = [0,1,0,2]
def move_penpen():  # 펜펜 움직이기
    global pen_x, pen_y, pen_d, pen_a
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
    #펜펜 에니메이션 번호 계산        
    #각 방향마다 3개의 이미지를 사용하기에 *3 
    #tmr 값은 프레임 마다 증가하여  tmr % 4는 0>1>2>3> ... 을 반복한다
    #ANIMATION[tmr % 4]은 인덱스 순서에 의해 0>1>0>2>....을 반복한다.
    pen_a = pen_d * 3 + ANIMATION[tmr % 4] 
```
3. 2번 함수를 게임 화면 함수에 추가한다.
```py
def draw_screen():  # 게임 화면 그리기
    canvas.delete("SCREEN") #먼저 화면 삭제
    for y in range(9): #미로 그리기
        for x in range(12):
            canvas.create_image(x * 60 + 30, y * 60 + 30, image=img_bg[map_data[y][x]], tag="SCREEN")
    canvas.create_image(pen_x, pen_y, image=img_pen[pen_a], tag="SCREEN") #pen_a #펜펜의 이미지 번호
    draw_txt("SCORE " +  str(score), 200, 30, 30, "white") #점수 표시
```
4. 점수 표시 함수
```py
def draw_txt(txt, x, y, siz, col):
    fnt = ("Times New Roman", siz, "bold")
    canvas.create_text(x+2, y+2, text=txt, fill="black",font=fnt, tag="SCREEN") #문자열 그림자 효과
    canvas.create_text(x, y, text=txt, fill=col,font=fnt, tag="SCREEN") #지정한 색으로 문자 표시
```
5. 사탕 처리 함수
```py
if map_data[my][mx] == 3: #사탕에 닿았나?
    score = score + 100 #사탕 1개당 100점 부여
    map_data[my][mx] = 2 #사탕을 일반 바닥으로 변경
    candy = candy - 1 #사탕 갯수 처리
```
6. 게임 플레이 규칙
```py
if idx == 0:#타이틀 화면
    canvas.create_image(360, 200, image=img_title, tag="SCREEN")
    if tmr % 10 < 5:
        draw_txt("Press SPACE !", 360, 380, 30, "yellow")
        if key == "space": #스페이스 입력시 시작
            score = 0 
            set_stage()
            set_chara_pos()
            idx = 1
if idx == 1: #게임 플레이
    move_penpen()
    move_enemy()
    if candy == 0: #캔디를 다 먹으면 4번으로 이동하여 게임 종료
        idx = 4 
        tmr = 0
if idx == 2: #적과 충돌!
    draw_txt("GAME OVER", 360, 270, 40, "red")
    if tmr == 50: #5초 뒤 타이틀 화면으로 이동
        idx = 0
if idx == 4: #스테이지 클리어.
    draw_txt("STAGE CLEAR", 360, 270, 40, "pink")
    if tmr == 50: #5초 뒤 타이틀 화면으로 이동
        idx = 0
```
7. 적과의 충돌 계산
```py
#이미지 크기는 60 픽셀이지만 40으로 설정한 이유 
#사용자 눈에 보이기에 접촉한 것이 확인 되어야 하기에
if abs(red_x - pen_x) <= 40 and abs(red_y - pen_y) <= 40: 
        idx = 2
        tmr = 0
```
8. 맵 에디터 핵심 함수
```py
#두 개의 bind()명령으로 마우스로 그리듯 맵을 그릴 수 있다.
cvs_bg.bind("<Button-1>", set_map) #클릭시 실행할 함수 지정
cvs_bg.bind("<B1-Motion>", set_map) #클릭 + 포인터 이동시 실행할 함수 지정
```