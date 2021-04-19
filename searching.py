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
#


def main():
    sequential_data = print(read_data("sequential.json", "unordered_numbers"))
    return sequential_data


if __name__ == '__main__':
    main()