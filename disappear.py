import os

# allows deleting to work
os.system('')


def delete_line(line_to_delete: str):
    delete_length = len(line_to_delete) + 1
    print('\033[F' + ' ' * delete_length +
          '\b' * delete_length, end="")


def delete_lines(lines_to_delete: str):
    lines = lines_to_delete.split('\n')
    for line in lines:
        delete_line(line)


def disappearing_input(prompt: str):
    value = input(prompt)
    delete_line(prompt + value)
    return value
