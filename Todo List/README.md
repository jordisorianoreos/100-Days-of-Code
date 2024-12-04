# ✅ Todo List

The **Todo List** project is a task management web application designed to help users organize and track their tasks across three distinct status categories. It features user authentication, an intuitive interface, and robust database management for seamless task handling.

## ✨ Features

### 🗂️ Task Management
- **Three Columns for Task Status**:
  - **To Do**: Add tasks that need to be started.
  - **Doing**: Tasks in progress.
  - **Done**: Completed tasks.
- **Task Workflow**:
  - Clicking a task in the **To Do** column moves it to **Doing**.
  - Clicking a task in the **Doing** column moves it to **Done**.

### 🔄 Task Controls
- **Add New Tasks**: Easily create tasks in any column.
- **Delete Tasks**:
  - Remove individual tasks.
  - Option to clear all tasks at once.

### 🔐 User Authentication
- **Register and Login System**:
  - Create an account to save and access your personalized tasks.
  - Tasks are tied to user accounts for secure management.

## 🛠️ Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite with relationships between tables for users and tasks.

## 🚀 Lessons Learned
1. **Database Relationships**: Managed relational tables to associate users with their tasks.
2. **Task Status Workflow**: Developed intuitive status transitions for tasks.
3. **Design Challenges**: Balanced visual appeal with functionality in the dashboard interface.

## 📝 Future Improvements
1. **Drag-and-Drop Interface**: Add drag-and-drop functionality for moving tasks between columns.
2. **Custom Categories**: Allow users to create their own task categories beyond To Do, Doing, and Done.
3. **Deadline Management**: Introduce due dates with notifications for pending tasks.

## 📂 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/jordisorianoreos/100-Days-of-Code.git
   ```
2. Navigate to the project directory
   ```bash
   cd "Todo List"
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
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
