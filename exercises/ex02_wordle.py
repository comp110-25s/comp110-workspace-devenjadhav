"""EX02 - Wordle: A simple word-guessing game."""

__author__ = "730760482"


def contains_char(word: str, char: str) -> bool:
    """Check if char exists in word."""
    assert len(char) == 1, f"len('{char}') is not 1"
    for letter in word:
        if letter == char:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    """Return emoji string based on Wordle's rules."""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002b1c"  # ⬜
    GREEN_BOX: str = "\U0001f7e9"  # 🟩
    YELLOW_BOX: str = "\U0001f7e8"  # 🟨

    result = ""

    for i in range(len(secret)):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX

    return result


def input_guess(expected_length: int) -> str:
    """Prompt user for a guess of the correct length and validate input."""
    guess = input(f"Enter a {expected_length} character word:")  # First prompt

    while len(guess) != expected_length:  # Keep prompting until correct length
        guess = input(f"That wasn't {expected_length} chars! Try again:")

    return guess  # Return valid guess


def main(secret: str) -> None:
    """Main game loop for Wordle."""
    turn = 1
    max_turns = 6
    won = False

    while turn <= max_turns and not won:
        print(f"=== Turn {turn}/{max_turns} ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            won = True
            print(f"You won in {turn}/{max_turns} turns!")
            return
        turn += 1

    """If the loop exits and the user hasn't won, they lose"""
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
