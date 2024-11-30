from tkinter import *
import random
from PIL import Image, ImageTk


class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Typing Speed Test')
        self.root.geometry('800x610')
        self.root.config(padx=50, pady=50, bg='#73bfb2')

        self.test_seconds = 60
        self.timer_running = False
        self.written_words = []
        self.right_written_words = []

        self.words_list = open('words.txt').read().splitlines()
        random.shuffle(self.words_list)
        self.words_list.append("")

        self.id_current_word = 0
        self.current_word = self.words_list[self.id_current_word]
        self.next_word = self.words_list[self.id_current_word]

        self.between_words_sep = 35

        self.canvas_width = 700
        self.canvas_height = 400

        self.show_main_screen()

    def show_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.title_text = "Typing Speed Test"
        self.title_label = Label(self.root, text="", font=("Courier New", 40, "bold"), bg='#73bfb2', fg='whitesmoke')
        self.title_label.pack(pady=20)
        self.animate_title(0)

        img = Image.open('images/typewriter.png').resize((150, 150))
        image_shown = ImageTk.PhotoImage(img)
        image_label = Label(self.root, image=str(image_shown), bg='#73bfb2')
        image_label.image = image_shown  # Keep a reference to avoid garbage collection
        image_label.pack(pady=20)

        start_button = Button(self.root, text="Start", font=("Ariel", 20), command=self.start_app)
        start_button.pack(pady=20)

    def animate_title(self, index):
        if index < len(self.title_text):
            current_text = self.title_text[:index + 1]
            self.title_label.config(text=current_text)
            self.root.after(100, self.animate_title, index + 1)

    def start_app(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.grid(column=0, row=0)

        self.cnv_cnt_word = self.canvas.create_text(self.canvas_width/2, self.canvas_height/2, text=self.words_list[0],
                                                    anchor='center', font=("Ariel", 35))

        current_w_width = self.get_text_width(self.canvas, self.cnv_cnt_word)

        self.cnv_lst_word = self.canvas.create_text(self.canvas_width/2 - current_w_width/2 - self.between_words_sep,
                                                    (0.443*self.canvas_height), text="",
                                                    anchor='ne', font=("Ariel", 33), fill='darkgray')

        self.cnv_nxt_word = self.canvas.create_text(self.canvas_width/2 + current_w_width/2 + self.between_words_sep,
                                                    (0.443*self.canvas_height), text=self.words_list[1],
                                                    anchor='nw', font=("Ariel", 33), fill='darkgray')

        self.cnv_timer = self.canvas.create_text(0.05*self.canvas_width, 0.05*self.canvas_height,
                                                 text=f"Time left: {self.test_seconds}",
                                                 anchor='nw', font=("Courier New", 14))
        self.cnv_score = self.canvas.create_text(0.95*self.canvas_width, 0.05*self.canvas_height,
                                                 text=f"CPM: 00  |  WPM: 00",
                                                 anchor='ne', font=("Courier New", 14))

        self.writing_box = Entry(self.root, font=("Ariel", 35), justify='center', state='normal')
        self.writing_box.grid(column=0, row=1)

        self.writing_box.bind('<space>', self.on_space)
        self.writing_box.bind('<Key>', self.first_key_press)
        self.writing_box.bind('<BackSpace>', self.return_last_word)

    def set_timer(self):
        self.timer_running = True
        self.update_timer(self.test_seconds)

    def update_timer(self, timer):
        if timer > 0:
            self.canvas.itemconfig(self.cnv_timer, text=f"Time left: {str(timer)}")

            corrected_cpm, raw_cpm = self.calculate_cpm(timer)
            wpm = round(corrected_cpm / 5)

            self.canvas.itemconfig(self.cnv_score, text=f"CPM: {corrected_cpm}  |  WPM: {wpm}")
            self.root.after(1000, self.update_timer, timer - 1)
        else:
            self.time_is_over()

    def time_is_over(self):
        self.canvas.itemconfig(self.cnv_timer, text="Time is over!")

        self.canvas.delete(self.cnv_lst_word)
        self.canvas.delete(self.cnv_cnt_word)
        self.canvas.delete(self.cnv_nxt_word)

        self.canvas.itemconfig(self.cnv_timer, font=("Courier New", 45), anchor='center')
        self.canvas.itemconfig(self.cnv_score, font=("Courier New", 20), anchor='center')

        self.canvas.coords(self.cnv_timer, self.canvas_width/2, self.canvas_height/2 - 30)
        self.canvas.coords(self.cnv_score, self.canvas_width/2, self.canvas_height/2 + 30)

        self.writing_box.delete(0, END)
        self.writing_box.config(state='disabled')
        self.writing_box.destroy()

        restart_button = Button(self.root, text="Restart", font=("Ariel", 20), command=self.restart_app)
        restart_button.grid(column=0, row=1, pady=20)

    def restart_app(self):
        self.__init__(self.root)

    def goto_next_word(self):
        self.id_current_word += 1

        if self.id_current_word < len(self.words_list) - 1:
            self.canvas.itemconfig(self.cnv_lst_word, text=self.words_list[self.id_current_word-1])
            self.canvas.itemconfig(self.cnv_cnt_word, text=self.words_list[self.id_current_word])
            self.canvas.itemconfig(self.cnv_nxt_word, text=self.words_list[self.id_current_word + 1])

            current_w_width = self.get_text_width(self.canvas, self.cnv_cnt_word)
            self.canvas.coords(self.cnv_lst_word, self.canvas_width/2 - current_w_width/2 - self.between_words_sep,
                               0.443*self.canvas_height)
            self.canvas.coords(self.cnv_nxt_word, self.canvas_width/2 + current_w_width/2 + self.between_words_sep,
                               0.443*self.canvas_height)
        else:
            self.canvas.itemconfig(self.cnv_cnt_word, text="")
            self.canvas.itemconfig(self.cnv_nxt_word, text="")

    def get_text_width(self, canvas, item):
        bbox = canvas.bbox(item)
        if bbox:
            width = bbox[2] - bbox[0]
            return width
        return 0

    def calculate_cpm(self, timer):
        self.right_written_words = []
        words_until_now = self.words_list[:len(self.written_words)]

        for i in range(len(words_until_now)):
            if words_until_now[i] == self.written_words[i]:
                self.right_written_words.append(self.written_words[i])
                self.canvas.itemconfig(self.cnv_lst_word, fill='green')
            else:
                self.canvas.itemconfig(self.cnv_lst_word, fill='red')

        str_written_words = ' '.join(self.right_written_words)
        character_count = len(str_written_words)
        corrected_cpm = int(character_count / ((self.test_seconds - timer - 0.0000000001) / 60))

        str_written_words = ' '.join(self.written_words)
        character_count = len(str_written_words)
        raw_cpm = int(character_count / ((self.test_seconds - timer - 0.0000000001) / 60))

        return corrected_cpm, raw_cpm

    def first_key_press(self, event):
        if not self.timer_running:
            self.set_timer()

    def on_space(self, event):
        self.written_words.append(self.writing_box.get().strip())
        self.goto_next_word()
        self.writing_box.delete(0, END)

    def return_last_word(self, event):
        if self.id_current_word > 0 and self.writing_box.get().strip() == '':
            self.id_current_word -= 2
            self.writing_box.insert(END, f"{self.written_words[self.id_current_word+1]} ")
            self.written_words = self.written_words[:-1]
            self.goto_next_word()


if __name__ == "__main__":
    root = Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
