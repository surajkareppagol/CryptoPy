def ceasar_cipher(mode="encrypt", text="", shift=3):
    alphabets = "abcdefghijklmnopqrstuvwxyz"

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
