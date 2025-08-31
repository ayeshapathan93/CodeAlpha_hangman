import random

def hangman():
    # Predefined words
    words = ["python", "code", "alpha", "hangman", "game"]
    word = random.choice(words)  # Randomly pick a word
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("🎮 Welcome to Hangman Game!")
    print("Word to guess:", " ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nGuess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")

        print("Word:", " ".join(guessed_word))

    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)


# Run the game
hangman()
