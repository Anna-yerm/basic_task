class Task2:
    first_arr = []
    second_arr = []

    def __init__(self, first_arr, second_arr):
        self.first_arr = first_arr
        self.second_arr = second_arr

    def is_exist(self, name):
        result = False

        for x in self.second_arr:
            if x == name:
                result = True

        return result

    def first_variant(self):
        new_string = []
        for y in self.first_arr:
            if not self.is_exist(y):
                new_string.append(y)
        print(new_string)

    def second_variant(self):
        print(list(filter(lambda x: x not in self.second_arr, self.first_arr)))
