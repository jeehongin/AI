#1
import tkinter as tk #Tkinter를 가져와 tkiner 모듈을 tk로 줄여서 사용함

def say_hello(): #say_hello라는 함수를 정의함
    label.config(text="Hello, World!") #호출될 때 레이블의 텍스트를 "Hello, World!"로 전환

root=tk.Tk() #기본 윈도우창 생성
button=tk.Button(root,text="Click Me",command=say_hello) #root 창 안에 들어갈 버튼 생성
button.pack() #버튼을 화면에 배치
label=tk.Label(root,text="") #창 안에 들어갈 레이블을 만듦
label.pack() #레이블을 화면에 배치
root.mainloop() #루프 실행

#2
import tkinter as tk

def greet(): #greet 함수 정의
    name = entry.get() #사용자가 입력한 이름을 호출
    label.config(text=f"Hello, {name}") #레이블의 텍스트를 "hello, {name}" 형식으로 전환

root = tk.Tk()
entry = tk.Entry(root) #텍스트 입력창 생성
entry.pack() #화면에 배치
button = tk.Button(root, text="Greet", command=greet) #버튼 생성
button.pack() #버튼 화면에 배치
label = tk.Label(root, text="")
label.pack()
root.mainloop()

#3
import tkinter as tk

def add(): #add 함수 정의
    result = int(entry1.get()) + int(entry2.get()) #entry1 과 entry2에서 값을 가져와 정수로 변환하고 더하여 result값으로 저장
    label.config(text=f"Result: {result}") #결과를 표시

root = tk.Tk()
entry1 = tk.Entry(root) #첫 번째 입력창 생성
entry1.pack() #배치
entry2 = tk.Entry(root) #두 번째 입력창 생성
entry2.pack() #배치
button = tk.Button(root, text="Add", command=add) #버튼 생성
button.pack() #버튼 배치
label = tk.Label(root, text="")
label.pack()
root.mainloop()

#4
import tkinter as tk

def show_selection(): #show 버튼을 눌렀을 때 실행되는 함수 show_selection
    selections = [] #빈 리스트 생성
    if var1.get(): selections.append("Option 1") #var1.get()이 참이면 "Option 1"리스트에 추가
    if var2.get(): selections.append("Option 2") #var2.get()이 참이면 "Option 2"리스트에 추가
    label.config(text=", ".join(selections)) #레이블의 텍스트를 ","로 구분하여 설정

root = tk.Tk()
var1 = tk.BooleanVar() #체크 여부를 저장할 BooleanVar 객체 생성
var2 = tk.BooleanVar() #체크 여부를 저장할 BooleanVar 객체 생성
tk.Checkbutton(root, text="Option 1", variable=var1).pack() #체크버튼 생성 및 var1 변수와 연결
tk.Checkbutton(root, text="Option 2", variable=var2).pack() #체크버튼 생성 및 var2 변수와 연결
tk.Button(root, text="Show", command=show_selection).pack() #클릭하면 show_selection 함수가 실행되는 버튼 생성
label = tk.Label(root, text="")
label.pack()
root.mainloop()

#5
import tkinter as tk

def change_color(): #버튼을 선택할 때 실행되는 change_color 함수 정의
    root.configure(bg=color.get()) #창의 배경색을 선택된 색상으로 변경

root = tk.Tk()
color = tk.StringVar() #선택된 값을 저장할 변수 생성
tk.Radiobutton(root, text="Red", variable=color, value="red", command=change_color).pack() #Red 레이블의 버튼 생성, 선택 시 color 변수 값이 "red"로 설정되고 배경이 빨간색으로 변경
tk.Radiobutton(root, text="Blue", variable=color, value="blue", command=change_color).pack() #Blue 레이블의 버튼 생성, 선택 시 color 변수 값이 "red"로 설정되고 배경이 빨간색으로 변경
tk.Radiobutton(root, text="Green", variable=color, value="green", command=change_color).pack() #Green 레이블의 버튼 생성, 선택 시 color 변수 값이 "red"로 설정되고 배경이 빨간색으로 변경
root.mainloop()

#6
import tkinter as tk

def resize(val): #슬라이더 값에 따라 호출되는 함수 정의
    label.config(font=("Arial", int(val))) #값을 정수로 바꾸고 그에 따라 폰트 크기를 변경

root = tk.Tk()
scale = tk.Scale(root, from_=10, to=40, orient="horizontal", command=resize) #범위가 10~40인 Scale 위젯을 생성
scale.pack()
label = tk.Label(root, text="Resizable Text") #화면에 텍스트 표시
label.pack()
root.mainloop()

#7
import tkinter as tk

def show_fruit(event): #리스트박스에서 항목을 선택했을 때 호출되는 함수 show_fruit 정의
    selection = listbox.get(listbox.curselection()) #리스트박스에서 선택된 항목의 텍스트를 가져옴
    label.config(text=f"Selected: {selection}") #레이블의 텍스트를 선택한 과일 이름으로 설정

root = tk.Tk()
listbox = tk.Listbox(root) #화면에 리스트박스 위젯 생성
for fruit in ["Apple", "Banana", "Cherry"]: #과일 이름에 대한 반복문 실행
    listbox.insert(tk.END, fruit) #리스트박스 끝에 현재 과일 항목 추가
listbox.pack() #리스트박스 화면에 배치
listbox.bind("<<ListboxSelect>>", show_fruit) #리스트박스 항목이 선택될 때 show_fruit 함수가 호출되도록 함
label = tk.Label(root, text="") #텍스트가 빈 레이블 생성
label.pack()
root.mainloop()

#8
import tkinter as tk

def show_message(msg): #메시지를 레이블에 표시하는 함수 show_message를 정의
    label.config(text=msg) #전달된 메시지로 레이블의 텍스트를 변경

root = tk.Tk()
menu = tk.Menu(root) #창에 메뉴를 생성
file_menu = tk.Menu(menu, tearoff=0) #File 이라는 하위메뉴 생성 및 테어오프 비활성화
file_menu.add_command(label="Open", command=lambda: show_message("Open clicked")) #'Open' 메뉴를 추가하고 클릭 시 "Open clicked" 메시지를 표시
menu.add_cascade(label="File", menu=file_menu) #'File'이라는 레이블로 file_menu를 추가
help_menu = tk.Menu(menu, tearoff=0) #File 이라는 하위메뉴 생성 및 테어오프 비활성화
help_menu.add_command(label="About", command=lambda: show_message("About clicked")) #'About' 메뉴를 추가하고 클릭 시 "About clicked" 메시지를 표시
menu.add_cascade(label="Help", menu=help_menu) #'Help'라는 레이블로 help_menu를 추가
root.config(menu=menu) #메뉴바 설정
label = tk.Label(root, text="")
label.pack()
root.mainloop()

#9
import tkinter as tk

def save_file(): #텍스트를 파일로 저장하는 함수 save_file을 정의
    with open("note.txt", "w") as f: #note.txt 라는 파일을 쓰기모드로 연다
        f.write(text.get("1.0", tk.END)) #텍스트 위젯의 모든 내용을 파일에 씀

root = tk.Tk()
text = tk.Text(root)
text.pack()
button = tk.Button(root, text="Save", command=save_file) #"Save"라는 텍스트가 표시되고 클릭 시 save_file 함수를 실행하는 버튼 생성
button.pack()
root.mainloop()

#10
import tkinter as tk
import time #time 모듈 불러오기

def update_time(): #현재 시간을 화면에 갱신하는 함수 update_time 정의
    current = time.strftime("%H:%M:%S") #현재 시간을 "시:분:초" 형식으로 전환
    label.config(text=current) #레이블의 텍스트를 현재 시간으로 설정
    root.after(1000, update_time) #1초 후에 함수를 다시 실행하도록 예약

root = tk.Tk()
label = tk.Label(root, font=("Arial", 24)) #폰트 크기를 설정한 텍스트 레이블 생성
label.pack()
update_time() #프로그램 시작 시 시간을 표시 및 이후 자동으로 갱신되도록 update_time 호출
root.mainloop()


