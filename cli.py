import functions
import time

time_date = time.strftime("%d %m %Y - %H:%M:%S")
print("It is", time_date)

while True:

    order = input('Add, show, edit, exit or complete: ').strip().capitalize()

    if order.startswith('Add'):
        todo = order[4:].capitalize() + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(filepath='Todos.txt', todos_arg=todos)

        todos = functions.get_todos()

        functions.show()

    elif order.startswith('Show'):

        todos = functions.get_todos()

        functions.show()

    elif order.startswith('Edit'):
        try:
            todos = functions.get_todos()

            number = int(order[5:])
            number = number - 1

            NewItem = input('What is this new item? ')
            todos[number] = NewItem.strip().capitalize() + '\n'

            functions.write_todos(todos)

            print(f'Great, your new list is now composed of:')

            todos = functions.get_todos()

            functions.show()

        except ValueError:
            print('Your command is not valid')
            continue

    elif order.startswith('Complete'):
        try:
            todos = functions.get_todos()

            number = int(order[8:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            print(f'The item {todo_to_remove} has now been completed. Your list is now:')

            functions.write_todos(todos)

            todos = functions.get_todos()

            functions.show()

        except (IndexError, ValueError):
            print('This item is not within the current scope of the list')
            continue

    elif order.startswith('Exit'):
        break

    else:
        print('That command is not valid')
        continue

print('Bye!')