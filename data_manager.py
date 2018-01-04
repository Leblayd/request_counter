import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def data_file_path(file_name):
    return os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else os.path.join(DIR_PATH, file_name)


def get_dict_from_file(filename="request_counts.txt"):
    with open(data_file_path(filename), 'r') as file:
        data = {}
        for line in file:
            data[(line.split(':')[0])] = int(line.split(':')[1][1:-1])
    return data


def write_dict_to_file(data, filename="request_counts.txt"):
    with open(data_file_path(filename), 'w') as file:
        for key in data:
            file.write("{}: {}\n".format(key, data[key]))


if __name__ == '__main__':
    the_data = get_dict_from_file()
    print(the_data)
    write_dict_to_file(the_data)
