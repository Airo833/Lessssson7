#Задание 1

import os

pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in pattern.items():
    if os.path.exists(root):
        print(root, 'существует')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            if os.path.exists(cur_dir):
                print(cur_dir, 'существует')
            else:
                os.makedirs(cur_dir)

#my_project существует

#Задание 2

'Thadanie 2'

#Задание 3

#Задание 4

import os
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0

for file in files:
        out_dict[10 ** len(str(file))] += 1


print(out_dict)

#{10: 69, 100: 35, 1000: 439, 10000: 1204, 100000: 679, 1000000: 76, 10000000: 3, 100000000: 1}

#Задание 5