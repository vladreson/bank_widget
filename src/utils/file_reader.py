import json
from pathlib import Path
from typing import Dict
from typing import List
from typing import Union


def read_json_file(file_path: Union[str, Path]) -> List[Dict]:

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
