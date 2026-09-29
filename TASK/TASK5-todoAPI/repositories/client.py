import requests
import json
BASE_URL="http://127.0.0.1:5000"

def text_api():
    print("创建任务")
    res=requests.post(f"{BASE_URL}/tasks",json={"title":"学习sql"},timeout=5)
    print(f"状态:{res.status_code}")
    print(f"数据:{res.json()}\n")

    print("2，获取任务列表")
    res=requests.get(f"{BASE_URL}/tasks?page=1&limit=5&keyword=SQLite",timeout=5)
    print(f"状态:{res.status_code}")
    print(f"数据:{res.json()}\n")

    print("3，修改任务状态")
    res=requests.patch(f"{BASE_URL}/tasks/1",json={"completed":True},timeout=5)
    print(f"状态{res.status_code}")

    print("4,空标题测试")
    res=requests.post(f"{BASE_URL}/tasks",json={"title":""},timeout=5)
    print(f"状态{res.status_code}")
    print(f"数据:{res.json()}\n")
if __name__=="__main__":
    text_api()
