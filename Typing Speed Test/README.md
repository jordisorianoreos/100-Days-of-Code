# ⌨️ Typing Speed Test

The **Typing Speed Test** is a Python-based desktop application designed to measure typing speed in real-time. It features an intuitive user interface built with Tkinter and provides metrics such as **CPM (Characters Per Minute)** and **WPM (Words Per Minute)**.

## ✨ Features

### 🕒 Timer
- A 60-second timer starts when the user begins typing.
- Displays remaining time dynamically on the interface.

### 📊 Performance Metrics
- **Corrected CPM**: Measures correctly typed characters per minute.
- **WPM**: Calculates words per minute, assuming an average word length of 5 characters.
- Updates in real-time during the typing test.

### 🖋️ Typing Workflow
- Words appear one at a time, with the current word highlighted in the center of the screen.
- The previous word appears to the left and the next word to the right for easy reference.
- Words turn **green** when correctly typed and **red** when incorrect.

### 🔄 Reset and Restart
- At the end of the timer, the results are displayed on the screen.
- Includes an option to restart the test.

### 🎨 Visual Design
- Animated title on the home screen.
- Clean and interactive layout using a typewriter-themed background image.

## 🛠️ Technologies Used
- **Python**: Core programming language.
- **Tkinter**: GUI library for interface creation.
- **Pillow**: For resizing and displaying images.

## 🚀 Lessons Learned
1. **Tkinter Mastery**: Improved structuring and layout handling for complex user interfaces.
2. **Timer Synchronization**: Learned how to implement dynamic updates for timers and metrics.
3. **Word Handling**: Developed efficient methods to transition between words and manage user input validation.

## 📈 Metrics Calculation
1. **Corrected CPM**:
   - Includes only characters in correctly typed words.
   - Excludes errors and incomplete words.
2. **Raw CPM**:
   - Includes all typed characters, regardless of correctness.
3. **WPM**:
   - Assumes a standard word length of 5 characters.

## 📂 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/jordisorianoreos/100-Days-of-Code.git
   ```
2. Navigate to the project directory
   ```bash
   cd "Typing Speed Test"
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
