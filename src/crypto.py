def ceasar_cipher(mode="encrypt", plain_text="", cipher_text="", shift=3):
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    if mode == "encrypt":
        cipher_text = ""
        for letter in plain_text:
            if letter.isalpha():
                cipher_text += alphabets[alphabets.index(letter) + shift % 26]
            else:
                cipher_text += letter
        return cipher_text

    elif mode == "decrypt":
        plain_text = ""
        for letter in plain_text:
            if letter.isalpha():
                plain_text += alphabets[alphabets.index(letter) - shift % 26]
            else:
                plain_text += letter
        return "abcd"
