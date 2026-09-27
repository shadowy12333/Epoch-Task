import json
import os
DATA_FILE="data.json"
def load_data():
    """从data,json读数据"""
    if not os.path.exists(DATA_FILE):
        return[]
    try:
        with open(DATA_FILE,"r",encoding="utf-8") as f:
            return json.load(f)#读取
    except json.JSONDecodeError:
        return[]

def save_data(tasks):#实现持久化储存
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(tasks,f,ensure_ascii=False,indent=2)


