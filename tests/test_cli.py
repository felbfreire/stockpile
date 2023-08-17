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

