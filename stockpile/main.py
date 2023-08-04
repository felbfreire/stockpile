from sys import argv

from config import JSON_FILE_PATH
from data import read_data, write_data


def main():
    if argv[1] == 'read_data':
        data_dic = read_data(JSON_FILE_PATH)

        for key in data_dic:
            print('%s: %s' % (key, data_dic[key]))

    if argv[1] == 'write_data':
        argv_starts_at = 2
        new_data = dict()
        json_data = read_data(JSON_FILE_PATH)

        for string_index in range(argv_starts_at, len(argv)):
            key, value = argv[string_index].split('=')
            new_data[key] = value
            json_data.update(new_data)

            write_data(json_data, JSON_FILE_PATH)

    if argv[1] == 'write_object':
        argv_starts_at = 2
        object_key = None
        json_object = dict()
        json_data = read_data(JSON_FILE_PATH)

        for string_index in range(argv_starts_at, len(argv)):
            if string_index == 2:
                object_key = argv[string_index]
            else:
                 key, value = argv[string_index].split('=')
                json_object.update({key: value})

        json_data[object_key] = json_object
        write_data(json_data, JSON_FILE_PATH)

