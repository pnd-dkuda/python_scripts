import json
import pyperclip

with open('source.json') as json_file:
    json_data = json.load(json_file)

with open('source.txt') as csv_file:
    csv_data = csv_file.read().rsplit(sep=',')

with open('input.txt') as user_input:
    table_lines = [' ' + line.strip('\n') + ' ||' for line in user_input.readlines()]
    table_lines.insert(0, 'Field | Description | Comment')
    table_lines.insert(1, '--- | --- | ---')


def print_keys(d):
    for k in d:
        print(k)


def print_cols():
    for col in csv_data:
        print(col)


def print_table():
    for row in table_lines:
        print(row)


multi_liner = '''{}'''.format('\n'.join(table_lines))

if __name__ == '__main__':
    print_table()
    pyperclip.copy(multi_liner)