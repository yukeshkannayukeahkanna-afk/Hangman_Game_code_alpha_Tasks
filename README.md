# Hangman_Game_code_alpha_Tasks
# 🪓 Hangman — Python Console Game

A simple, text-based **Hangman** game built with pure Python.  
Guess the hidden word one letter at a time — before the man is hanged!

---

## 📸 Preview

```
   -----
   |   |
   O   |
  /|\  |
       |
       |
=========

  Word    : _ _ t _ _ _
  Wrong   : a, e, i
  Chances : 3 remaining
----------------------------------------
  Enter a letter:
```

---

## 🎮 How to Play

1. A secret word is randomly chosen.
2. You see the word as blanks: `_ _ _ _ _ _`
3. Enter **one letter** per turn.
4. A correct guess reveals that letter in the word.
5. A wrong guess adds a body part to the hangman drawing.
6. You **win** by revealing all letters before 6 wrong guesses.
7. You **lose** if you make 6 incorrect guesses.

---

## 🚀 Getting Started

### Prerequisites

- Python **3.6+** (no external libraries required)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/hangman-python.git

# Navigate into the project folder
cd hangman-python
```

### Run the Game

```bash
python hangman.py
```

---

## 📁 Project Structure

```
hangman-python/
│
├── hangman.py      # Main game script
└── README.md       # Project documentation
```

---

## 🧠 Concepts Used

| Concept       | Usage in Project                                      |
|---------------|-------------------------------------------------------|
| `random`      | Picks a secret word randomly from the word list       |
| `while` loop  | Keeps the game running until win or lose condition    |
| `if-else`     | Validates input and checks correct/wrong guesses      |
| Strings       | Builds the `_ y _ h _ n` letter-reveal display        |
| Lists & Sets  | Tracks wrong guesses (list) and all guesses (set)     |

---

## ⚙️ Game Rules

| Setting           | Value                                  |
|-------------------|----------------------------------------|
| Word pool         | 5 predefined words                     |
| Max wrong guesses | 6                                      |
| Input             | Single alphabetic character (a–z)      |
| Repeated guess    | Warned, does not count as a new guess  |
| Play again        | Prompted after every round             |

---

## 📝 Word List

The game randomly picks from these 5 words:

```python
WORDS = ["python", "jungle", "rocket", "bridge", "castle"]
```

> 💡 You can easily expand this list inside `hangman.py` to add more words.

---

## 🔧 Possible Improvements

- [ ] Load words from an external `.txt` file
- [ ] Add difficulty levels (easy / medium / hard word lengths)
- [ ] Track and display win/loss score across rounds
- [ ] Add a hint feature (reveal one letter for free)
- [ ] Build a GUI version using `tkinter`

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Built as a beginner Python project to practice core programming concepts:  
`random` · `while loops` · `if-else` · `strings` · `lists`

---

## 👨‍💻 Author

**Yukeshkanna P**
B.Tech AI & Data Science
Aspiring Software Developer

---

## Connect

LinkedIn: [www.linkedin.com/in/yukeshkanna022007]

GitHub: [https://github.com/yukeshkannayukeahkanna-afk]
