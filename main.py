from decorators import logger1

class FlatIterator:

    def __init__(self, nested_list):
        self.result = []
        self.get_result(nested_list)

    def get_result(self, lists):
        for item in lists:
            if isinstance(item, list):
                self.get_result(item)
            else:
                self.result.append(item)

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.result):
            raise StopIteration

        return self.result[self.cursor]


@logger1
def main():
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

if __name__ == '__main__':
    main()
