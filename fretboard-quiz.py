import random
import time

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


def get_random_string():
    return random.randrange(1, 7)


def get_random_fret():
    return random.randrange(0, 13)


def generate_start_num(string_num):
    if string_num == 1 or string_num == 6:
        start_num = 7
    elif string_num == 2:
        start_num = 2
    elif string_num == 3:
        start_num = 10
    elif string_num == 4:
        start_num = 5
    elif string_num == 5:
        start_num = 0
    return start_num


def generate_string_notes(string_num):
    start_num = generate_start_num(string_num)
    new_notes = notes[start_num:] + notes[:start_num] + \
        notes[start_num:start_num + 1]
    return new_notes


def generate_question():
    random_string = get_random_string()
    random_fret = get_random_fret()
    print(f"""
    \n***************
    \nString: {random_string}
    \nFret: {random_fret}
    """)
    generate_answer(random_string, random_fret)


def generate_answer(string, fret):
    ordered_notes = generate_string_notes(string)
    answer = ordered_notes[fret]
    user_input = input("\nYour Guess: ").upper()
    generate_response(answer, user_input)


def generate_response(answer, guess):
    if answer == guess:
        print(f"Correct! The answer was {answer}")
    else:
        print(f"Oops! The answer was {answer}")
    time.sleep(3)
    generate_question()


if __name__ == "__main__":
    generate_question()
