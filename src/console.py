import json

from rich.console import Console
from rich.panel import Panel

from crypto import *

with open("src/crypto.json", "r") as file:
    data = json.loads(file.read())

console = Console()

console.clear()

back = False

console.print(
    Panel(
        "[green]CryptoPy[/green] - A Collection Of Cryptography Programs Written In Python"
    )
)

console.print(Panel("1. Ceasar Cipher\n2. Vigenère cipher\n3. Transposition Cipher"))


while True:
    option = console.input("\n1. 📋 Get Info ┆ 2. 🔑 Encypt ┆ 3. 🔓 Decrypt\n👉 Choice: ")

    # Get info
    if option == "1":
        console.clear()
        console.print(
            Panel("1. Ceasar Cipher\n2. Vigenère cipher\n3. Transposition Cipher")
        )
        choice = int(console.input("\n\n👉 Choice: ")) - 1

        console.clear()
        console.print(
            Panel(
                f"[green bold]{data['data'][choice]['title'].capitalize()}[/green bold]"
            )
        )
        console.print(f"👉 {data['data'][choice]['description']}", justify="full")

    # Encrypt
    elif option == "2":
        console.clear()
        console.print(
            Panel("1. Ceasar Cipher\n2. Vigenère cipher\n3. Transposition Cipher")
        )
        choice = int(console.input("\n\n👉 Choice: ")) - 1

        console.print(
            Panel(
                f"[green bold]{data['data'][choice]['title'].capitalize()}[/green bold]"
            )
        )

        if choice == 0:
            plain_text = console.input("⌨️ Enter input text: ")
            shift = int(console.input("⚙️ Enter shift value: "))
            cipher_text = ceasar_cipher(text=plain_text, shift=shift)

        elif choice == 1:
            plain_text = console.input("⌨️ Enter input text: ")
            key_text = console.input("🔑 Enter the key: ")
            cipher_text = vigenere_cipher(text=plain_text, key=key_text)

        elif choice == 2:
            plain_text = console.input("⌨️ Enter input text: ")
            key_text = console.input("🔑 Enter the key: ")
            cipher_text = transposition_cipher(text=plain_text, key=key_text)

        console.print(
            Panel(f"The encrypted text is: [green bold]{cipher_text}[/green bold]")
        )

    # Decrypt
    elif option == "3":
        console.clear()
        console.print(
            Panel("1. Ceasar Cipher\n2. Vigenère cipher\n3. Transposition Cipher")
        )
        choice = int(console.input("\n\n👉 Choice: ")) - 1
        mode = "decrypt"

        console.print(
            Panel(
                f"[green bold]{data['data'][choice]['title'].capitalize()}[/green bold]"
            )
        )

        if choice == 0:
            cipher_text = console.input("⌨️ Enter cipher text: ")
            shift = int(console.input("⚙️ Enter shift value: "))
            plain_text = ceasar_cipher(mode=mode, text=cipher_text, shift=shift)

        elif choice == 1:
            cipher_text = console.input("⌨️ Enter input text: ")
            key_text = console.input("🔑 Enter the key: ")
            plain_text = vigenere_cipher(mode=mode, text=cipher_text, key=key_text)

        elif choice == 2:
            cipher_text = console.input("⌨️ Enter input text: ")
            key_text = console.input("🔑 Enter the key: ")
            plain_text = transposition_cipher(mode=mode, text=cipher_text, key=key_text)

        console.print(
            Panel(f"The decrypted text is: [green bold]{plain_text}[/green bold]")
        )
    else:
        console.clear()
        break

    back = console.input("0. ⬅️ Go Back\n\n👉 Choice: ")

    if back == "0":
        console.clear()
        continue


if __name__ == "main":
    pass
