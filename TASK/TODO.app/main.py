from todo import Task, add_task,find_task,delete_task
from storage import load_data,save_data
def main():
    raw_data=load_data()
    tasks=[Task(item["id"],item["title"],item["completed"]) for item in raw_data]

    while True:
        print("\n===== 任务清单 =====")
        print("1. 添加任务")
        print("2. 查看任务")
        print("3. 完成任务")
        print("4. 删除任务")
        print("5. 退出")
        print("====================")

        try:
            choise=int(input("输入你的选择bro"))
            if choise==1:
                title=input("请输入任务名:").strip()
                if not title:
                    print("任务名不能为空:")
                    continue
                add_task(tasks,title)## ##
                save_data([t.to_dict()for t in tasks])##
                print("创建好了！")
            elif choise==2:
                if not tasks:
                    print("没有任务哦")
                else:
                    for t in tasks:
                        status={"已完成"if t.completed else "未完成"}
                        print(f"id:{t.id}|{t.title}|{status}")
            elif choise==3:
                task_id=int(input("输入你完成的任务"))
                t=find_task(tasks,task_id)
                if t:
                    t.completed=True
                    save_data([t.to_dict()for t in tasks])
                    print("任务标记为完成")
                else:
                    print("没找到任务")
            elif choise==4:
                task_id=int(input("输入要删的任务id"))
                task=find_task(tasks,task_id)
                if t:
                    delete_task(tasks,task_id)
                    print("删除成功")
                else:
                    print("任务不存在")
            elif choise==5:
                print("bye~~")
                break
            else:
                print("请输入1~5的数字")
        except ValueError:
            print("你应该输入数字")




if __name__=="__main__":
    main()







