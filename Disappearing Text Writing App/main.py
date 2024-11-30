from tkinter import *
from tkinter.filedialog import asksaveasfilename
import pygame

pygame.init()
pygame.mixer.init()

whoosh_sound = pygame.mixer.Sound("sounds/whoosh3.mp3")


def play_whoosh_sound():
    whoosh_sound.play()


def stop_whoosh_sound():
    whoosh_sound.stop()


def set_timer():
    global timer, timer_running, rect_id, main_timer_finished, test_seconds
    try:
        test_seconds = float(entry_minutes.get()) * 60
    except ValueError:
        entry_minutes.delete(0, END)
        entry_minutes.insert(END, '1')

    entry_minutes.config(state='disabled')
    btn_start_timer.config(state='disabled')
    timer = test_seconds
    timer_running = True
    main_timer_finished = False
    rect_id = canvas.create_rectangle(0, 0, 0, 10, fill="green")
    update_timer()


def update_timer():
    global timer, main_timer_finished
    if timer > 0:
        new_x = (test_seconds - timer) * (canvas.winfo_width() / test_seconds)
        canvas.coords(rect_id, 0, 0, new_x, 10)
        timer -= 1
        window.after(1000, update_timer)
    else:
        new_x = canvas.winfo_width()
        canvas.coords(rect_id, 0, 0, new_x, 10)
        main_timer_finished = True
        window.after_cancel(idle_timer)
        window.after_cancel(whoosh_timer)
        btn_save.config(state='normal')
        btn_reset.config(state='normal')
        text_window.config(state='disabled')


def clear_no_write():
    global idle_timer
    if not main_timer_finished:
        text_window.delete(1.0, END)
        idle_timer = window.after(5000, clear_no_write)


def reset_idle_timer(event):
    global idle_timer, whoosh_timer
    if not main_timer_finished:
        stop_whoosh_sound()
        window.after_cancel(idle_timer)
        window.after_cancel(whoosh_timer)
        whoosh_timer = window.after(4300, play_whoosh_sound)
        idle_timer = window.after(5000, clear_no_write)


def reset_app():
    global idle_timer, whoosh_timer, main_timer_finished
    window.after_cancel(idle_timer)
    window.after_cancel(whoosh_timer)
    stop_whoosh_sound()
    entry_minutes.config(state='normal')
    entry_minutes.delete(0, END)
    btn_start_timer.config(state='normal')
    btn_save.config(state='disabled')
    btn_reset.config(state='disabled')
    text_window.config(state='normal')
    text_window.delete(1.0, END)
    text_window.insert(END, "This text is going to disappear...")
    whoosh_timer = window.after(2300, play_whoosh_sound)
    idle_timer = window.after(3000, clear_no_write)
    canvas.delete("all")
    main_timer_finished = False
    window.title("Write, don't think!")


def save_file():
    filepath = asksaveasfilename(
        defaultextension='txt',
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')],
    )
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text = text_window.get(1.0, END)
        output_file.write(text)
    window.title(f'Text Editor - {filepath}')


window_width = 800
window_height = 600

window = Tk()
window.title("Write, don't think!")
window.geometry(f'{window_width}x{window_height}')
window.config(padx=50, pady=50, bg='gray')
window.wm_minsize(window_width, window_height-200)

fr_buttons = Frame(window, relief=RAISED, bd=2)
lbl_minutes = Label(fr_buttons, text="Enter minutes:")
lbl_minutes.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
entry_minutes = Entry(fr_buttons, justify='center')
entry_minutes.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

btn_save = Button(fr_buttons, text='Save As...', command=save_file, state='disabled')
btn_start_timer = Button(fr_buttons, text='Start Timer', command=set_timer)
btn_reset = Button(fr_buttons, text='Reset', command=reset_app, state='disabled')

btn_save.grid(row=3, column=0, sticky='ew', padx=5, pady=5)
btn_start_timer.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
btn_reset.grid(row=4, column=0, sticky='ew', padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky='ns')
text_window = Text(window, font=('Helvetica', 13), width=60, height=10, bg='whitesmoke')
text_window.grid(row=0, column=1, sticky='nsew')
text_window.insert(END, "This text is going to disappear...")

canvas = Canvas(window, width=window_width, height=10, bg='white')
canvas.grid(row=1, column=1, pady=20, sticky='ew')

text_window.bind("<Configure>", lambda event: canvas.config(width=event.width))

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

main_timer_finished = False
test_seconds = 60
whoosh_timer = window.after(2300, play_whoosh_sound)
idle_timer = window.after(3000, clear_no_write)
text_window.bind("<KeyPress>", reset_idle_timer)

window.mainloop()
