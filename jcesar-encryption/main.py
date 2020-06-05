# GLOBAL VARIABLES
chars = '!¡¿?áéíóúabcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'


def encrypt(message, seed):
    encrypted_message = ''
    for letter in message:
        if letter == ' ':
            encrypted_message += '$'
        else:
            i = chars.find(letter)
            j = (i + seed) % len(chars)
            encrypted_message += chars[j]
    return encrypted_message


def decrypt(message, seed):
    decrypted_message = ''
    for letter in message:
        if letter == '$':
            decrypted_message += ' '
        else:
            i = chars.find(letter)
            j = (i - seed) % len(chars)
            decrypted_message += chars[j]
    return decrypted_message


# UTILS
def print_encrypted_message(encrypted_message):
    print("------------------")
    print("Mensaje encriptado")
    print(encrypted_message)


def print_decrypted_message(decrypted_message):
    print("---------------------")
    print("Mensaje desencriptado")
    print(decrypted_message)


def invalid_seed():
    print("-----------------")
    print("Semilla invalida")
    print("-----------------")


def invalid_choice():
    print("-----------------")
    print("Elección invalida")


# MAIN
def main():
    print('Si desea copiar y pegar los mensajes encriptados,')
    print('debe hacerlo con los botones del mouse')
    print('Los atajos CTRL + C y CTRL + V no funcionan')
    print('Puede encriptar mensajes usando espacios y los siguientes carácteres:')
    print(chars)
    while True:
        print("----------------------")
        print('Cifrado de Julio Cesar')
        print('1. Encriptar')
        print('2. Desencriptar')
        try:
            choice = int(input('Elección: '))
            # ENCRYPT
            if choice == 1:
                message = str(input('Mensaje a encriptar: '))
                seed = int(input('Semilla: '))
                # VALIDATE SEED
                while seed <= 0:
                    invalid_seed()
                    seed = int(input('Semilla: '))
                encrypted_message = encrypt(message, seed)
                print_encrypted_message(encrypted_message)
            # DECRYPT
            elif choice == 2:
                message = str(input('Mensaje a desencriptar: '))
                seed = int(input('Semilla: '))
                # VALIDATE SEED
                while seed <= 0:
                    invalid_seed()
                    seed = int(input('Semilla: '))
                decrypted_message = decrypt(message, seed)
                print_decrypted_message(decrypted_message)
            # INVALID CHOICE
            else:
                invalid_choice()
        except:
            invalid_choice()


if __name__ == "__main__":
    main()
