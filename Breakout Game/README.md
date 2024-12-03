# 🎮 Breakout Game

This Breakout project has been incredibly entertaining to create. It is a classic brick-breaking arcade game implemented using Python's Turtle graphics library. The game features multiple levels, a dynamic paddle, and sound effects to enhance the user experience.

## ✨ Features

### 🧱 Game Elements
- **Paddle**: Used to bounce the ball back towards the bricks.
- **Ball**: Moves around the screen, bouncing off walls and breaking bricks.
- **Bricks**: A total of 50 bricks arranged in 5 rows and 10 columns.
- **Scoreboard**: Tracks the player’s score.

### 🎯 Gameplay Mechanics
- The ball:
  - Bounces off the walls and paddle.
  - Breaks a brick when it collides, increasing the score.
- The paddle:
  - Allows for sharper rebound angles when the ball hits closer to its edges.
- Levels:
  - All bricks reset when cleared, progressing to the next level.
  - Each new level increases the ball's maximum speed.
- Sound effects:
  - Play during collisions for a more immersive experience.

## 🛠️ Technologies Used
- **Programming Language**: Python.
- **Graphics**: Turtle Graphics library for visual elements.
- **Sound Effects**: Python's `Pygame` module.

## 🚀 Challenges and Lessons Learned
1. **Collision Detection**: Fine-tuning the distances between objects to accurately detect bounces was the most challenging aspect, as the Turtle library has limited support for such mechanics.
2. **Game Design**: Balancing gameplay elements like ball speed and rebound angles was key to creating an enjoyable experience.
3. **Multilevel System**: Implementing the level progression and speed adjustments required careful planning.

## 📝 Future Improvements
1. Add a **lives system** to make the game more challenging.
2. Implement **power-ups** (e.g., larger paddle, faster ball, extra points).
3. Enhance the graphics with **better animations** and visual effects.
4. Include a **high score tracker** to save the best scores.

## 📂 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/jordisorianoreos/100-Days-of-Code.git
   ```
2. Navigate to the project directory
   ```bash
   cd "Breakout Game"
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
