import subprocess


class SSHConfig:

    def __init__(self, identity, remote, destination):
        self.identity = identity
        self.remote = remote
        self.destination = destination

    def get_scp_command(self, file):
        return f'scp -i {self.identity} {self.remote}{file} {self.destination}'


sample_config = SSHConfig(
    identity='~/.ssh/server',
    remote='root@server:/home/x/y/',
    destination='~/Desktop/scp/'
)


def read_lines_from_file(list_of_files):
    lines = []
    with open(list_of_files) as files:
        for file in files:
            lines.append(file.strip('\n'))

    return lines


if __name__ == '__main__':
    pass