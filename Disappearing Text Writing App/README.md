# ✏️ Disappearing Text App

The **Disappearing Text App** is a unique writing application designed to encourage continuous writing. If the user stops typing for more than 5 seconds, all progress will be erased, adding a fun and challenging twist to the writing process. The app includes visual progress tracking and sound effects to enhance the user experience.

## ✨ Features

### 🖋️ Writing Interface
- **Text Entry Area**: A spacious text box created using Tkinter's `Text` widget for typing.
- **Time Selector**: Buttons allow the user to set a writing time in minutes.
- **Visual Timer**: A green progress bar below the text area fills proportionally to the elapsed time.

### ⏱️ Timer-Based Functionality
- If no input is detected for **5 seconds**:
  - A 'whoosh' sound plays as a warning.
  - The written text is erased if the user doesn’t resume typing.
  - The 5-second timer resets if the user starts typing again.

### 🛑 End of Writing Session
- When the set writing time ends:
  - The text box is **locked**, preventing further edits.
  - Options are provided to:
    - Save the text to a file.
    - Reset the app for a new session.

## 🛠️ Technologies Used
- **Programming Language**: Python.
- **GUI**: Tkinter for building the interface.
- **Sound Effects**: `pygame` library to handle audio playback.

## 🚀 Lessons Learned
1. **Synchronizing Events**: Managing the `after` functions in Tkinter to coordinate text deletion and sound playback without errors was a valuable learning experience.
2. **User Feedback**: Adding audio and visual cues significantly improved the app’s interactivity and usability.
3. **File Handling**: Implementing the save-to-file functionality reinforced my understanding of Python’s file I/O operations.

## 📝 Future Improvements
1. Allow the user to **pause the timer** or extend the writing session.
2. Provide customization options for:
   - The **idle time** before text disappears.
   - The **sound effect** played as a warning.
3. Enhance the UI with a more modern design using a framework like **Tkinter themes** or **custom widgets**.

## 📂 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/jordisorianoreos/100-Days-of-Code.git
   ```
2. Navigate to the project directory
   ```bash
   cd "Disappearing Text App"
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
