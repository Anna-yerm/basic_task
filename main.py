from task1 import Task1
from task2 import Task2

# Task1

task1 = Task1("C:\study\est")
task1.print_last_modified_files()

# Task2

first_arr = {"Alex", "Dima", "Kate", "Galina", "Ivan"}
second_arr = {"Dima", "Ivan", "Kate"}

task2 = Task2(first_arr, second_arr)

task2.first_variant()
task2.second_variant()