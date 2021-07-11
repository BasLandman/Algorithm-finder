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


class AlgorithmFinder:

    def __init__(self, file_name: str, output_file: str):
        self.file_name = file_name
        self.output_file = output_file
        self.output = {}
        self.file_length = None
        self.count_cases_string = None
        self.average_uppercase_expected = None
        self.average_lowercase_expected = None
        self.average_number_expected = None

    def write_output_to_file(self) -> None:
        try:
            with open(str(self.output_file), 'a+') as file:

                file.write(
                    self.count_cases_string
                )

        except Exception:
            print('error writing output to file.')

    def get_file_length(self) -> None:
        with open(self.file_name, encoding="'latin-1'") as file:
            self.file_length = len(file.readlines())

    def get_average_expected(self) -> None:
        """calculates the average characters suppost to be appearing in the strings if the algorithm is complete random."""

        self.average_number_expected = self.file_length / len(numbers_array)
        self.average_lowercase_expected = self.file_length / len(lowercase_letters_array)
        self.average_uppercase_expected = self.file_length / len(uppercase_letters_array)

    def count_cases(self) -> None:
        """"Count how many times a character appears in specific positions of a list of strings."""

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

        self.count_cases_string = "0: { string position }, 1: { Numbers: Appear amount }: 2: { UppercaseLetter: Appear amount } 3: { LowercaseLetter: Appear amount }" \
                                  + ''.join([
            f"\n 0: {i}        1: {self.output[i]['numbers']}       2: {self.output[i]['uppercase_letters']}       3: {self.output[i]['lowercase_letters']}"
            for i in self.output])


def main():
    instance = AlgorithmFinder(
        'codes.txt',
        'output.txt'
    )
    instance.write_output_to_file()

    instance.count_cases()

    print(instance.count_cases_string)

    instance.get_file_length()

    instance.get_average_expected()
    print(instance.average_uppercase_expected)
    print(instance.average_lowercase_expected)
    print(instance.average_number_expected)

if __name__ == '__main__':
    main()
