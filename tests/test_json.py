import os

from stockpile.data import write_data, read_data, update_data


TEST_FILE = 'json_test.json'


class TestData:

    def test_read_data_to_json_file_writes_on_file(self):
        data = {'foo': 'bar'}

        write_data(data, TEST_FILE)

        expected_data = read_data(TEST_FILE)
        os.system('rm %s' % (TEST_FILE))

        assert expected_data == {"foo": "bar"}


    def test_update_data_updates_json_file(self):
        initial_data = {'foo': 'bar'}
        new_data = {'foo': 'lol'}

        write_data(initial_data, TEST_FILE)
        update_data(new_data, TEST_FILE)

        assert read_data(TEST_FILE) == {"foo": "lol"}
