import os
import json


# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    # with open(file_path) as f:
    #     data = dict(json.load(f))
    #     if field in data.keys():
    #         return field
    #     # ???
    #     else:
    #         return None
    with open(file_path, "r") as json_file:
        seq = json.load(json_file)
        return seq[field]

def linear_search(sequence, cislo):
    positions = []
    count = 0
    for idx, prvok in enumerate(sequence):
        if prvok == cislo:
            count += 1
            positions.append(idx)
        else:
            continue
    return {"positions": positions, "count": count}
#     ako z toho spravím slovník?

    # indices = []
    # count = 0
    # idx = 0
    # while idx < len(sequence):
    #     if sequence[idx] == cislo:
    #         indices.append(idx)
    #         count += 1
    #     idx += 1
    #
    # return {"position": indices, "count": count}

def pattern_search(seq, pattern):
    """
    
    :param seq: 
    :param pattern: 
    :return: 
    """""
    found = set()
    pattern_size = len(pattern)

    left_idx = 0
    right_idx = 0

    while right_idx < len(seq):
        for idx in range(pattern_size):
            if pattern[idx] != seq[left_idx +idx]:
                break
        #         breakom sa posunieme o ďalší index
        else:
            found.add(left_idx + pattern_size//2)
        #         funguje len v prípade lichých prvkov, ak je sudé, dáme celočíselné

        left_idx = left_idx +1
        right_idx = right_idx +1
    # for idx, prvok in enumerate(seq):
    #     if prvok == pattern:
    #         count += 1
    #         found.add(idx)
    #     else:
    #         continue
    return found

def binary_search(zoznam_c, cislo):

    left, right = (0, len(zoznam_c)-1)
    while left <= right:
        middle = (right + left)//2

        if cislo < zoznam_c[middle]:
            right = middle -1
        elif cislo > zoznam_c[middle]:
            left = middle +1
        else:
            return middle
    return





def main():
    number = 5
    sequential_data = (read_data("sequential.json", "unordered_numbers"))

    positions = (linear_search(sequential_data, number))
    print(positions)

    found = pattern_search(sequential_data, pattern=...)
    print(found)

    zoznam_c = read_data("sequential.json", "ordered_numbers")
    number_pas = binary_search(zoznam_c, cislo=5)

    return sequential_data, positions


if __name__ == '__main__':
    main()