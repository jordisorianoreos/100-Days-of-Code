from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter.colorchooser import askcolor


class WatermarkApp:
    def __init__(self, window):
        self.window = window
        self.window_width = 800
        self.window_height = 600
        self.canvas_width = self.window_width - 100
        self.canvas_height = self.window_height - 100
        self.path = ''
        self.logo_path = ''
        self.current_image = None
        self.image_shown = None
        self.chosen_color = 'whitesmoke'
        self.upload_button_id = None

        self.setup_window()
        self.create_widgets()
        self.create_new_canvas()

    def setup_window(self):
        self.window.title('MyIMG: Watermark App')
        self.window.geometry(f'{self.window_width}x{self.window_height + 10}')
        self.window.config(padx=50, pady=50, bg='light gray')

    def create_widgets(self):
        self.label_entry = Label(self.window, text="Text to Insert:", bg='light gray')
        self.text_entry = Entry(self.window, width=50)
        self.text_color_btn = Button(self.window, text="Text Color", command=self.change_color_text, bg=self.chosen_color)
        self.insert_button = Button(self.window, text="Insert Text", command=self.insert_text, bg='whitesmoke')
        self.upload_logo_button = Button(self.window, text="Upload Logo", command=self.upload_logo, bg='whitesmoke')
        self.save_image_button = Button(self.window, text="Save as...", command=self.save_image, bg='whitesmoke')
        self.reset_button = Button(self.window, text="Reset", command=self.create_new_canvas, bg='whitesmoke')

    def create_new_canvas(self):
        if hasattr(self, 'canvas'):
            self.canvas.destroy()

        self.chosen_color = 'whitesmoke'
        self.text_color_btn.config(bg=self.chosen_color)

        self.canvas = Canvas(self.window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.grid(column=0, row=0, columnspan=7)

        self.canvas.create_text(self.canvas_width / 2, (self.canvas_height / 2) - 125,
                                text="MyIMG", font=("Terminal", 25, "bold"), fill='steelblue')

        img = Image.open('images/app_logo.png').resize((150, 150))
        self.image_shown = ImageTk.PhotoImage(img)
        self.canvas.create_image(self.canvas_width / 2, self.canvas_height / 2, anchor=CENTER, image=self.image_shown)

        upload_button = Button(self.window, text='Upload Image', command=self.upload_image, font=12)
        self.upload_button_id = self.canvas.create_window(self.canvas_width / 2, (self.canvas_height / 2) + 110,
                                                          anchor=CENTER, window=upload_button)

        self.show_layout(False)

    def upload_image(self):
        f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
        self.path = filedialog.askopenfilename(filetypes=f_types)
        if self.path:
            image = Image.open(self.path)
            self.current_image = image
            self.change_shown_image(image)
            self.change_layout()

    def upload_logo(self):
        f_types = [('PNG Files', '*.png')]
        self.logo_path = filedialog.askopenfilename(filetypes=f_types)
        if self.logo_path and self.path:
            image = Image.open(self.path)
            logo = Image.open(self.logo_path)
            logo = self.resize_logo(image, logo)
            position = self.calculate_logo_position(image, logo)
            image.paste(logo, position, logo)
            self.current_image = image
            self.change_shown_image(image)

    @staticmethod
    def resize_logo(image, logo):
        logo_width, logo_height = logo.size
        new_logo_width = int(image.width / 15)
        new_logo_height = int((new_logo_width / logo_width) * logo_height)
        return logo.resize((new_logo_width, new_logo_height))

    @staticmethod
    def calculate_logo_position(image, logo):
        return int(0.97 * image.width) - logo.width, int(0.97 * image.height) - logo.height

    def save_image(self):
        if self.current_image:
            f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=f_types)
            if save_path:
                self.current_image.save(save_path)

    def change_shown_image(self, image):
        width, height = image.size
        new_height = int(0.8 * self.canvas_height)
        new_width = int((new_height / height) * width)
        image_resized = image.resize((new_width, new_height))
        self.image_shown = ImageTk.PhotoImage(image_resized)
        self.canvas.create_image(self.canvas_width / 2, self.canvas_height / 2, anchor=CENTER, image=self.image_shown)

    def change_layout(self):
        if self.upload_button_id is not None:
            self.canvas.delete(self.upload_button_id)
        self.show_layout(True)

    def show_layout(self, show):
        if show:
            self.label_entry.grid(column=0, row=1, pady=15)
            self.text_entry.grid(column=1, row=1)
            self.text_color_btn.grid(column=2, row=1)
            self.insert_button.grid(column=3, row=1)
            self.upload_logo_button.grid(column=4, row=1)
            self.save_image_button.grid(column=5, row=1)
            self.reset_button.grid(column=6, row=1)
        else:
            self.text_entry.delete(0, END)
            self.label_entry.grid_forget()
            self.text_entry.grid_forget()
            self.text_color_btn.grid_forget()
            self.insert_button.grid_forget()
            self.upload_logo_button.grid_forget()
            self.save_image_button.grid_forget()
            self.reset_button.grid_forget()

    def insert_text(self):
        input_text = self.text_entry.get()
        if self.path and input_text:
            image_w_text = Image.open(self.path)
            draw = ImageDraw.Draw(image_w_text)
            font = self.load_font(image_w_text)
            text_length = draw.textlength(input_text, font)
            x = (image_w_text.width - text_length - image_w_text.width / 25)
            y = image_w_text.height - image_w_text.height / 10
            draw.text((x, y), input_text, fill=self.chosen_color, font=font)
            self.current_image = image_w_text
            self.change_shown_image(image_w_text)

    @staticmethod
    def load_font(image):
        try:
            return ImageFont.truetype("fonts/Rogbold.otf", size=int(image.height / 15))
        except OSError:
            return ImageFont.load_default()

    def change_color_text(self):
        self.chosen_color = askcolor(title="Text Color")[1]
        self.text_color_btn.config(bg=str(self.chosen_color))


# Main loop
window = Tk()
app = WatermarkApp(window)
window.mainloop()
