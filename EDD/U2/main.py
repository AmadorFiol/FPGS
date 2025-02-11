from toDoList import ToDoList
def main():
    todolist=ToDoList()
    todolist.add_task("Desinstalar el LOL")
    todolist.add_task("Irse de cañas")
    todolist.add_task("Conducir")

    print(todolist.get_pending_tasks())

    todolist.change_task_status("Conducir")
    print(todolist.get_pending_tasks())

    todolist.remove_task("Irse de cañas")
    print(todolist.get_pending_tasks())



if __name__=="__main__":
    main()