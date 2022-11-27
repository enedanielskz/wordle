import os

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


def update_list(old_list, green_letters, yellow_letters, red_letters):
    new_list = []

    for test_word in old_list:
        for pos in range(5):
            if green_letters[pos] != "-" and test_word[pos] != green_letters[pos]:
                break
            elif yellow_letters[pos] != "-" and (test_word.find(yellow_letters[pos]) == -1
                                                 or test_word[pos] == yellow_letters[pos]):
                break
            elif red_letters[pos] != "-" and test_word.find(red_letters[pos]) != -1:
                break
        else:
            new_list.append(test_word)

    return new_list


def get_common_letters(guess_list):
    common_letters = [{}, {}, {}, {}, {}]

    for test_word in guess_list:
        for pos in range(5):
            letter = test_word[pos]
            if letter in common_letters[pos]:
                common_letters[pos][letter] += 1
            else:
                common_letters[pos][letter] = 1

    return common_letters


def get_best_guess(guess_list, common_letters):
    best_score = 0
    best_guess = ""

    for test_word in guess_list:
        unique_letters = {}
        for pos in range(5):
            letter = test_word[pos]

            if letter in unique_letters:
                if common_letters[pos][letter] > unique_letters[letter]:
                    unique_letters[letter] = common_letters[pos][letter]
            else:
                unique_letters[letter] = common_letters[pos][letter]

        score = sum(unique_letters.values())
        if score > best_score:
            best_score = score
            best_guess = test_word

    return best_guess


def main():
    initialize_colorama()

    word_list = read_word_list("words.txt")
    first_guess = get_best_guess(word_list, get_common_letters(word_list))

    average_guess = 0
    min_guess = 100
    max_guess = 0

    word_number = 0
    for word in word_list:
        word_number += 1
        print(f"{Fore.BLUE}Word {word_number}: {Fore.GREEN}{word},", end=" ")

        guess_number = 0
        correct_letters = 0

        guess_list = list(word_list)

        green_letters = ["-", "-", "-", "-", "-"]

        while True:
            yellow_letters = ["-", "-", "-", "-", "-"]
            red_letters = ["-", "-", "-", "-", "-"]

            guess_number += 1
            if guess_number == 1:
                guess = first_guess
            elif len(guess_list) > 2 and correct_letters != 4:
                guess = get_best_guess(guess_list, get_common_letters(guess_list))
            else:
                guess = guess_list[0]

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

            if correct_letters == 5:
                print()
                average_guess += guess_number
                if guess_number < min_guess:
                    min_guess = guess_number
                if guess_number > max_guess:
                    max_guess = guess_number
                break
            else:
                print(",", end=" ")

            guess_list = update_list(guess_list, green_letters, yellow_letters, red_letters)

    average_guess /= word_number
    print(f"{Fore.BLUE}Average guess: {average_guess}\nMinimum guess: {min_guess}\n"
          f"Maximum guess: {max_guess}{Fore.RESET}\n")


if __name__ == "__main__":
    main()
