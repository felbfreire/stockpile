import json


def write_data(data: dict, file_path: str=None):
    with open(file_path, 'w') as json_file:
        json_file.write(json.dumps(data))
        json_file.close()


def read_data(file_path: str=None):
    with open(file_path, 'r') as file:
        data = file.read()
        return json.loads(data)

