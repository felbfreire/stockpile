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

