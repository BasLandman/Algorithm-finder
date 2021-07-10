uppercase_letters_array = [
    'Q', 'W', 'E',
    'R', 'T', 'Y',
    'U', 'I', 'O',
    'P', 'A', 'S',
    'D', 'F', 'G',
    'H', 'J', 'K',
    'L', 'Z', 'X',
    'C', 'V', 'B',
    'N', 'M'
]
lowercase_letters_array = [
    'q', 'w', 'e',
    'r', 't', 'y',
    'u', 'i', 'o',
    'p', 'a', 's',
    'd', 'f', 'g',
    'h', 'j', 'k',
    'l', 'z', 'x',
    'c', 'v', 'b',
    'n', 'm'
]

numbers_array = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '0'
]

file = str(input('file: ')) or 'codes.txt'


class AlgorithmFinder:

    def __init__(self, file_name: str, output_file: str):
        self.file_name = file_name
        self.output_file = output_file
        self.output = {}
        self.output_string = None

    def format_output_string(self) -> None:
        try:
            self.output_string = "0: postition, 1: numbers amount: 2: uppercase amount: 3: lowercase amount" + ''.join(
                [
                    f"\n 0: {i}        1: {self.output[i]['numbers']}       2: {self.output[i]['uppercase_letters']}       3: {self.output[i]['lowercase_letters']}"
                    for i in self.output])
        except Exception:
            print('error printing output')

    def write_output_to_file(self) -> None:
        try:
            with open(str(self.output_file), 'a+') as file:

                file.write(
                    self.output_string
                )

        except Exception:
            print('error writing output to file.')

    def count_cases(self) -> None:
        with open(self.file_name, encoding="'latin-1'") as file:
            for string in file:
                for idx, char in enumerate(str(string.strip())):

                    # uppercase
                    if str(char) in uppercase_letters_array:

                        if idx not in self.output.keys():
                            self.output[idx] = {
                                'numbers': {},
                                'lowercase_letters': {},
                                'uppercase_letters': {}
                            }

                        if char not in self.output[idx]['uppercase_letters']:
                            self.output[idx]['uppercase_letters'][char] = 0

                        if char in self.output[idx]['uppercase_letters']:
                            self.output[idx]['uppercase_letters'][char] += 1

                    # lowercase
                    if str(char) in lowercase_letters_array:

                        if idx not in self.output.keys():
                            self.output[idx] = {'numbers': {}, 'lowercase_letters': {}, 'uppercase_letters': {}}

                        if char not in self.output[idx]['lowercase_letters']:
                            self.output[idx]['lowercase_letters'][char] = 0
                        if char in self.output[idx]['lowercase_letters']:
                            self.output[idx]['lowercase_letters'][char] += 1

                    # numbers
                    if str(char) in numbers_array:
                        if idx not in self.output.keys():
                            self.output[idx] = {'numbers': {}, 'lowercase_letters': {}, 'uppercase_letters': {}}

                        if char not in self.output[idx]['numbers']:
                            self.output[idx]['numbers'][char] = 0
                        if char in self.output[idx]['numbers']:
                            self.output[idx]['numbers'][char] += 1


def main():

    instance = AlgorithmFinder(
        'codes.txt',
        'output.txt'
    )

    instance.count_cases()
    instance.format_output_string()
    instance.write_output_to_file()


if __name__ == '__main__':
    main()
