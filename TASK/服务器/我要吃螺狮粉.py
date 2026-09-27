import requests
url="https://jsonplaceholder.typicode.com/posts"
payload={"food":"螺狮粉","数目":1}
response=requests.post(url,json=payload)
print(f"状态是{response.status_code}")
