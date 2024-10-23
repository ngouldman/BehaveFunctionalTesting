import json
import xmltodict
from pathlib import Path

def file_walker(file_path):
    path = Path(file_path)
    for file in path.rglob('*'):
        with open(file, 'r') as data:
                data = data.read()
                data_dict = xmltodict.parse(data)

    return data_dict


