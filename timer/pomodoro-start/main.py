from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    time_label.configure(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    check_mark.configure(text='')
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps % 8 ==0:
        count_down(long_break_sec)
        time_label.configure(text='Break')
    elif reps % 2 ==0:
        count_down(short_break_sec)
        time_label.configure(text='Break')
    else:
        count_down(work_sec)
        time_label.configure(text='Work', fg='red')
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count % 60
    if count_sec<10:
        count_sec=f'0{count_sec}'

    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count>0:
        global timer
        timer= window.after(1000,count_down,count -1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="√"
        check_mark.configure(text=f'{mark}')

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('Pomodoro')
window['bg']=PINK
window.configure(padx=100,pady=50)



check_mark='√'
canvas=Canvas(width=200, heigh=224,bg=PINK,highlightthickness=0)
tomato_img=PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text=canvas.create_text(100,135, text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1, row=1)


time_label=Label(text='TIMER', fg=GREEN, font=(FONT_NAME,80,'bold'),bg=PINK,highlightthickness=0)
time_label.grid(column=1,row=0)



button_start=Button(text='Start', highlightbackground=PINK, fg= 'black', highlightthickness=0, command=start_timer)
button_start.grid(column=0,row=2)

button_reset=Button(text='Reset', highlightbackground=PINK,fg='black', highlightthickness=0, command=reset)
button_reset.grid(column=2,row=2)

check_mark=Label(fg=GREEN, bg=PINK, font=(FONT_NAME, 30,'bold'))
check_mark.grid(column=1,row=3)

window.mainloop()