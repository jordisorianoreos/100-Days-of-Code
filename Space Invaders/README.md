# 🚀 Space Invaders

The **Space Invaders** project is a recreation of the classic arcade game with modern touches. It’s a fast-paced, progressively challenging game where players control a spaceship to defeat waves of aliens, with obstacles and dynamic gameplay elements.

## ✨ Features

### 👾 Alien Waves
- A **5-row by 10-column grid** of aliens (Turtle objects) that:
  - Move horizontally from right to left across the screen.
  - Drop down when they reach the screen edges.
  - Have a chance to fire bullets in each game loop cycle.
- When all aliens are destroyed, a new wave appears with:
  - **Faster movement**.
  - **Increased firing probability**.

### 🚀 Player’s Spaceship
- **Mouse-controlled movement**: The spaceship moves horizontally based on mouse position.
- **Bullet firing**:
  - Click the left mouse button to shoot.
  - Initial cooldown of one second between shots.
  - Cooldown reduces as levels progress.

### ☄ Rock Obstacles
- Three clusters of small Turtle blocks act as obstacles.
- Rocks can be destroyed by bullets, adding a strategic layer to the game.

### 🔊 Sound Effects
- Custom sounds for:
  - Shooting.
  - Explosions.
  - Level progression.
  - Game-over events.

### 🕹️ Progressive Difficulty
- Each new level increases the challenge:
  - **Faster aliens**.
  - **Higher alien firing probability**.
  - **Reduced spaceship shot cooldown**.

### 🛑 Game Over
- The game ends if:
  - An alien bullet hits the spaceship.
  - Aliens reach the bottom of the screen.

## 🛠️ Technologies Used
- **Python**: Core game logic.
- **Turtle Graphics**: For visual elements like aliens, spaceship, bullets, and obstacles.
- **Sound Effects**: Enhancing player immersion.

## 🚀 Lessons Learned
1. **Game Loops**: Mastered handling simultaneous events (movement, firing, and collision detection).
2. **Collision Logic**: Refined skills in calculating object interactions with custom hitboxes.
3. **Game Balance**: Learned how to fine-tune difficulty to keep gameplay engaging.

## 📝 Future Improvements
1. Add **power-ups** for the spaceship (e.g., shields, multi-shot).
2. Include a **scoreboard** and **leaderboard** to track player achievements.
3. Enhance alien movement patterns for greater unpredictability.
4. Integrate more **levels and unique alien types** with special abilities.

## 📂 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/jordisorianoreos/100-Days-of-Code.git
   ```
2. Navigate to the project directory
   ```bash
   cd "Space Invaders"
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
