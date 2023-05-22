import pyAesCrypt
import os
from pathlib import Path


def decrypt_file():
    folder = input('[/] Введите путь к папке с файлом: ')
    file_name = input('[/] Введите имя файла с расширением: ')
    full_path = os.path.join(folder, file_name)
    new_file_name = 'decrypted_' + os.path.splitext(file_name)[0]
    try:
        if Path(os.path.join(folder, new_file_name)).is_file():
            raise Exception('\nВНИМАНИЕ, ОШИБКА:\n'
                            'Дешифрованный файл уже существует!\n'
                            'Во избежание потери данных дешифрация не осуществлена.\n'
                            'Проверьте директорию на наличие файла.\n')
        else:
            # password = getpass(prompt='Введите ваш секретный ключ: ')
            password = input('[/] Введите ваш секретный ключ: ')
            pyAesCrypt.decryptFile(infile=full_path, outfile=f'{os.path.join(folder, new_file_name)}', passw=password)
            print(f'\nИсходный файл: {full_path}\n'
                  'Результат операции: Успех!\n'
                  f'Дешифрованный файл: {os.path.join(folder, new_file_name)}\n')
    except FileNotFoundError:
        print('Ошибка: Файл не найден!')
    except Exception as ex:
        print(ex)
