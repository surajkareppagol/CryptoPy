from rich.console import Console
from rich.panel import Panel

from crypto import ceasar_cipher

console = Console()

back = False

console.print(
    Panel(
        "[green]CryptoPy[/green] - A collection of cryptography programs written in python".capitalize()
    )
)

console.print(
    Panel(
        """
    1. Ceasar Cipher
    2. RSA
  """
    )
)


while True:
    option = console.input("1. 📋 Get Info ┆ 2. 🔑 Encypt ┆ 3. 🔓 Decrypt\n👉 Choice: ")

    if option == "1":
        console.clear()
        algortihm = console.input("1. Ceasar Cipher\n\n👉 Choice: ")

        if algortihm == "1":
            console.print(Panel("[green bold]Ceasar Cipher[/green bold]"))
            console.print(
                """👉 In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
            The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communications security.""",
                justify="full",
            )

            back = console.input("0. ⬅️ Go Back\n\n👉 Choice: ")

            if back == "0":
                console.clear()
                continue
    elif option == "2":
        console.clear()
        algortihm = console.input("1. Ceasar Cipher\n\n👉 Choice: ")

        if algortihm == "1":
            console.print(Panel("[green bold]Ceasar Cipher[/green bold]"))
            plain_text = console.input("⌨️ Enter input text: ")
            shift = int(console.input("⚙️ Enter shift value: "))

            cipher_text = ceasar_cipher(plain_text=plain_text, shift=shift)

            console.print(
                Panel(f"The encrypted text is: [green bold]{cipher_text}[/green bold]")
            )

            back = console.input("0. ⬅️ Go Back\n\n👉 Choice: ")

            if back == "0":
                console.clear()
                continue
    elif option == "3":
        console.clear()
        mode = "decrypt"
        algortihm = console.input("1. Ceasar Cipher\n\n👉 Choice: ")

        if algortihm == "1":
            console.print(Panel("[green bold]Ceasar Cipher[/green bold]"))
            cipher_text = console.input("⌨️ Enter cipher text: ")
            shift = int(console.input("⚙️ Enter shift value: "))

            plain_text = ceasar_cipher(mode=mode, cipher_text=cipher_text, shift=shift)

            console.print(
                Panel(f"The decrypted text is: [green bold]{plain_text}[/green bold]")
            )

            back = console.input("0. ⬅️ Go Back\n\n👉 Choice: ")

            if back == "0":
                console.clear()
                continue

    else:
        break


if __name__ == "main":
    pass
