from .txt_reader import read_txt_file
import json

def read_json_file(path: str) -> str:
    data = read_txt_file(path)
    data = json.loads(data)

    return data
