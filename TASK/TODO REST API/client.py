
import requests
BASE_URL="http://127.0.0.1:5000"
try :
    print("1,创建测试")
    response=requests.post(f"{BASE_URL}/tasks",json={"title":"学flask"},timeout=5)
    response.raise_for_status()
    """提前拦截错误：在请求失败的第一时间发现问题，而不是等到后续处理数据时才崩溃。
简化代码：不需要手动写 if response.status_code != 200: 这样的判断逻辑。
统一异常处理：可以将所有网络相关的错误（超时、连接失败、HTTP错误）放在同一个 try-except 块中集中处理，让代码更健壮。
"""
    print(f"状态:{response.status_code}")
    print(f"数据:{response.json()}\n")

    print("2.获取所有任务")
    response=requests.get(f"{BASE_URL}/tasks",timeout=5)
    response.raise_for_status()
    print(f"状态:{response.status_code}")
    print(f"数据:{response.json()}\n")

    print("3,获取单个任务(get)")
    response=requests.get(f"{BASE_URL}/tasks/1",timeout=5)#/1指id为1
    response.raise_for_status()
    print(f"状态:{response.status_code}")
    print(f"数据{response.json()}\n")
except requests.HTTPError as e:
    print(f"HTTP错误{e}")
try:
    print("4.修改任务")
    response=requests.patch(f"{BASE_URL}/tasks/1",json={"completed":True},timeout=5)
    response.raise_for_status()
    print(f"状态{response.status_code}")
    print(f"{response.json()}\n")
except requests.exceptions.HTTPError as e:
    print(f"HTTP错误{e}")

    print("5.删任务")
    response=requests.delete(f"{BASE_URL}/tasks/1",timeout=5)
    response.raise_for_status()
    print(f"状态{response.status_code}")
    print(f"{response.json()}\n")


    print("6，任务不存在时")
    response=requests.get(f"{BASE_URL}/tasks/114514",timeout=5)
    print(f"状态:{response.status_code}")
    if response.content:
        try:
            print(f"返回内容:{response.json()}\n")
        except:
            print(f"返回内容不是Json{e}\n")
    else:
        print("返回内容为空")

except requests.HTTPError as e:
    print(f"HTTP错误{e}")
except requests.ConnectionError:
    print("连接失败！你忘记启动 app.py 了吧，杂鱼~")
except Exception as e:
    print(f"出错了qwq{e}")
















