import json
import pyperclip


# --- HANDLE JSON --- #


# '/Users/david/Documents/dev/python_scripting/transform_into_markdown_table/input_source_files/source.json'
with open('./input_source_files/source.json') as json_file:
    json_data = json.load(json_file)


def print_keys(d):
    for k in d:
        print(k)


keys = [k for k in json_data]


# --- HANDLE CSV --- #


with open('./input_source_files/csv_headers.txt') as csv_headers:
    csv_cols = csv_headers.read().rsplit(sep=',')


def print_cols():
    for col in csv_cols:
        print(col)


# --- GET MANUAL INPUT AS LINES --- #


with open('./input_source_files/input.txt') as user_input:
    file_input = [line.strip('\n') for line in user_input.readlines()]


# --- CREATE MARKDOWN TABLE --- #


def get_three_col_md_table(list_of_column_headers):
    rows = [f' {row} ||' for row in list_of_column_headers]
    rows.insert(0, 'Field | Description | Comment')
    rows.insert(1, '--- | --- | ---')
    return '''{}'''.format('\n'.join(rows))


def print_table(table):
    for row in table:
        print(row)


if __name__ == '__main__':
    # print to console to check
    print_keys(json_data)

    # Prepare Data
    md_input_table = get_three_col_md_table(file_input)
    md_json_table = get_three_col_md_table(keys)

    # Copy table to clipboard
    pyperclip.copy(md_json_table)