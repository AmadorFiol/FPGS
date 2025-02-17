from toDoList import ToDoList
import unittest
class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todolist=ToDoList()

    #test add_task
    def test_add_task(self):
        self.todolist.add_task("Comprar el pan")
        self.assertIn("Comprar pan",[task.title for task in self.todolist.taskArray])
        
    #test remove_task
    def test_remove_task(self):
        self.todolist.add_task("Comprar el pan")
        self.todolist.remove_task("Comprar el pan")
        self.assertNotIn("Comprar pan",[task.title for task in self.todolist.taskArray])
    #test change_task_status
    def test_change_task_status(self):
        self.todolist.add_task("Comprar el pan")
        self.todolist.change_task_status("Comprar el pan")
        task_status=[task.status for task in self.todolist.taskArray if task.title=="Comprar el pan"][0]
        self.assertTrue(task_status)

    #test get_pending
    def test_get_pending_tasks(self):
        self.todolist.add_task("Comprar el pan")
        self.todolist.add_task("Ir al gym")
        self.todolist.change_task_status("Comprar el pan")
        pending_tasks=self.todolist.get_pending_tasks()
        self.assertIn("Comprar pan",[task.title for task in pending_tasks])
        self.assertNotIn("Ir al gym",[task.title for task in pending_tasks])

    #test get_completed
    def test_get_completed_tasks(self):
        self.todolist.add_task("Comprar el pan")
        self.todolist.add_task("Ir al gym")
        self.todolist.change_task_status("Comprar el pan")
        completed_tasks=self.todolist.get_completed_tasks()
        self.assertNotIn("Comprar pan",[task.title for task in completed_tasks])
        self.assertIn("Ir al gym",[task.title for task in completed_tasks])

if __name__=="__main__":
    unittest.main()