import os
import pyautogui as keyboard
import time


def start():
    for i in range(0, 5):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Wordle guesser starting in {5-i}")
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Wordle guesser started!\n")
    time.sleep(1)


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


def reset_feedback():
    file = open("feedback.txt", "w")
    file.write("1\n1\n1")
    file.close()


def get_feedback():
    file = open("feedback.txt", "r")
    green_letters = file.readline().split()
    yellow_letters = file.readline().split()
    red_letters = file.readline().split()
    file.close()
    return green_letters, yellow_letters, red_letters


def main():
    reset_feedback()

    start()

    word_list = read_word_list("words.txt")
    guess_list = list(word_list)
    first_guess = get_best_guess(guess_list, get_common_letters(guess_list))

    while True:
        time.sleep(0.1)

        green_letters, yellow_letters, red_letters = get_feedback()
        if green_letters == yellow_letters == red_letters == ["0"]:
            print("Wordle guesser finished guessing!\n")
            break
        elif "-" not in green_letters:
            guess_list = list(word_list)
            guess = first_guess
        else:
            guess_list = update_list(guess_list, green_letters, yellow_letters, red_letters)
            if len(guess_list) > 2 and green_letters.count("-") != 1:
                guess = get_best_guess(guess_list, get_common_letters(guess_list))
            else:
                guess = guess_list[0]

        keyboard.typewrite(guess)
        keyboard.press("enter")


if __name__ == "__main__":
    main()
