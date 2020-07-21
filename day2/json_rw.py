import sys
import json

def to_json(l: list,file_name:str) -> None:
    with open(file_name,'w') as handle:
        json.dump(l, handle, indent=4)

def read_json(filename: str) -> list:
    with open(filename, 'r') as handle:
        l = json.load(handle)
    return l

