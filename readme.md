#파이썬을 이용한 액션 게임  
IDE : vs code  
언어 : python 3.11.1  
서적 : 파이썬으로 배우는 게임 개발 실전편  

게임 규칙
1. 방향키를 사용해 펭귄을 상하좌우로 이동
2. 사탕을 모두 먹으면 스테이지 클리어
3. 레드에게 닳으면 충격 받음
4. 레드에게 닿으면 펭귄 수명이 -1, 수명이 0이 되면 게임 종료
5. 스테이지 진행 중 새로운 적이 추가
6. 모든 스테이지 클리어 하면 엔딩 표시

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
```