import os
import os.path



class Task3:
    def __init__(self, file_path, row_number):
        self.file_path = file_path
        self.row_number = row_number

    def get_file_name(self):
        return os.path.basename(self.file_path).split(self.get_file_extension())[0]

    def get_file_path(self):
        return os.path.dirname(self.file_path)

    def get_file_extension(self):
        return os.path.splitext(self.file_path)[-1]

    def get_new_file_name(self):
        return self.get_file_name() + '_res' + self.get_file_extension()

    def get_new_file_path(self):
        a = self.get_file_path() + "/" + self.get_new_file_name()
        print(a)
        return a

    def copy_lines_to_new_file(self):
        x = self.row_number
        with open(self.file_path, 'r') as f1:
            data = f1.readlines()

        with open(self.file_path, 'w') as f1:
            for line in data[0:1:]:
                for line1 in data[x+1::]:
                    f1.write(line+line1)

        with open(self.get_new_file_path(), 'w') as f2:
            for line in data[1:x+1:]:
                f2.write(line)


"""for line in data[1:x + 1:]:"""


