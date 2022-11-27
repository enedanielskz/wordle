import os
import random

from colorama import init, Fore


def initialize_colorama():
    init()
    os.system('cls' if os.name == 'nt' else 'clear')


def read_word_list(file_name):
    file = open(file_name, "r")
    word_list = file.readlines()
    file.close()
    for pos in range(len(word_list)):
        word_list[pos] = word_list[pos].replace("\n", "")
    return word_list


def send_feedback(green_letters, yellow_letters, red_letters):
    file = open("feedback.txt", "w")
    file.write(f"{' '.join(green_letters)}\n{' '.join(yellow_letters)}\n{' '.join(red_letters)}")
    file.close()


def main():
    initialize_colorama()

    word_list = read_word_list("words.txt")

    word_number = int(input(f"{Fore.BLUE}Number of words to guess: "))
    print()

    average_guess = 0
    min_guess = 100
    max_guess = 0
    for n in range(word_number):
        word = random.choice(word_list)
        print(f"{Fore.BLUE}Word {n + 1}: {Fore.GREEN}-----")

        green_letters = ["-", "-", "-", "-", "-"]
        correct_letters = 0
        guess_number = 0
        while True:
            guess_number += 1
            yellow_letters = ["-", "-", "-", "-", "-"]
            red_letters = ["-", "-", "-", "-", "-"]

            while True:
                guess = input(f"{Fore.BLUE}Guess {guess_number}: {Fore.WHITE}")
                if guess in word_list:
                    break
                print(f"{Fore.RED}Error: {Fore.WHITE}{guess} {Fore.RED}is not in the list.")

            print(f"{Fore.BLUE}Guess {guess_number}: ", end="")
            for pos in range(5):
                if guess[pos] == word[pos]:
                    print(f"{Fore.GREEN}{guess[pos]}", end="")
                    if guess[pos] != green_letters[pos]:
                        green_letters[pos] = guess[pos]
                        correct_letters += 1
                elif word.find(guess[pos]) != -1:
                    print(f"{Fore.YELLOW}{guess[pos]}", end="")
                    yellow_letters[pos] = guess[pos]
                else:
                    print(f"{Fore.RED}{guess[pos]}", end="")
                    red_letters[pos] = guess[pos]

            send_feedback(green_letters, yellow_letters, red_letters)

            if correct_letters == 5:
                print(f"{Fore.BLUE} Correct!\n")
                average_guess += guess_number
                if guess_number < min_guess:
                    min_guess = guess_number
                if guess_number > max_guess:
                    max_guess = guess_number
                break
            print()

    send_feedback("0", "0", "0")

    average_guess /= word_number
    print(f"{Fore.BLUE}Average guess: {average_guess}\nMinimum guess: {min_guess}\n"
          f"Maximum guess: {max_guess}{Fore.RESET}\n")


if __name__ == "__main__":
    main()
