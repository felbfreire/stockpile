import os

from stockpile.data import write_data, read_data


TEST_FILE = 'json_test.json'


class TestData:

    def test_read_data_to_json_file_writes_on_file(self):
        data = {'foo': 'bar', 'goo': 'car'}

        write_data(data, TEST_FILE)

        expected_data = read_data(TEST_FILE)
        os.system('rm %s' % (TEST_FILE))

        assert expected_data == {"foo": "bar", "goo": "car"}

