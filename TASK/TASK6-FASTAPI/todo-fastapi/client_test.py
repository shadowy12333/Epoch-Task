import requests

BASE_URL="http://127.0.0.1:8000"
res=requests.post(f"{BASE_URL}/auth/register",json={"username":"senpai","password":"xiabeize114514"},timeout=5)
print("注册",res.status_code,res.json())

res=requests.post(f"{BASE_URL}/auth/login",data={"username":"senpai","password":"xiabeize114514"},timeout=5)
print("登录",res.status_code,res.json())
token=res.json()["access_token"]

headers={"Authorization":f"Bearer {token}"}
res=requests.get(f"{BASE_URL}/auth/me",headers=headers,timeout=5)##
print("我的信息 ",res.status_code,res.json())

res=requests.post(f"{BASE_URL}/tasks",headers=headers,json={"title":"国庆节狠狠玩Minecraft"},timeout=5)
print("创建任务",res.status_code,res.text)

res=requests.get(f"{BASE_URL}/tasks",headers=headers,timeout=5)
print("任务列表",res.status_code,res.json())
#无token测试
res=requests.get(f"{BASE_URL}/tasks",timeout=5)
print("猜猜我成功没？",res.status_code,res.json())
