import json
import pyperclip


with open('source.json') as json_file:
    json_data = json.load(json_file)

with open('source.txt') as csv_file:
    csv_data = csv_file.read().rsplit(sep=',')

with open('input.txt') as user_input:
    user_input_data = user_input.read()


def print_keys(d):
    for k in d:
        print(k)


def print_cols():
    for col in csv_data:
        print(col)


if __name__ == '__main__':
    print(user_input_data)
    type(user_input_data)