# wwwddeeeesfaawwww
from typing import List
def letters_count(str_ex : str) -> List[str]:
    letter_tmp = str_ex[0]
    letter_counter = 0
    solutions = []

    for letter in str_ex:
        if letter == letter_tmp:
            letter_counter += 1
        else:
            solutions.append(str(letter_counter) + letter_tmp)
            letter_tmp = letter
            letter_counter = 1
    solutions.append(str(letter_counter) + letter_tmp)
    return solutions


def string_validation(string: str):
    while len(string) == 0:
        string = input("Zbyt krótki ciąg znaków. Podaj dłuższy: ")
    return string


if __name__ == "__main__":
    text = input("Podaj ciąg znaków:")
    validated_text = string_validation(text)
    x = letters_count(validated_text)
    print("".join(x))
