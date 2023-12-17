import json

from rich.console import Console
from rich.panel import Panel

from crypto import ceasar_cipher

with open("src/crypto.json", "r") as file:
    data = json.loads(file.read())

console = Console()

back = False

console.print(
    Panel(
        "[green]CryptoPy[/green] - A Collection Of Cryptography Programs Written In Python"
    )
)

console.print(Panel("1. Ceasar Cipher\n2. RSA"))


while True:
    option = console.input("1. 📋 Get Info ┆ 2. 🔑 Encypt ┆ 3. 🔓 Decrypt\n👉 Choice: ")

    # Get info
    if option == "1":
        console.clear()
        choice = int(console.input("1. Ceasar Cipher\n\n👉 Choice: ")) - 1

        console.print(
            Panel(
                f"[green bold]{data['data'][choice]['title'].capitalize()}[/green bold]"
            )
        )
        console.print(f"👉 {data['data'][choice]['description']}", justify="full")

    # Encrypt
    elif option == "2":
        console.clear()
        choice = int(console.input("1. Ceasar Cipher\n\n👉 Choice: ")) - 1

        if choice == 0:
            console.print(
                Panel(
                    f"[green bold]{data['data'][choice]['title'].capitalize()}[/green bold]"
                )
            )
            plain_text = console.input("⌨️ Enter input text: ")
            shift = int(console.input("⚙️ Enter shift value: "))

            cipher_text = ceasar_cipher(text=plain_text, shift=shift)

            console.print(
                Panel(f"The encrypted text is: [green bold]{cipher_text}[/green bold]")
            )

    # Decrypt
    elif option == "3":
        console.clear()
        mode = "decrypt"
        choice = console.input("1. Ceasar Cipher\n\n👉 Choice: ")

        if choice == "1":
            console.print(Panel("[green bold]Ceasar Cipher[/green bold]"))
            cipher_text = console.input("⌨️ Enter cipher text: ")
            shift = int(console.input("⚙️ Enter shift value: "))

            plain_text = ceasar_cipher(mode=mode, text=cipher_text, shift=shift)

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
