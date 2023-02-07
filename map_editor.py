import tkinter

chip = 0 #맵 칩번호 변수
map_data = [] #미로 데이터를 대입할 리스트
for i in range(9):#리스트 초기화
    map_data.append([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

#미로 그리는 함수
def draw_map():
    cvs_bg.delete("BG") #모든 이미지 삭제
    for y in range(9):
        for x in range(12):
            cvs_bg.create_image(60 * x + 30, 60 * y + 30, image=img[map_data[y][x]], tag="BG") #맵 칩으로 미로 그림

#미로 내 칩 배치 함수
def set_map(e): 
    x = int(e.x / 60) #미로 내 인덱스 계산
    y = int(e.y / 60) #미로 내 인덱스 계산
    #클릭한 위치가 미로 범위라면...
    if 0 <= x and x <= 11 and 0 <= y and y <= 8: 
        map_data[y][x] = chip #리스트에 chip값 대입
        draw_map() #미로 그리기

#선택용 맵 칩 표시 함수
def draw_chip(): 
    cvs_chip.delete("CHIP") #모든 이미지 삭제
    for i in range(len(img)):
        cvs_chip.create_image(30, 30 + i * 60, image=img[i], tag="CHIP") #맵 칩 그리기
    #선택한 칩에 테두리 표시
    cvs_chip.create_rectangle(4, 4 + 60 * chip, 57, 57 + 60 * chip, outline="red", width=3, tag="CHIP")

#맵 칩 선택 함수
def select_chip(e):
    global chip
    y = int(e.y / 60) #y좌표에서 칩 번호 계산
    if 0 <= y and y < len(img): #클릭한 위치가 맵 칩이라면..
        chip = y #맵 칩 번호 대입
        draw_chip() #선택용 칩 그림

def put_data():
    c = 0
    text.delete("1.0", "end")
    for y in range(9):
        for x in range(12):
            text.insert("end", str(map_data[y][x])+ ",")
            if map_data[y][x] == 3:
                c = c+1
        text.insert("end", "\n")
    text.insert("end", "candy = "+str(c))

root = tkinter.Tk() #윈도우 객체 생성
root.geometry("820x760") #크기 기정
root.title("맵 에디터") #타이틀 지정
cvs_bg = tkinter.Canvas(width=720, height=540, bg="white") #캔버스 컴포넌트 생성
cvs_bg.place(x=10, y=10) #캔버스 배치
cvs_bg.bind("<Button-1>", set_map) #클릭시 실행할 함수 지정
cvs_bg.bind("<B1-Motion>", set_map) #클릭 + 포인터 이동시 실행할 함수 지정
cvs_chip = tkinter.Canvas(width=60, height=540, bg="black") #캔버스 컴포넌트 생성(칩 생성용)
cvs_chip.place(x=740, y=10)
cvs_chip.bind("<Button-1>", select_chip)
text = tkinter.Text(width=40, height=14)
text.place(x=10, y=560)
btn = tkinter.Button(text="데이터 출력", font=("Times New Roman", 16), fg="blue", command=put_data)
btn.place(x=400, y=560)
img = [
    tkinter.PhotoImage(file="image_penpen/chip00.png"),
    tkinter.PhotoImage(file="image_penpen/chip01.png"),
    tkinter.PhotoImage(file="image_penpen/chip02.png"),
    tkinter.PhotoImage(file="image_penpen/chip03.png")
]
draw_map()
draw_chip()
root.mainloop()
