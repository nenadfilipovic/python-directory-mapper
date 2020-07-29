import os
from pathlib import Path
import requests


class DirectoryMapper:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def send_data(self, payload):
        response = requests.post('', json=payload)
        print(response)

    def list_directory(self):
        directory_list = []
        file_list = []
        files = []
        for (dirpath, dirnames, filenames) in os.walk(self.dir_path):
            directory_list.extend(dirnames)
            file_list.extend(filenames)
        for file in file_list:
            if file.endswith(".txt") and Path(file).stem.isnumeric():
                files.append(file)
        files = [os.path.splitext(each)[0] for each in files]
        self.send_data({'product': directory_list, 'price': files})


o = DirectoryMapper(r"")
o.list_directory()
