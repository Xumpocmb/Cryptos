import pyAesCrypt
import os


def encrypt_file():
    folder = input('[/] Введите путь к папке с файлом: ')
    file_name = input('[/] Введите имя файла с расширением: ')
    full_path = os.path.join(folder, file_name)
    # password = getpass(prompt='Введите ваш секретный ключ: ')
    password = input('[/] Введите ваш секретный ключ: ')
    try:
        pyAesCrypt.encryptFile(infile=full_path, outfile=f'{full_path}.aes', passw=password)
        print('\n')
        print(f'Исходный файл: {full_path}\n'
              'Результат операции: Успех!\n'
              f'Зашифрованный файл: {full_path}.aes\n')
    except Exception as ex:
        print(f'Ошибка: {ex}')
    except FileNotFoundError:
        print('Ошибка: Файл не найден!')
