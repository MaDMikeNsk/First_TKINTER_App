from tkinter import *

parent = Tk()
parent.geometry('400x400')


def push_button(direction):
    global state, frames_list
    if 0 <= state + direction <= 5:
        frames_list[state].grid_forget()
        state += direction
        frames_list[state].grid(row=0, column=0, columnspan=2)


# Creating 6 frames with labels on it
frames_list = []
for i in range(6):
    frame = Frame(parent, height=200, width=400, bg='blue') #Why not blue????????????????????????????
    label = Label(frame, text=f'->>{i}').grid(row=0, column=0, columnspan=2)
    frames_list.append(frame)

backward = Button(parent, text="<<<---", padx=50, pady=50, command=lambda: push_button(-1)).grid(row=1, column=0)
forward = Button(parent, text="--->>>", padx=50, pady=50, command=lambda: push_button(1)).grid(row=1, column=1)

state = 0
frames_list[state].grid(row=0, column=0, columnspan=2)

parent.mainloop()
