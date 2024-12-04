# 🎨 Image Colour Palette Generator

The **Image Colour Palette Generator** is a web application that extracts the most frequent colors from an image and displays them as a palette. It uses clustering techniques to identify dominant colors, making it a handy tool for designers, artists, and anyone looking for color inspiration.

## ✨ Features

### 🌟 Upload and Analyze Images
- Users can **upload an image** through the interface.
- After uploading, the app redirects to a page displaying:
  - The **uploaded image**.
  - A **color palette** with the 10 most frequent colors in the image.

### 🎨 Color Swatches
- Each swatch displays:
  - A rectangle filled with the color.
  - The **hex code** of the color.
  - The **percentage** it represents within the image.

### 🧠 Algorithm
- Utilizes a **k-means clustering algorithm** to reduce the number of colors in the image by grouping similar ones.
- Selects and ranks the top 10 colors based on frequency.

## 🛠️ Technologies Used
- **Frontend**: HTML, CSS, JS for the user interface.
- **Backend**: Python (Flask) for image processing and server-side logic.
- **Image Analysis**: `Pillow` for image handling and `sklearn` for clustering.

## 🚀 Lessons Learned
1. **Image Processing**: Gained experience in extracting meaningful data from images, such as dominant colors.
2. **Clustering Techniques**: Implementing k-means clustering reinforced my understanding of unsupervised learning.
3. **Web Integration**: Learned to integrate complex backend processes with a simple, user-friendly web interface.

## 📝 Future Improvements
1. Add an option to **download the palette** as an image or JSON file.
2. Include support for **customizable cluster numbers**, allowing users to choose how many colors to extract.
3. Improve the UI/UX with animations and responsive design.
4. Extend the functionality to support **batch processing** of multiple images.

## 📂 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/jordisorianoreos/100-Days-of-Code.git
   ```
2. Navigate to the project directory
   ```bash
   cd "Image Colour Palette Generator"
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python webpage.py
   ```
5. Open your browser and go to:
   ```bash
   http://localhost:5000
   ```
## 📧 Contact

If you have any questions, comments, or simply want to connect, feel free to reach out:

- **Email**: [jordisorianoreos@gmail.com](mailto:jordisorianoreos@gmail.com)
- **LinkedIn**: [Jordi Soriano Reos](https://www.linkedin.com/in/jordi-soriano-reos/)

Thank you for visiting my repository!
