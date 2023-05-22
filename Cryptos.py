from art import tprint
from clear_console import clear
from decrypt_file import decrypt_file
from encrypt_file import encrypt_file
import sys

# from getpass import getpass


def print_warning_message():
    print('\n',
          '-'*35,
          '\nВы выбрали опцию для работы с файлом, для которой нужен секретный ключ.\n'
          'На следующем шаге Вам нужно ввести секретный ключ.\n'
          'ОБРАТИТЕ ВНИМАНИЕ: ВВЕДЕННЫЙ ВАМИ СЕКРЕТНЫЙ КЛЮЧ ИСПОЛЬЗУЕТСЯ ДЛЯ ШИФРОВАНИЯ И ДЕШИФРОВАНИЯ\n'
          'Если Вы утеряли или забыли ключ, работа с дешифрованием файла не будет корректной!\n')


def print_app_menu():
    tprint('Cryptos')
    print('[/] Программа для шифрования и дешифрования файлов.\n'
          '[/] Выберите действие:\n'
          '\t1: Шифрование файла\n'
          '\t2: Дешифрование файла\n'
          '\t0: Я запустил эту программу по ошибке, позвольте выйти!\n')


# шифрование файла
def choice_encrypt_file():
    print_warning_message()
    encrypt_file()
    choice_after()


# дешифрование файла
def choice_decrypt_file():
    print_warning_message()
    decrypt_file()
    choice_after()


def choice_after():
    print('\n'
          '1: Главное меню\n'
          '0: Выход из программы\n')
    user_choice = input('\tВаш выбор?.. ')
    if user_choice == '1':
        clear()
        main()
    else:
        exit_app()


def exit_app():
    clear()
    print('\n',
          '-' * 35,
          '\n\tХороший выбор ;), до свидания!')
    sys.exit()


def main():
    print_app_menu()

    user_choice = input('\tВаш выбор?.. ')
    if user_choice == '1':
        choice_encrypt_file()
    elif user_choice == '2':
        choice_decrypt_file()
    elif user_choice == '0':
        exit_app()


if __name__ == '__main__':
    main()
