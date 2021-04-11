from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
time = None
times = 0
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    # after we want stop count we need to use cancel and put var window.after
    window.after_cancel(time)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text='')
    global times
    times = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_count():
    global times
    times += 1
    if times % 2 == 0:
        if times != 8:
            count_down(SHORT_BREAK_MIN * 60)
            timer.config(text="Break", fg=RED)
        else:
            count_down(LONG_BREAK_MIN * 60)
            timer.config(text="Break", fg=PINK)
    elif times % 2 != 0:
        count_down(WORK_MIN * 60)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

import math


def count_down(count):
    min_text = math.floor(count / 60)
    sec = count % 60
    canvas.itemconfig(timer_text, text=f"{min_text}:{sec}")
    if sec < 10 and sec == 0:
        sec = f"0{sec}"
    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        start_count()
        # add check mark after count to zero
        check_number = ''
        work_sessions = math.floor(times/2)
        for _ in range(work_sessions):
            check_number += '✓'
        check.config(text=check_number)

# when it come to zero, start it again

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer.grid(column=1, row=0)

# create canvas in original window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_Img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_Img)
timer_text = canvas.create_text(100, 120, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
# save canvas create to var
canvas.grid(column=1, row=1)


start = Button(text='Start', highlightthickness=0, command=start_count)
start.grid(column=0, row=2)

Reset = Button(text='Reset', highlightthickness=0, command=reset_timer)
Reset.grid(column=2, row=2)

check = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check.grid(column=1, row=3)

window.mainloop()
