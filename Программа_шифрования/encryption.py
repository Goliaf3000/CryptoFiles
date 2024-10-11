import pyAesCrypt
import os
import hashlib
import sys
sys.stdout._encoding = 'utf-8'


#поиск размера ключевого файла и преобразование его в хэш


# функция шифрования файла
def encryption(cryptfile, keys):

    # задаём размер буфера
    buffer_size = 512 * 1024
    chek = cryptfile.find(".crp")
    if chek <= 0:
    # вызываем метод шифрования
        pyAesCrypt.encryptFile(
         str(cryptfile),
          str(cryptfile) + ".crp",
         keys,
          buffer_size
        )
    # чтобы видеть результат выводим на печать имя зашифрованного файла
    # удаляем исходный файл
        os.remove(cryptfile)
        return("Файл зашифрован")
    else: return("Файл уже зашифрован")

# функция сканирования директорий
def walking_by_dirs(dir, keys):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        # если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, keys)
                return (encryption(path, keys))
            except Exception as ex:
                return("Файл зашифрован")
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, keys)
def get(a,b,c):            
    cryptfile = a
    file = b
    password = c
    file_size = os.path.getsize(file)
    failHash = str(file_size) + password
    hash_object = hashlib.md5(failHash.encode())
    keys = hash_object.hexdigest()
    digits = '1234567890'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '!@#$%^&*()-+'
    acceptable = digits+upper_letters+lower_letters+symbols

    passwd = set(password)
    if any(char not in acceptable for char in passwd):
        return('Ошибка. Запрещенный спецсимвол')
    else:
        recommendations = []
        if len(password) < 6:
            recommendations.append(f'увеличить число символов - {6-len(password)}')
        for what, message in ((digits,        'цифру'),
                              (symbols,       'спецсимвол'),
                              (upper_letters, 'заглавную букву'),
                              (lower_letters, 'строчную букву')):
            if all(char not in what for char in passwd):
                recommendations.append(f'добавить 1 {message}')

        if recommendations:
            return 'Слабый пароль:', '\n'", ".join(recommendations)
        else:
            return (walking_by_dirs(cryptfile, keys))
            
    