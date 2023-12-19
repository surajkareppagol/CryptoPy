alphabets = "abcdefghijklmnopqrstuvwxyz"


def ceasar_cipher(mode="encrypt", text="", shift=3):
    encrypt = True if mode == "encrypt" else False

    result_text = ""
    for letter in text:
        if letter.isalpha() and encrypt:
            result_text += alphabets[alphabets.index(letter) + shift % 26]
        elif letter.isalpha() and not encrypt:
            result_text += alphabets[alphabets.index(letter) - shift % 26]
        else:
            result_text += letter
    return result_text


def vigenere_cipher(mode="encrypt", text="", key=""):
    encrypt = True if mode == "encrypt" else False

    result_text = ""

    shift_values = []
    for letter in key[::-1]:
        shift_values.append(alphabets.index(letter))

    for letter in text:
        shift = shift_values.pop()
        if letter.isalpha() and encrypt:
            shift_position = alphabets.index(letter) + shift % 26
            if shift_position > 25:
                shift_position = shift_position - 26
            result_text += alphabets[shift_position]
        elif letter.isalpha() and not encrypt:
            shift_position = alphabets.index(letter) - shift % 26
            if shift_position > 25:
                shift_position = shift_position + 26
            result_text += alphabets[shift_position]
        else:
            result_text += letter
    return result_text


def transposition_cipher(mode="encrypt", text="", key=""):
    encrypt = True if mode == "encrypt" else False
    result_text = ""

    if encrypt:
        # Create 1st row
        matrix = [list(key)]

        # Create 2nd row
        position_of_keys = [alphabets.index(letter) for letter in key]

        keys_sorted = position_of_keys[::]
        keys_sorted.sort()

        for index, value in enumerate(keys_sorted):
            index_of_key = position_of_keys.index(value)
            position_of_keys[index_of_key] = index

        matrix.append(position_of_keys)

        # Break text and add it to matrix

        total_text_rows = (len(text) // len(key)) + 1
        text_row = []
        text = text + (total_text_rows * len(key) - len(text) + 1) * " "

        for index, letter in enumerate(text):
            if index % len(key) == 0 and index != 0:
                matrix.append(text_row)
                text_row = []
                text_row.append(letter)
            else:
                text_row.append(letter)

        # Create cipher text

        for index, value in enumerate(key):
            index_of_key = matrix[1].index(index)

            for _ in range(2, total_text_rows + 2):
                result_text += matrix[_][index_of_key]
    else:
        # Create 1st row
        matrix = [list(key)]

        # Create 2nd row
        position_of_keys = [alphabets.index(letter) for letter in key]

        keys_sorted = position_of_keys[::]
        keys_sorted.sort()

        for index, value in enumerate(keys_sorted):
            index_of_key = position_of_keys.index(value)
            position_of_keys[index_of_key] = index

        matrix.append(position_of_keys)

        # Break the text

        # Need to add more steps

    return "Still working on it."
