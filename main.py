from lexic import Lexic


def read_file(file_name: str) -> str:
    """Reads a file and splits it by \\n."""
    try:
        with open(file_name, mode='r') as f:
            return ''.join(f.readlines()).replace('\n', '')
    except FileNotFoundError:
        return ''


def main() -> int:
    lexic = Lexic()

    file = read_file('./source_code.txt')

    lexic.read(file)


if __name__ == '__main__':
    main()
