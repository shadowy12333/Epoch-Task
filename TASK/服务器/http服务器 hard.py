#查数据
import requests#引用库，开场白   request库中方法小写
import socket
url = "http://127.0.0.1:5002"#定位网站
params={"userId":1}#自动编码成 ?userId=1 的形式，拼接到请求 URL 的末尾

try:
    response=requests.get(url,params=params,timeout=5)
    ##params=params：可选参数，以字典形式传递 URL 查询字符串。requests 会自动将其编码并拼接到 URL 后面。例如 params={'wd': 'python', 'page': 1} 会被拼接为 ?wd=python&page=1。
    response.raise_for_status()#依旧返回状态码
    data=response.json()#将服务器返回的 JSON 格式字符串解析为当前编程语言中可直接操作的原生数据结构
    print(f"网页状态是:{response.status_code}")#状态码
    print(f"拿到了:{len(data)}条")
    print(data)
    print(type(data))
except requests.Timeout:
    print("太jb慢了!")
except requests.ConnectionError:
    print("你的网络有问题")
except requests.HTTPError as e:
    print(f"http地址错误:{e}")
except Exception as e:
    print(f"发生未知错误:{e}")


print("--------------------------------------")
url="https://jsonplaceholder.typicode.com/posts"
payload={
    "title":"今天学http",
    "body":"我去,学不懂",
"userId":1
}#整一个json格式的给你加个请求头
try:
    response=requests.post("url.json=payload,timeout=5")
    response.raise_for_status()

    print(f"状态码:{response.status_code}")
    print(f"新数据:{response.json()}\n")
except requests.HTTPError as e:
    print(f"数据有问题{e.response.status_code}")
except Exception as e:
    print(f"报错{e}")

try:
    response=requests.get("https://jsonplaceholder.typicode.com/thisis_not_exist",timeout=5)
    response.raise_for_status()
except requests.HTTPError as o:
    print(f"look it by your self  {o.response.status_code}")
except requests.Timeout:
    print("链接超时")

