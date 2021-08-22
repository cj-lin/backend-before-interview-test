from collections import Counter


def get_num_of_sorted(strs):
    if not strs:
        print('strs cannot be empty!')
        raise

    if len(strs) > 100:
        print('Too many items in strs!')
        raise

    len_of_str = len(strs[0])

    if not all(map(lambda x: len(x) == len_of_str, strs)):
        print('Not all items in strs are the same!')
        raise

    if len_of_str > 1000:
        print('String in strs is too long!')
        raise

    return Counter(map(lambda x: list(x) == sorted(x), list(zip(*strs))))[False]


if __name__ == '__main__':
    strs = []

    while(True):
        input_str = input('Please put your strings(0 for EOF): ')
        if input_str == '0':
            break
        elif not input_str.islower():
            print('Input is not in lowercase!')
            raise
        strs.append(input_str)

    print(get_num_of_sorted(strs))
