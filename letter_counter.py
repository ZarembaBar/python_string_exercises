# wwwddeeeesfaawwww

def letters_count(str_ex):
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


def final_parts_add(list_of_parts):
    solution = ""
    for part in list_of_parts:
        solution += str(part)
    return solution


if __name__ == "__main__":
    text = input("Podaj ciąg znaków:")

    x = letters_count(text)
    print(final_parts_add(x))
    