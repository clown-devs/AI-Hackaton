import os
import shutil

def copy_files(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir + "/rec")
        os.makedirs(target_dir + "/not_rec")

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            old_file_path = os.path.join(root, file)
            # Разделяем путь на части
            path_parts = root.split(os.sep)
            # Используем только нужные нам части для создания нового имени файла
            new_file_name = ''.join(path_parts[1:]) + os.path.splitext(file)[0]
            # Удаляем пробелы из нового имени файла

            if file.endswith('.REC'):
                new_file_name = new_file_name.replace(' ', '') + '.REC'
                new_file_path = os.path.join(target_dir + "/rec", new_file_name)
            else:
                new_file_name = new_file_name.replace(' ', '') + os.path.splitext(file)[1]
                new_file_path = os.path.join(target_dir + "/not_rec", new_file_name)
            shutil.copy2(old_file_path, new_file_path)


import sys

if len(sys.argv) != 3:
    print("Usage: python main.py <dataset_path> <output_dir>")
    sys.exit(1)


input_file = sys.argv[1]
output_file = sys.argv[2]

copy_files(input_file, output_file)