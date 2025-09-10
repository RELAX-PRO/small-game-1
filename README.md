"# Number Guessing Game 🎯

A fun and interactive Python-based number guessing game where players try to guess a randomly generated number between 1 and 100!

## 🎮 Game Features

- **Two Difficulty Levels:**
  - **Easy Mode**: 10 attempts to guess the number
  - **Hard Mode**: 5 attempts to guess the number
- **Interactive Gameplay**: Real-time feedback on your guesses
- **Smart Hints**: Get "too high" or "too low" guidance
- **Attempt Tracking**: See how many guesses you have remaining

## 🚀 Quick Start

### Prerequisites

- Python 3.x installed on your system
- No additional dependencies required (uses only built-in libraries)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/RELAX-PRO/small-game-1.git
   cd small-game-1
   ```

2. Run the game:
   ```bash
   python3 "2.guess the number.py"
   ```

## 🎯 How to Play

1. **Start the Game**: Run the Python script
2. **Choose Difficulty**: Type `easy` for 10 attempts or `hard` for 5 attempts
3. **Make Your Guesses**: Enter numbers between 1 and 100
4. **Follow the Hints**: 
   - "Too high" means your guess is above the target number
   - "Too low" means your guess is below the target number
5. **Win Condition**: Guess the correct number before running out of attempts!

## 📝 Example Gameplay

```
Welcome the number guessing game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
Make a guess: 50
Too low
You have 9 attempts remaining to guess the number.
Make a guess: 75
Too low
You have 8 attempts remaining to guess the number.
Make a guess: 88
Too high
You have 7 attempts remaining to guess the number.
Make a guess: 82
You got it! The answer was 82
```

## 🔧 Technical Details

- **Language**: Python 3.x
- **Dependencies**: `random` (built-in module)
- **File Size**: ~900 bytes
- **Platform**: Cross-platform (Windows, macOS, Linux)

## 🎲 Game Logic

The game uses Python's `random.randint(1, 100)` to generate a random number between 1 and 100 (inclusive). The player's input is validated and compared against this target number, providing feedback until the number is guessed correctly or attempts run out.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements! Some ideas for enhancements:

- Add a scoring system
- Implement difficulty-based scoring
- Add a play-again feature
- Create a GUI version
- Add statistics tracking

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Have Fun!

Enjoy playing the Number Guessing Game! Challenge your friends to see who can guess the number in fewer attempts!" 
