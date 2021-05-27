from datetime import datetime, timedelta
from os import scandir


class Task1:
    def __init__(self, file_directory):
        self.file_directory = file_directory

    def convert_date(self, timestamp):
        d = datetime.utcfromtimestamp(timestamp)
        formated_date = d.strftime('%d %b %Y')
        return formated_date

    def convert_time(self, timestamp):
        d = datetime.utcfromtimestamp(timestamp)
        formated_time = d.strftime('%H:%M:%S')
        return formated_time

    def get_files(self, extension):
        dir_entries = scandir(self.file_directory)
        result = []
        for entry in dir_entries:
            fileformat = entry.name.split(".")[-1]
            if entry.is_file() and fileformat == extension:
                result.append(entry)

        return result

    def print_last_modified_files(self):
        files = self.get_files('txt')
        files.sort(reverse=True, key=lambda x: x.stat().st_mtime)

        print("List of found files with entered extension sorted by date:")
        self.print_array(files)

        result = []

        min_date = datetime.fromtimestamp(files[0].stat().st_mtime) - timedelta(seconds=10)

        for file in files:
            date = datetime.fromtimestamp(file.stat().st_mtime)

            if date > min_date:
                result.append(file)

        print("Files in 10sec:")
        self.print_array(result)

    def print_array(self, files):
        for file in files:
            info = file.stat()
            fileformat = file.name.split(".")[-1]
            print(
                f'{file.name}\t Format: {fileformat}, Last Modified: {self.convert_time(info.st_mtime)} , {self.convert_date(info.st_mtime)}')
