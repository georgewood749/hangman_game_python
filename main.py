import random
import HangmanASCII
import WordList

random_word = random.choice(WordList.word_list)
word_length = len(random_word)
display = []
played_letters = []
lives = 6

for _ in range(word_length):
    display += "_"

print(HangmanASCII.logo)
print(' '.join(display))

another_game = True
while another_game:
    end = False
    while not end:
        player_guess = input("\nPlease guess a letter.\n")

        for position in range(word_length):
            letter = random_word[position]
            if letter == player_guess:
                display[position] = letter

        if player_guess in played_letters:
            print(f"You've already guessed {player_guess}")

        if player_guess not in random_word and player_guess not in played_letters:
            print(f"You guessed {player_guess}. That is not in the word.")
            lives -= 1

        played_letters.append(player_guess)

        print(HangmanASCII.stages[lives])
        print(' '.join(display))

        if lives == 0:
            end = True
            print(f"\nGame over!\nThe word was: {random_word}")
        if "_" not in display:
            end = True
            print("You win!")
    play_again = input("Would you like to play another game? Y or N\n").lower()
    if play_again == "n":
        another_game = False





