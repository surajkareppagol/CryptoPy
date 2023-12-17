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
