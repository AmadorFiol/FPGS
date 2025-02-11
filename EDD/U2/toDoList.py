class Task:
    def __init__(self, title):
        self.title=title
        self.completed=False

    def change_status(self):
        if self.completed==False:
            self.completed=True
        else:
            self.completed=False

class ToDoList:
    def __init__(self):
        self.taskArray=[]

    def add_task(self,title):
        self.taskArray.append(Task(title))

    def remove_task(self,title):
        for task in self.taskArray:
            if task.title == title:
                self.taskArray.remove(task)

    def change_task_status(self,title):
        for task in self.taskArray:
            if task.title==title:
                task.change_status()
    
    def get_pending_tasks(self):
        return [task.title for task in self.taskArray if not task.completed]
    
    def get_completed_tasks(self):
        return [task.title for task in self.taskArray if task.completed]
