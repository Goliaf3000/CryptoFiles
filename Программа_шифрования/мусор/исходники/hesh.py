import hashlib
import sys
import os
sys.stdout._encoding = 'utf-8'
file = input('Выберите ключевой файл - ')
file_size = os.path.getsize(file) + 12
failHash = str(file_size)
hash_object = hashlib.md5(failHash.encode())
a = hash_object.hexdigest()
print(a) 