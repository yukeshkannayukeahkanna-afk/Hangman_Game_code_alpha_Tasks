import random

# ─── Word List ────────────────────────────────────────────────────────────────
WORDS = ["python", "jungle", "rocket", "bridge", "castle"]

# ─── Hangman Stages (0 = full hang, 6 = safe) ────────────────────────────────
HANGMAN_STAGES = [
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
   |   |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
       |
       |
       |
=========""",
    """
   -----
   |   |
       |
       |
       |
       |
=========""",
]

# ─── Helper: display current word state ──────────────────────────────────────
def display_word(secret_word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

# ─── Helper: check if player won ─────────────────────────────────────────────
def is_won(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)

# ─── Main Game ────────────────────────────────────────────────────────────────
def play_hangman():
    print("\n" + "=" * 40)
    print("       Welcome to HANGMAN!")
    print("=" * 40)

    secret_word    = random.choice(WORDS)
    guessed        = set()          # all letters guessed so far
    wrong_guesses  = []             # only incorrect ones
    max_wrong      = 6

    while True:
        remaining = max_wrong - len(wrong_guesses)

        # ── Display hangman drawing ──────────────────────────────────────────
        print(HANGMAN_STAGES[len(wrong_guesses)])

        # ── Display game status ──────────────────────────────────────────────
        print(f"\n  Word    : {display_word(secret_word, guessed)}")
        print(f"  Wrong   : {', '.join(wrong_guesses) if wrong_guesses else 'None'}")
        print(f"  Chances : {remaining} remaining")
        print("-" * 40)

        # ── Win check ────────────────────────────────────────────────────────
        if is_won(secret_word, guessed):
            print(f"\n  🎉  You WON! The word was '{secret_word.upper()}'")
            break

        # ── Lose check ───────────────────────────────────────────────────────
        if len(wrong_guesses) >= max_wrong:
            print(f"\n  💀  Game Over! The word was '{secret_word.upper()}'")
            break

        # ── Get player input ─────────────────────────────────────────────────
        guess = input("  Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter (a-z).")
            continue

        if guess in guessed:
            print(f"  ⚠  You already guessed '{guess}'. Try another.")
            continue

        guessed.add(guess)

        if guess in secret_word:
            print(f"  ✅  '{guess}' is in the word!")
        else:
            wrong_guesses.append(guess)
            print(f"  ❌  '{guess}' is NOT in the word.")

    # ── Play again? ──────────────────────────────────────────────────────────
    print("\n" + "=" * 40)
    again = input("  Play again? (y / n): ").strip().lower()
    if again == "y":
        play_hangman()
    else:
        print("\n  Thanks for playing! Goodbye 👋\n")

# ─── Entry Point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    play_hangman()
