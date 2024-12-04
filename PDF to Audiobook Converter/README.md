# 📖 PDF to Audiobook Converter

The **PDF to Audiobook Converter** is a handy tool for transforming any PDF file into an audiobook. This project combines text extraction and high-quality text-to-speech (TTS) functionality to produce an MP3 file from the content of a PDF document.

## ✨ Features

### 📂 File Selection
- The interface, built with **Tkinter**, includes:
  - A simple button to select the PDF file to convert.
  - User-friendly navigation to pick any local PDF file.

### 🔊 Text-to-Speech Conversion
- Utilizes the **edge_tts** library for converting text to speech, offering:
  - Adjustable **pitch** and **speed**.
  - A wide selection of **narrators** in multiple languages.
- Converts raw text from the PDF into an **MP3 file**.
- Output files are stored in a dedicated `outputs` folder.

### 📜 PDF Text Extraction
- Employs the **PyPDF2** library to:
  - Read and extract the raw text content of the selected PDF.
  - Ensure accurate text processing for conversion.

## 🛠️ Technologies Used
- **GUI**: Tkinter for the graphical interface.
- **Text Extraction**: PyPDF2 for reading PDF content.
- **Text-to-Speech**: edge_tts for generating high-quality audio files.

## 🚀 Lessons Learned
1. **PDF Handling**: Learned the intricacies of extracting clean text from PDFs using PyPDF2.
2. **TTS Integration**: Explored a powerful, free TTS solution with extensive customization options.
3. **User Experience**: Improved skills in building intuitive interfaces with Tkinter.

## 📝 Future Improvements
1. Add support for **batch processing** multiple PDFs at once.
2. Allow users to **customize output paths** for generated MP3 files.
3. Enhance the interface with **progress indicators** during conversion.
4. Include **error handling** for PDFs with complex layouts or encryption.

## 📂 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/jordisorianoreos/100-Days-of-Code.git
   ```
2. Navigate to the project directory
   ```bash
   cd "PDF to Audiobook Converter"
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## 📧 Contact

If you have any questions, comments, or simply want to connect, feel free to reach out:

- **Email**: [jordisorianoreos@gmail.com](mailto:jordisorianoreos@gmail.com)
- **LinkedIn**: [Jordi Soriano Reos](https://www.linkedin.com/in/jordi-soriano-reos/)

Thank you for visiting my repository!
