from sys import argv

from config import JSON_FILE_PATH
from data import read_data, write_data


def main():
    if argv[1] == 'read_data':
        data_dic = read_data(JSON_FILE_PATH)

        for key in data_dic:
            print('%s: %s' % (key, data_dic[key]))

