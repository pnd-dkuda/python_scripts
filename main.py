import subprocess


def get_scp_command(identity, source, destination, files=None):
    return f'scp -i {identity} {source}{files} {destination}'


def read_lines_from_file(list_of_files):
    lines = []
    with open(list_of_files) as files:
        for file in files:
            lines.append(file.strip('\n'))

    return lines


if __name__ == '__main__':
    pass
