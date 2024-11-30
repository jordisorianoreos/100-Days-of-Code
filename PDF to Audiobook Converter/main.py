from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import PyPDF2
import asyncio
import edge_tts
from PIL import Image, ImageTk

VOICES = ['en-AU-NatashaNeural', 'en-AU-WilliamNeural']


async def save_as_mp3(text, output_path, voice):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)


def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


def open_pdf():
    pdf_path = askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        text = pdf_to_text(pdf_path)
        save_path = asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if save_path:
            voice = VOICES[1]
            loop = asyncio.get_event_loop_policy().get_event_loop()
            try:
                loop.run_until_complete(save_as_mp3(text, save_path, voice))
            finally:
                loop.close()
            os.system(f'start "" "{save_path}"')


root_width = 300
root_height = 250

root = Tk()
root.geometry(f"{root_width}x{root_height}")
root.title("PDF to MP3 Converter")

logo_path = "images/text-to-speech.png"
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((100, 100))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = Label(root, image=str(logo_photo))
logo_label.place(relx=0.5, rely=0.4, anchor=CENTER)

open_button = Button(root, text="Open PDF", command=open_pdf)
open_button.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
