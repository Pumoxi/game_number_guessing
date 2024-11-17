# Number Guessing Game 🎲  

A simple and interactive Python CLI game where you guess a randomly generated number between 1 and 100. Test your luck and logic with two levels of difficulty!  

---

## Features  
- **Difficulty Modes**:  
  - Easy: 10 attempts  
  - Hard: 5 attempts  
- Provides feedback ("Too high" or "Too low") after each guess.  
- Declares a win or loss based on the number of attempts left.  

---

## How It Works  

1. The program generates a random number between 1 and 100.  
2. You choose a difficulty level: **easy** (10 attempts) or **hard** (5 attempts).  
3. Start guessing!  
   - If your guess is too high or too low, you'll receive feedback to guide your next guess.  
   - You win if you guess correctly within the allowed attempts.  
   - If you run out of attempts, the game ends with a loss.  

---

## How to Run  

### Prerequisites  
- Python 3.x installed on your machine.  

### Steps  
1. Clone this repository:  
   ```bash  
   git clone git@github.com:Pumoxi/game_number_guessing.git
   ```

2.	Navigate to the project folder:

    ```bash
    cd game_number_guessing
    ```


3.	Run the script:

    ```python
    python main.py  
    ```

4. Sample Gameplay

    ```plaintext
    Welcome to the Number Guessing Game!  
    I'm thinking of a number between 1 and 100.  

    Choose a difficulty. Type 'easy' or 'hard': easy  
    You have 10 attempts remaining to guess the number.  
    Make a guess: 50  
    Too low.  
    Guess again.  

    You have 9 attempts remaining to guess the number.  
    Make a guess: 75  
    Too high.  
    Guess again.  

    You have 8 attempts remaining to guess the number.  
    Make a guess: 63  
    You got it! The answer was 63.  
    ```

## Customization

You can easily modify the game by updating the following variables in the code:
	•	EASY_ATTEMPTS for the number of attempts in easy mode.
	•	HARD_ATTEMPTS for the number of attempts in hard mode.

## Acknowledgments

- The development of this project was inspired by course “Master Python by building 100 projects in 100 days”, Dr. Angela Yu.