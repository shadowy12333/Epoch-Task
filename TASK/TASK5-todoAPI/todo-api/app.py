from flask import Flask,request,jsonify
from repositories.database import init_db
from repositories.tasks import(
create_task,get_all_tasks,get_task_by_id,
update_task,delete_task,delete_task
)
app=Flask(__name__)
init_db()

@app.get("/tasks")
def list_tasks():
    try:
        page=int(request.args.get("page",1))#request.args的作用是把？后的值赋予进去
        limit=int(request.args.get("limit",10))
    except ValueError:
        return jsonify({"error":"输入的得是数字"}),400
    keyword = request.args.get("keyword","").strip()
    completed_str=request.args.get("completed","").strip()
    completed=None#初始化占位，不过滤标记。“我现在还不知道用户到底想筛选什么，等后面解析完再赋值。”
    if completed_str.lower()=="true":
        completed=True
    elif completed_str.lower()=="false":
        completed=False

    tasks=get_all_tasks(page=page,limit=limit,keyword=keyword,completed=completed)#左形右边实参
    return jsonify(
        {"items":tasks,
         "page":page,
         "limit":limit,
         "total":len(tasks)
         })
#获取任务
@app.get("/tasks/<int:task_id>")
def ger_task(task_id):
    task=get_task_by_id(task_id)
    if task is None:
        return jsonify({"erroe":"任务不存在"}),404
    return jsonify(task)
#创建任务（单个
@app.post("/tasks")
def create_task_route():
    data=request.get_json()
    if not data or not data.get("title","").strip():
        return jsonify("要输入标题哦")
    title=data["title"].strip()
    if len(title)>100:
        return jsonify("你故意找茬是不是？为什么标题那么长？"),400

    task_id=create_task(title)
    new_task=get_task_by_id(task_id)
    return jsonify(new_task),201

#修改任务
@app.patch("/task/<int:task_id>")
def update_existing_task(task_id):
    data=request.get_json()
    if not data:
        return jsonify("请求为空？")
    title=data.get("title")
    completed=data.get("completed")

    if completed is not None and not isinstance(completed,bool):
        return jsonify("completed得是布尔类型"),404
    updated=update_task(task_id,title=title,completed=completed)
    if not updated:
        return jsonify("你好像没有做任何修改"),404#这里有点问题
    return jsonify(get_task_by_id(task_id))
#删除任务
@app.delete("/task/<int:task_id>")
def delete_existing_task(task_id):
    deleted=delete_task(task_id)
    if not deleted:
        return jsonify("删除失败"),404
    return jsonify("删除成功"),200

if __name__=="__main__":
    app.run(debug=True,port=5000)
