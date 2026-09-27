import json
from pathlib import Path
DATA_FILE=Path("C:/Users/SHARKER8/Desktop/todo.app/data")
def load_data():
    if not DATA_FILE.exists():
        return []
    try:
        content = DATA_FILE.read_text(encoding="utf-8")
        return json.loads(content)
    except json.JSONDecodeError:
        print("check your words!")
        return []
def save_data(tasks):
    json_string=json.dumps(tasks,ensure_ascii=False,indent=3)##
    DATA_FILE.write_text(json_string,"utf-8")




