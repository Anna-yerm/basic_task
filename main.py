from task1 import Task1
from task2 import Task2
from task3 import Task3

# Task1

task1 = Task1("C:\study\est")
task1.print_last_modified_files()

# Task2

first_arr = {"Alex", "Dima", "Kate", "Galina", "Ivan"}
second_arr = {"Dima", "Ivan", "Kate"}

task2 = Task2(first_arr, second_arr)

task2.first_variant()
task2.second_variant()


# Task3

file_path1 = 'C:/study/task3/test_file.txt'
row_number1 = 3

task3 = Task3(file_path1, row_number1)

task3.copy_lines_to_new_file()
