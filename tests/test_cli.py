import os 

from stockpile.data import read_data
from stockpile.config import JSON_FILE_PATH


ERASE_DATA_COMMAND = 'python stockpile erase_data'


class TestCli:
    def test_write_object(self):
        cli_command = 'write_object test_key foo=bar'

        os.system(ERASE_DATA_COMMAND)
        os.system(("python stockpile {}".format(cli_command)))

        data = read_data(JSON_FILE_PATH)
        
        assert data == {"test_key": {"foo": "bar"}}

    def test_write_data_writes_on_file(self):
        cli_command = 'write_data a=1 b=2'

        os.system(ERASE_DATA_COMMAND)
        os.system(("python stockpile {}".format(cli_command)))

        data = read_data(JSON_FILE_PATH)

        assert data == {"a": "1", "b": "2"}

    def test_update_object_updates_object(self):
        insert_object_command = 'python stockpile write_object test_object inner_key=test_value'
        update_object_command = 'python stockpile update_object test_object inner_key=TestValue'

        os.system(ERASE_DATA_COMMAND)
        os.system(insert_object_command)
        os.system(update_object_command)

        data = read_data(JSON_FILE_PATH)

        assert data == {'test_object': {'inner_key': 'TestValue'}}

