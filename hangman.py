import random

def hangman():
    # Five predefined words per CodeAlpha scope
    words = ["python", "developer", "hangman", "internship", "codealpha"]
    chosen_word = random.choice(words)
    attempts = 6  # Limit incorrect guesses to 6
    guessed_letters = set()
    display = ["_"] * len(chosen_word)

    print("🎮 Welcome to Hangman (CodeAlpha Task 1)!")
    while attempts > 0 and "_" in display:
        print("\nWord:", " ".join(display))
        print("Attempts left:", attempts)
        guess = input("Enter a single letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter exactly one alphabet letter.")
            continue
        if guess in guessed_letters:
            print("⚠️ You already tried that letter.")
            continue
        guessed_letters.add(guess)

        if guess in chosen_word:
            for i, ch in enumerate(chosen_word):
                if ch == guess:
                    display[i] = guess
            print("✅ Correct!")
        else:
            attempts -= 1
            print("❌ Wrong guess.")

    if "_" not in display:
        print(f"🎉 You won! The word was: {chosen_word}")
    else:
        print(f"💀 Game over! The word was: {chosen_word}")

if __name__ == "__main__":
    hangman()
