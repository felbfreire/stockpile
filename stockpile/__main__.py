from config import JSON_FILE_PATH
from data import read_data


if __name__ == '__main__':
    print('\nHello from Mr. Thomas Stockpile\n')

    data_dic = read_data(JSON_FILE_PATH)

    for key in data_dic:
        print('%s: %s' % (key, data_dic[key]))

