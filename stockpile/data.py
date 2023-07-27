import json


def write_data(data: dict, file_path: str=None):
    with open(file_path, 'w') as json_file:
        json_file.write(json.dumps(data))
        json_file.close()


def read_data(file_path: str=None):
    with open(file_path, 'r') as file:
        data = file.read()
        return json.loads(data)


def update_data(to_update: dict, file_path: str=None):
    data = read_data(file_path)

    data.update(to_update)
    write_data(data, file_path)
