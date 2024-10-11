import pyAesCrypt
import os
import hashlib
import sys
sys.stdout._encoding = 'utf-8'


#поиск размера ключевого файла и преобразование его в хэш


# функция шифрования файла
def decryption(cryptfile, keys):

    # задаём размер буфера
    buffer_size = 512 * 1024
    chek = cryptfile.find(".crp")
    if chek > 0:
    # вызываем метод шифрования
        pyAesCrypt.decryptFile(
          str(cryptfile),
          str(os.path.splitext(cryptfile)[0]),
         keys,
         buffer_size
     )
    # чтобы видеть результат выводим на печать имя зашифрованного файла
        print("[Файл '" + str(os.path.splitext(cryptfile)[0]) + "' расшифрован]")

    # удаляем исходный файл
        os.remove(cryptfile)
    else: print ("файлы не зашифрованы")

# функция сканирования директорий
def walking_by_dirs(dir, keys):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                decryption(path, keys)
            except Exception as ex:
                print(ex)
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
    walking_by_dirs(cryptfile, keys)
    return ("Файл успешно расшифрован")