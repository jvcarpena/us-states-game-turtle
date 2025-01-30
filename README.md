# U.S. States Game

## Overview
The U.S. States Game is an interactive quiz that helps users learn and test their knowledge of the 50 U.S. states. The game is built using Python's Turtle module for visualization and Pandas for data handling.

## Features
- Interactive GUI using Turtle graphics.
- Users input state names to be placed on a U.S. map.
- Tracks correctly guessed states in real-time.
- Generates a CSV file (`states_to_learn.csv`) with unguessed states.
- Ends when all states are correctly guessed or the user exits.

## Technologies Used
- **Python**
- **Turtle** (for graphics and user interaction)
- **Pandas** (for data processing)
- **CSV** (for storing missing states)

## Installation & Setup
1. **Clone the repository**:
   ```sh
   git clone <repository_url>
   cd us-states-game
   ```
2. **Set up a virtual environment (optional but recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```sh
   pip install pandas turtle
   ```
4. **Download the required files**:
   - Ensure `50_states.csv` (containing state names and coordinates) and `blank_states_img.gif` (map image) are in the project folder.

5. **Run the game**:
   ```sh
   python us_states_game.py
   ```

## How to Play
1. A U.S. map appears, prompting the user to enter state names.
2. Correct guesses are displayed on the map at their respective locations.
3. The game continues until all states are guessed or the user types `Exit`.
4. When exiting, a CSV file is generated containing states the user missed.

## Future Enhancements
- Implement a timer for added challenge.
- Add a scoring system and leaderboard.
- Provide hints for difficult states.

## Author
**JV Carpena**
