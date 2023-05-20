FILEPATH = 'Todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return list of to-do items """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items in list within the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def show():
    """ Shows list line by line. """
    with open(FILEPATH, 'r') as file:
        todos_local = file.readlines()

    for i, j in enumerate(todos_local):
        j = j.strip('\n')
        row = f"{i + 1}. {j}"
        print(row)


if __name__ == "__main__":
    print('Hello from modules')
