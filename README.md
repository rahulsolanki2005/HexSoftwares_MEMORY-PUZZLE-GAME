# 🎮 Memory Puzzle Game

**Memory Puzzle Game** is a fun and challenging Python-based card matching game that:
- Tests your memory by matching pairs of emoji cards in a 4x4 grid.
- Features **three difficulty levels** (Easy, Medium, Hard) with different time limits.
- Tracks your **moves** and **best scores** for each difficulty.
- Provides a clean, modern dark-themed UI with smooth gameplay.

---

## 🔧 Features

- **Three Difficulty Levels**
  - Easy: 90 seconds to match all 8 pairs
  - Medium: 60 seconds for a moderate challenge
  - Hard: 45 seconds for memory experts
- **Real-time Timer**
  - Countdown timer that turns red when time is running out
  - Game ends when timer reaches zero
- **Score Tracking**
  - Move counter to track your efficiency
  - High score system saves your best performance for each difficulty
- **Modern UI**
  - Dark-themed interface with vibrant colors
  - 16 unique emoji cards (🎮🎯🎲🎪🎨🎭 and more)
  - Smooth card flip animations
  - Resizable window for different screen sizes
- **Game Mechanics**
  - Click cards to flip and reveal emojis
  - Match two identical cards to keep them flipped
  - Win by matching all 8 pairs before time runs out

---

## 🎯 How it Works

- **Card System**: 16 cards (8 pairs) are randomly shuffled at the start of each game
- **Matching Logic**: Click two cards to flip them. If they match, they stay green and disabled. If not, they flip back after 1 second
- **Timer**: Starts when the game begins and counts down. Game ends with victory if all pairs are matched, or defeat if time runs out
- **Scoring**: Your score is based on the number of moves taken. Fewer moves = better score

---

## ⚙️ Requirements

- Python 3.7+
- Tkinter (comes pre-installed with Python)

No additional libraries needed!

---

## 🚀 Installation & Usage

1. Clone the repository:
```bash
git clone https://github.com/rahulsolanki2005/HexSoftwares_MEMORY-PUZZLE-GAME
cd memory-puzzle-game
```

2. Run the game:
```bash
python app.py
```

3. Select difficulty level and start playing!

---

## 🎮 How to Play

1. **Choose Difficulty**: Select Easy, Medium, or Hard from the main menu
2. **Flip Cards**: Click on any card to flip it and reveal the emoji
3. **Find Matches**: Click another card to find its matching pair
4. **Complete the Grid**: Match all 8 pairs before the timer runs out
5. **Beat Your Score**: Try to win with fewer moves to set a new high score

**Game Rules:**
- Two cards can be flipped at a time
- Matching cards turn green and stay flipped
- Non-matching cards flip back after 1 second
- Win by matching all pairs within the time limit

---

## 📁 Project Structure

```
memory-puzzle-game/
│
├── app.py          # Main game file with complete logic
└── README.md               # Project documentation
```

---

## 🎨 Customization

You can easily customize the game by editing `app.py`:

- **Emojis**: Change the `self.emojis` list to use different symbols
- **Colors**: Modify color codes for UI elements
- **Time Limits**: Adjust `time_limit` values for each difficulty
- **Window Size**: Change `geometry()` values for different screen sizes

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [https://github.com/rahulsolanki2005)
- Email: rahul.solanki.cs@gmail.com

---

Made with ❤️ and Python | Built as an internship project

⭐ **Star this repo if you enjoyed the game!** ⭐
