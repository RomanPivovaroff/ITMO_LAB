import timeit

tasksList = ['main_task', 'task1', 'task2']

for name in tasksList:
    print(name + ": ", timeit.timeit(f'import {name};{name}.main()',number=100))