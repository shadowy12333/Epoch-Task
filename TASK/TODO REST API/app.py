from flask import Flask,request,jsonify
from storage import load_data,save_data
app=Flask(__name__)
tasks=load_data()#启动前读取

@app.get("/tasks")
def get_tasks():
    return jsonify(tasks)

@app.get("/tasks/<int:task_id>")
#@是python的装饰器语法，作用是把下面的函数“注册”到 Flask 应用中，告诉框架“当满足某个 URL 条件时，调用这个函数”。
def get_task(task_id):
    for task in tasks:
        if task["id"]==task_id:
            return jsonify(task)
        return jsonify({"error:查找不到task"}),404

@app.post("/tasks")
def create_task():
    data=request.get_json()
    if not data or "title" not in data:
        return jsonify("error:缺少title参数"),400
    new_id = max([t["id"]for t in tasks],default=0)+1##
    new_task={
        "id":new_id,
        "title":data["title"],
        "completed":data.get("completed",False)
    }
    tasks.append(new_task)
    save_data(tasks)

    return jsonify(new_task),201

@app.patch("/tasks/<int:task_id>")
def update_task(task_id):
    data=request.get_json()
    if not data:
        return jsonify({"error:请求为空"}),400
    for task in tasks:
        if task["id"]==task_id:
            if "title" in data:
                task["title"] = data["title"]
            if "completed" in data:
                task["completed"] = data["completed"]
            save_data(tasks)#保存
            return jsonify(task)#字典
    return jsonify({"error":"找不到任务"}),404
@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    global tasks#声明全局变量
    for index,task in enumerate(tasks):##
        if task["id"]==task_id:
            deleted=tasks.pop(index)
            save_data(tasks)
            return jsonify({"message":"删除成功","deleted":deleted})
    return jsonify({"error":"找不到任务"})
if __name__=="__main__":
    app.run(debug=True,port=5000)








